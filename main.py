from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse
import re

# from db import Database
from database.db import Database
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import unidecode
import random
from datetime import datetime, timedelta, date
from markupsafe import Markup

from database.statistics_table import StatsData
from database.subgroups_table import SubgroupData
from language_manager import LanguageManager, DEFAULT_LANGUAGE


def fuzzy_search_items(query: str, item_list: list[str], threshold: int = 40) -> list[tuple[str, int]]:
    keys_list = []
    items_dict = {}
    for item in item_list:
        for key in item['names']:
            keys_list.append(unidecode.unidecode(key))
            items_dict[unidecode.unidecode(key)] = item
    matches = process.extract(unidecode.unidecode(query), keys_list, scorer=fuzz.token_sort_ratio, limit=10)
    print(matches)
    items_added = set()
    filtered_matches = []
    for key, score in matches:
        if score >= threshold and items_dict[key]['display_name'] not in items_added:
            filtered_matches.append((items_dict[key], score))
            items_added.add(items_dict[key]['display_name'])
    print(filtered_matches)
    return filtered_matches

async def not_found(request: Request, *args):
    return templates.TemplateResponse(name="not_found.html", context={"request": request})

db = Database()
app = FastAPI(exception_handlers={404: not_found})
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


lm = LanguageManager()

def translate(request: Request, key: str, *args) -> str:
    lang = get_lang(request)
    text = lm.get(lang, key)
    # print("*args: ", args)
    text = text.format(*args) # {}, {0}
    return Markup(text)

templates.env.globals.update(translate=translate)

search_options = []



def get_notification_messages(request: Request, schedule_type: str, **kwargs):
    notification_messages = []
    if schedule_type == "group" or schedule_type == "subgroup":
        group_name = kwargs["group_name"]
        semester_id = kwargs["semester_id"]
        is_not_uploaded = (group_name not in ["6N", "5N", "4N", "3N", "2N"] and semester_id == 1)
        if is_not_uploaded:
            notification_message = translate(request, "schedule-not-uploaded-message", '<u>', '</u>',
                                             '<a class="underline-link" href="https://t.me/dokpdl">', '</a>')
            notification_messages.append(notification_message)
        is_not_checked = (semester_id == 2)
        if is_not_checked:
            notification_message = translate(request, "schedule-not-checked-message", '<u>', '</u>', '<u>', '</u>', '<u>', '</u>', '<a class="underline-link" href="https://t.me/dokpdl">', '</a>')
            notification_messages.append(notification_message)
    if schedule_type == "teacher":
        teacher_name: str = kwargs["teacher_name"]
        if teacher_name.count("?") > 0:
            notification_message = translate(request, "schedule-unknown-teacher-message", '<a class="underline-link" href="https://t.me/dokpdl">', '</a>')
            notification_messages.append(notification_message)
    if date(2026, 2, 21) < date.today() < date(2026, 3, 1):
        notification_message = translate(request, "schedule-updated-message", "<u>", "</u>")
        notification_messages.append(notification_message)
    return notification_messages

@app.get("/lesson/{id}", response_class=HTMLResponse)
async def get_lesson(request: Request, id: str):
    # lesson_dict = db.find_lesson_by_id(id)
    lesson_data = db.extend_lessons_data([db.lessons_table.find_lesson_by_id(lesson_id=id)])[0]
    print(lesson_data)

    chosen_groups = [i["subgroup_display_name"] for i in lesson_data["subgroups"]]
    chosen_groups.extend(lesson_data["groups"]) # mixed
    return templates.TemplateResponse(name="card_page.html", request=request, context={"lesson": lesson_data, "chosen_groups": chosen_groups})

