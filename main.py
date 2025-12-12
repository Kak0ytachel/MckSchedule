from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from db import Database
from database.db import Database
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import unidecode
import random

def fuzzy_search_items(query: str, item_list: list[str], threshold: int = 0) -> list[tuple[str, int]]:
    matches = process.extract(query, item_list, scorer=fuzz.token_sort_ratio)
    filtered_matches = [
        (item, score)
        for item, score in matches
        if score >= threshold
    ]
    return filtered_matches

async def not_found(request: Request, *args):
    return templates.TemplateResponse(name="not_found.html", context={"request": request})

db = Database()
app = FastAPI(exception_handlers={404: not_found})
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/lesson/{id}", response_class=HTMLResponse)
async def get_lesson(request: Request, id: str):
    # lesson_dict = db.find_lesson_by_id(id)
    lesson_data = db.extend_lessons_data([db.lessons_table.find_lesson_by_id(lesson_id=id)])[0]
    print(lesson_data)

    chosen_groups = [i["subgroup_display_name"] for i in lesson_data["subgroups"]]
    chosen_groups.extend(lesson_data["groups"]) # mixed
    return templates.TemplateResponse(name="card_page.html", request=request, context={"lesson": lesson_data, "chosen_groups": chosen_groups})

@app.get("/group/{group_name}")
async def get_group_schedule(request: Request, group_name: str):
    subgroups_data = db.get_child_subgroups(group_name)
    schedule = db.extend_lessons_data(db.get_group_schedule(group_name))
    schedule.sort(key=lambda x: x["weekday"] * 7 * 24 + x["start_hour"] * 60 + x["start_minute"])
    chosen_groups = [i["subgroup_display_name"] for i in subgroups_data]
    chosen_groups.append(group_name) # mixed
    weekday_names = ["None", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return templates.TemplateResponse(name="schedule_group.html", request=request, context={
        "schedule": schedule, "group": group_name, "category_title": group_name, "subgroups_data": subgroups_data,
        "chosen_groups": chosen_groups, "weekday_names": weekday_names})


@app.get("/group/{group_name}/{subgroup_name}")
async def get_subgroup_schedule(request: Request, group_name: str, subgroup_name: str):
    group_id = db.groups_table.find_group_id(group_name)
    subgroup_data = db.subgroups_table.find_subgroup_info_by_name_and_parent(subgroup_name, group_id)
    subgroup_data["parent_group_name"] = group_name
    subgroups_data = [subgroup_data]
    schedule = db.extend_lessons_data(db.get_subgroup_schedule(subgroup_name, group_name))
    schedule.sort(key=lambda x: x["weekday"] * 7 * 24 + x["start_hour"] * 60 + x["start_minute"])
    chosen_groups = [subgroup_data["subgroup_display_name"], group_name] # mixed
    weekday_names = ["None", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return templates.TemplateResponse(name="schedule_group.html", request=request, context={
        "schedule": schedule, "group": group_name, "category_title": subgroup_data["subgroup_display_name"],
        "subgroups_data": subgroups_data, "chosen_groups": chosen_groups, "weekday_names": weekday_names})


@app.get("/hello/{name}", response_class=HTMLResponse)
async def say_hello(request: Request, name: str):
    return templates.TemplateResponse(name="hello_world.html", context={"request": request, "name": name})
    # return {"message": f"Hello {name}"}

@app.get("/search")
async def search(request: Request):
    print(request)
    search_request = unidecode.unidecode(request.query_params.get("q"))
    print(search_request)
    group_names = db.groups_table.get_all_group_names()
    subgroups_data = db.subgroups_table.get_all_subgroups()
    #TODO: unidecode subgroup display names with making backwards transition dict
    subgroup_names = [i["subgroup_display_name"] for i in subgroups_data]
    if search_request in group_names:
        return RedirectResponse(url=f"/group/{search_request}")
    names = group_names.copy()
    names.extend(subgroup_names)
    matches = fuzzy_search_items(search_request, names)
    if len(matches) == 0:
        return RedirectResponse(url="/")
        #TODO: show nothing found
    elif matches[0][1] > 85:
        name = matches[0][0]
        if name in group_names:
            return RedirectResponse(url=f"/group/{name}")
        subgroup_data = list(filter(lambda x: (x["subgroup_display_name"] == name), subgroups_data))[0]
        print(subgroup_data)
        group_id = subgroup_data["group_id"]
        group_name = db.groups_table.find_group_names([group_id])[group_id]
        print(group_name)
        return RedirectResponse(url=f"/group/{group_name}/{subgroup_data['subgroup_name']}")

    #TODO: add search page
    search_items = []
    for i in matches:
        name = i[0]
        if name in group_names:
            link = f"/group/{name}"
            data_subgroup = "group"
        else:
            subgroup_data = list(filter(lambda x: (x["subgroup_display_name"] == name), subgroups_data))[0]
            group_id = subgroup_data["group_id"]
            group_name = db.groups_table.find_group_names([group_id])[group_id]
            link = f"/group/{group_name}/{subgroup_data['subgroup_name']}"
            name = subgroup_data["subgroup_display_name"]
            data_subgroup = subgroup_data["subgroup_name"]
        search_items.append({"link": link, "data_subgroup": data_subgroup, "name": name})
    #TODO: add freq check
    common_items = []
    common_names = ['6N', '6N / inz', '6N / arch'] #TODO fix
    for name in common_names:
        if name in group_names:
            link = f"/group/{name}"
            data_subgroup = "group"
        else:
            subgroup_data = list(filter(lambda x: (x["subgroup_display_name"] == name), subgroups_data))[0]
            group_id = subgroup_data["group_id"]
            group_name = db.groups_table.find_group_names([group_id])[group_id]
            link = f"/group/{group_name}/{subgroup_data['subgroup_name']}"
            name = subgroup_data["subgroup_display_name"]
            data_subgroup = subgroup_data["subgroup_name"]
        common_items.append({"link": link, "data_subgroup": data_subgroup, "name": name})
    return templates.TemplateResponse(name="search.html", context={"request": request, "matches": matches, "query": search_request, "search_groups": search_items, "common_items": common_items})

@app.get("/changelog", response_class=HTMLResponse)
async def changelog(request: Request):
    return templates.TemplateResponse(name="changelog.html", context={"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(name="about.html", context={"request": request})

@app.get("/", response_class=HTMLResponse)
async def main_test(request: Request):
    lessons = db.lessons_table.get_all_lessons()
    lessons = db.extend_lessons_data(lessons)
    radius = 300
    elements = []
    lessons_numer = random.randint(min(10, len(lessons)), len(lessons))
    for lesson in (random.sample(lessons, lessons_numer)):
        groups = lesson['groups'] + [i['subgroup_display_name'] for i in lesson['subgroups']]
        lesson['chosen_group'] = random.choice(groups)
        item = {'lesson': lesson,
                'x': str(random.randint(-1 * radius, radius)),
                'y': str(random.randint(-1 * radius, radius)),
                'rotate': str(random.randint(-180, 180))
                }
        elements.append(item)
        print(item)

    groups: dict = db.groups_table.get_all_groups()
    subgroups = db.subgroups_table.get_all_subgroups()
    group_items = []
    for group in groups.values():
        item = {'link': f"/group/{group}", 'name': group, 'data_subgroup': 'group'}
        group_items.append(item)
    for subgroup in subgroups:
        group_id = subgroup['group_id']
        group_name = groups[group_id]
        item = {'link': f"/group/{group_name}/{subgroup['subgroup_name']}", 'name': subgroup['subgroup_display_name'], 'data_subgroup': subgroup['subgroup_name']}
        group_items.append(item)
    random.shuffle(group_items)
    return templates.TemplateResponse(name="home.html", context={"request": request, "elements": elements, "groups": group_items})


    # return templates.TemplateResponse(name="search.html", context={"request": request})

# @app.get("/group/{group_id}")
# async def get_group(group_id: str):
#     return db.find_all_lessons_by_group_id(group_id)
#     return {"message": f"Hello {group_name}"}
#
# @app.get("/group/{group_id}/{subgroup_name}")
# async def get_subgroup(group_id: str, subgroup_name: str):
#     available_subgroups = db.find_subgroup_names(group_id)
#     print(available_subgroups)
#     if subgroup_name.lower() not in [i.lower() for i in available_subgroups]:
#         return RedirectResponse(url=f"/group/{group_id}")
#     return db.get_subgroup_schedule(subgroup_name, group_id)
#     return {"message": f"Hello {group_name}/{subgroup_name}/{subgroup_name}"}

class Lesson:
    subgroup_names: list[str]
    weekday: int
    start_hour: int
    start_minute: int
    end_hour: int
    end_minute: int

if __name__ == "__main__":
    print(db.subgroups_table.find_child_subgroups("6N"))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, proxy_headers=True, forwarded_allow_ips="*")