@app.get("/group/{group_name}/semester/{semester_id}")
@app.get("/group/{group_name}")
async def get_group_schedule(request: Request, group_name: str, semester_id: int = None):
    if group_name not in db.groups_table.get_all_group_names():
        return RedirectResponse(url="/not-found")

    if semester_id is None:
        semester_id = db.semesters_table.get_current_semester_id()

    schedule = db.get_schedule_from_group(group_name, semester_id)


    subgroups_data = db.get_child_subgroups(group_name)


    chosen_groups = [i["subgroup_display_name"] for i in subgroups_data]
    chosen_groups.append(group_name) # mixed

    notification_messages = get_notification_messages(request, "group", group_name=group_name, semester_id=semester_id)

    group_id = db.groups_table.find_group_id(group_name)
    db.statistics_table.insert("group", item_id=group_id)

    base_link = "/group/" + group_name
    semesters = make_semesters(base_link, semester_id)

    header_links = []
    header_links.extend([{"link": f"/group/{i["parent_group_name"]}/{i["subgroup_name"]}",
                          "name": i["subgroup_display_name"],
                          "data_subgroup": i["subgroup_name"]} for i in subgroups_data])
    header_links.append({"link": f"/group/{group_name}", "name": group_name, "data_subgroup": "group"})

    print(db.statistics_table.count_all_time("group", group_id))

    return templates.TemplateResponse(name="schedule_group.html", request=request, context={
        "schedule": schedule, "group": group_name, "category_title": group_name, "subgroups_data": subgroups_data,
        "chosen_groups": chosen_groups, "notification_messages": notification_messages,
        "header_links": header_links, "semesters": semesters})


@app.get("/group/{group_name}/{subgroup_name}")
@app.get("/group/{group_name}/{subgroup_name}/semester/{semester_id}")
async def get_subgroup_schedule(request: Request, group_name: str, subgroup_name: str, semester_id: int = None):

    if semester_id is None:
        semester_id = db.semesters_table.get_current_semester_id()

    group_id = db.groups_table.find_group_id(group_name)
    subgroup_data = db.subgroups_table.find_subgroup_info_by_name_and_parent(subgroup_name, group_id)
    subgroup_data["parent_group_name"] = group_name
    subgroups_data = [subgroup_data]
    schedule = db.extend_lessons_data(db.get_subgroup_schedule(subgroup_name, group_name))
    schedule = list(filter(lambda x: (x['semester_id'] == semester_id), schedule)) #TODO: replace with mega query
    schedule.sort(key=lambda x: x["weekday"] * 7 * 24 + x["start_hour"] * 60 + x["start_minute"])
    chosen_groups = [subgroup_data["subgroup_display_name"], group_name] # mixed

    notification_messages = get_notification_messages(request, "subgroup", group_name=group_name, subgroup_name=subgroup_name, semester_id=semester_id)

    base_link = "/group/" + group_name + "/" + subgroup_name
    semesters = make_semesters(base_link, semester_id)

    header_links = []
    header_links.extend(
        [{"link": f"/group/{i["parent_group_name"]}/{i["subgroup_name"]}", "name": i["subgroup_display_name"], "data_subgroup": i["subgroup_name"]} for i in
         subgroups_data])
    header_links.append({"link": f"/group/{group_name}", "name": group_name, "data_subgroup": "group"})

    subgroup_id = subgroup_data["subgroup_id"]
    db.statistics_table.insert("subgroup", item_id=subgroup_id)
    print(schedule)
    return templates.TemplateResponse(name="schedule_group.html", request=request, context={
        "schedule": schedule, "group": group_name, "category_title": subgroup_data["subgroup_display_name"],
        "subgroups_data": subgroups_data, "chosen_groups": chosen_groups,
        "notification_messages": notification_messages, "header_links": header_links, "semesters": semesters, })

@app.get("/classroom/{classroom_short_name}")
@app.get("/classroom/{classroom_short_name}/semester/{semester_id}")
async def get_classroom_schedule(request: Request, classroom_short_name: str, semester_id: int = None):
    if semester_id is None:
        semester_id = db.semesters_table.get_current_semester_id()

    classroom_short_name = classroom_short_name.lower()
    classroom_id = db.classrooms_table.find_classroom_id_by_short_name(classroom_short_name)
    classroom_display_name = db.classrooms_table.find_classroom_display_name(classroom_id)
    schedule = db.extend_lessons_data(db.lessons_table.find_lessons_by_classroom_id(classroom_id, semester_id))
    schedule.sort(key=lambda x: x["weekday"] * 7 * 24 + x["start_hour"] * 60 + x["start_minute"])
    chosen_groups = 'all'

    notification_messages = [] #TODO

    base_link = "/classroom/" + classroom_short_name
    semesters = make_semesters(base_link, semester_id)

    db.statistics_table.insert("classroom", item_id=classroom_id)


    return templates.TemplateResponse(name="schedule_group.html", request=request, context={
        "schedule": schedule, "group": [], "category_title": classroom_display_name,
        "subgroups_data": [], "chosen_groups": chosen_groups,
        "notification_messages": notification_messages, "header_links": [], "semesters": semesters})

# TODO: add logger

@app.get("/search")
async def search(request: Request):
    search_request = unidecode.unidecode(request.query_params.get("q"))

    global search_options
    if len(search_options) == 0:
        search_options = make_search_options()
    matches = fuzzy_search_items(search_request, search_options)

    search_items = [i[0] for i in matches]
    if len(matches) > 0:
        if matches[0][1] > 85:
            return RedirectResponse(url=matches[0][0]['link'])

    before = datetime.now() - timedelta(days=7)
    stats = db.statistics_table.count_all_elements(before, datetime.now())

    stats = make_stats(stats)

    max_len = 20
    if len(stats) > max_len:
        stats = stats[:max_len]

    return templates.TemplateResponse(name="search.html", context={"request": request, "matches": matches, "query": search_request, "search_items": search_items, "common_items": stats})

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
    min_cards = 20
    max_cards = 40
    lessons_numer = random.randint(min(min_cards, len(lessons)), min(len(lessons), max_cards))
    for lesson in (random.sample(lessons, lessons_numer)):
        groups = lesson['groups'] + [i['subgroup_display_name'] for i in lesson['subgroups']]
        lesson['chosen_group'] = random.choice(groups) if len(groups) > 0 else None
        item = {'lesson': lesson,
                'x': str(random.randint(-1 * radius, radius)),
                'y': str(random.randint(-1 * radius, radius)),
                'rotate': str(random.randint(-180, 180))
                }
        elements.append(item)
        # print(item)

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

@app.get("/teacher/{teacher_init}", response_class=HTMLResponse)
@app.get("/teacher/{teacher_init}/semester/{semester_id}", response_class=HTMLResponse)
def get_teacher_schedule(request: Request, teacher_init: str, semester_id: int = None):
    if semester_id is None:
        semester_id = db.semesters_table.get_current_semester_id()

    name = db.teachers_table.find_teacher_name(teacher_init)
    lessons = db.lessons_table.find_lessons_by_teacher_initials(teacher_init, semester_id)
    lessons = db.extend_lessons_data(lessons)

    notification_messages = get_notification_messages(request, "teacher", teacher_init=teacher_init, teacher_name=name, semester_id=semester_id)


    db.statistics_table.insert("teacher", item_name=teacher_init)
    lessons.sort(key=lambda x: x["weekday"] * 7 * 24 + x["start_hour"] * 60 + x["start_minute"])
    chosen_groups = 'all'

    base_link = "/teacher/" + teacher_init
    semesters = make_semesters(base_link, semester_id)

    return templates.TemplateResponse(name="schedule_group.html", context={
        "request": request, "schedule": lessons, "chosen_groups": chosen_groups, "category_title": name,
        "semesters": semesters, "notification_messages": notification_messages,})

def make_search_options() -> list[dict]:
    options = []
    groups_dict = db.groups_table.get_all_groups()
    group_names = list(groups_dict.values())
    for i in group_names:
        options.append({"link": f"/group/{i}", "names": [i],  "display_name": i, "data_subgroup": "group"})

    subgroups_data = db.subgroups_table.get_all_subgroups()
    for i in subgroups_data:
        group_id = i["group_id"]
        group_name = groups_dict[group_id]
        options.append({"link": f"/group/{group_name}/{i['subgroup_name']}", "names": [i["subgroup_display_name"]], "display_name": i["subgroup_display_name"], "data_subgroup": i["subgroup_name"]})

    teachers = db.teachers_table.get_all_teachers()
    for teacher in teachers.items():
        options.append({"link": f"/teacher/{teacher[0]}", "names": [teacher[0], teacher[1]], "display_name": teacher[1], "data_subgroup": "teacher"})

    classrooms = db.classrooms_table.get_classroom_names()
    for classroom in classrooms.items():
        options.append({"link": f"/classroom/{classroom[0]}", "names": [classroom[1], classroom[0]], "display_name": classroom[1], "data_subgroup": "classroom"})

    return options

@app.get("/api/search_index", response_class=JSONResponse)
def api_get_search_options():
    global search_options
    if len(search_options) == 0:
        search_options = make_search_options()
    return JSONResponse(content=search_options)

@app.get("/api/statistics", response_class=JSONResponse)
def api_get_statistics():
    content = db.statistics_table.count_all_elements(datetime(1970, 1, 1), datetime.now())
    return JSONResponse(content=content)

def make_stats(stats: list[dict]):
    groups = db.groups_table.get_all_groups()
    subgroups = db.subgroups_table.get_all_subgroups_dict()
    teachers = db.teachers_table.get_all_teachers()
    classrooms = db.classrooms_table.get_classroom_data()
    # print(max_value)
    for i in stats:
        i['data_subgroup'] = i['item_type']
        if i['item_type'] == "group":
            i['display_name'] = groups[i['item_id']]
            i["link"] = '/group/' + groups[i['item_id']]
        if i['item_type'] == "subgroup":
            i['display_name'] = subgroups[i['item_id']]['subgroup_display_name']
            subgroup_data: SubgroupData = subgroups[i['item_id']]
            i['link'] = '/group/' + groups[subgroup_data['group_id']] + "/" + subgroup_data['subgroup_name']
            i['data_subgroup'] = subgroup_data['subgroup_name']
        if i['item_type'] == "teacher":
            i['display_name'] = teachers[i['item_name']]
            i['link'] = '/teacher/' + i['item_name']
        if i['item_type'] == "classroom":
            i['display_name'] = classrooms[i['item_id']]['classroom_display_name']
            i['link'] = '/classroom/' + classrooms[i['item_id']]['classroom_short_name']
    return stats

@app.get("/statistics/{period}")
@app.get("/statistics")
def get_statistics(request: Request, period: str = "all"):
    if period not in ['all', '1d', '3d', '7d', '30d']:
        return RedirectResponse(url="/statistics")
    if period == "all":
        before = datetime(1970, 1, 1)
    else:
        before = datetime.now() - timedelta(days=int(period[:-1]))
    stats = db.statistics_table.count_all_elements(before, datetime.now())
    stats = make_stats(stats)
    max_value = max([i['count'] for i in stats]) if len(stats) > 0 else 0
    max_width = 50
    for i in stats:
        i['width'] = max_width / max_value * i['count']
    # return JSONResponse(content=stats)
    return templates.TemplateResponse(name="statistics.html", context={"request": request, "stats": stats, "period": period,
                                                                       "options": ["1d", "3d", "7d", "30d", "all"]})


@app.post("/api/lang")
def set_lang(request: Request, lang: str = Form(...)):
    print(lang)
    referer_url = request.headers.get("referer", '/')
    response = RedirectResponse(url=referer_url, status_code=303)
    response.set_cookie(key="lang", value=lang)
    return response

@app.get("/test/lang")
def get_lang(request: Request):
    lang = request.cookies.get("lang")
    lang = lang[:2] if lang is not None and len(lang) > 0 else None
    # print("cookie_lang: ", lang)
    if lang is None:
        # print(request.headers.get("accept-language"))
        pattern = r'([a-z]{2})(?:-[A-Z]{2,4})?(?=[,;]|$)'
        languages = list(re.findall(pattern, request.headers.get("accept-language")))
        # print(languages)
        for i in languages:
            if lm.check_lang(i):
                return i
        return DEFAULT_LANGUAGE
    return lm.check_get_lang(lang)


def make_semesters(base_link, semester_id) -> dict:
    semesters = db.semesters_table.get_semesters()
    for i in semesters:
        i['is_default'] = i['semester_id'] == db.semesters_table.get_current_semester_id()
        i['is_chosen'] = i['semester_id'] == semester_id
        i['link'] = base_link + "/semester/" + str(i["semester_id"]) if not i['is_default'] else base_link
    return semesters


@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse(name="login.html", context={"request": request})

if __name__ == "__main__":
    print(db.subgroups_table.find_child_subgroups("6N"))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, proxy_headers=True, forwarded_allow_ips="*")

