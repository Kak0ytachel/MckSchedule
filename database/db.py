import os
import dotenv
import mysql.connector

from database.classrooms_table import ClassroomsTable
from database.group_lessons_table import GroupLessonsTable
from database.groups_table import GroupsTable
from database.lessons_table import LessonsTable
from database.subgroup_lessons_table import SubgroupLessonsTable
from database.subgroups_table import SubgroupsTable
from database.subjects_table import SubjectsTable
from database.teachers_table import TeachersTable


dotenv.load_dotenv()


class Database:
    def __init__(self):
        print("INITING DATABASE")
        self.mydb = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            autocommit=True,
            port=os.getenv("DB_PORT"),
            # database="schedule"
        )
        self.cursor = self.mydb.cursor(buffered=True)
        # self._drop_database()
        self._init_database()
        self._load_sample_data()

    def _init_database(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS schedule;")
        self.cursor.execute("USE schedule;")
        self.groups_table = GroupsTable(self.cursor)
        self.classrooms_table = ClassroomsTable(self.cursor)
        self.teachers_table = TeachersTable(self.cursor)
        self.subjects_table = SubjectsTable(self.cursor)
        self.lessons_table = LessonsTable(self.cursor)
        self.group_lessons_table = GroupLessonsTable(self.cursor)
        self.subgroups_table = SubgroupsTable(self.cursor)
        self.subgroup_lessons_table = SubgroupLessonsTable(self.cursor)


    def _drop_database(self):
        self.cursor.execute("DROP DATABASE IF EXISTS schedule;")

    def get_group_schedule(self, group_name):
        group_id = self.groups_table.find_group_id(group_name)
        child_subgroup_ids = self.subgroups_table.find_child_subgroups(group_id)
        lessons_ids = []
        lessons_ids.extend(self.group_lessons_table.find_group_lessons_ids(group_id))
        lessons_ids.extend(self.subgroup_lessons_table.find_subgroups_lessons_ids(child_subgroup_ids))
        lessons = self.lessons_table.find_lessons_by_ids(lessons_ids)
        return lessons

    def get_subgroup_schedule(self, subgroup_name, group_name):
        group_id = self.groups_table.find_group_id(group_name)
        subgroup_info = self.subgroups_table.find_subgroup_info_by_name_and_parent(subgroup_name, group_id)
        subgroup_id = subgroup_info['subgroup_id']
        lessons_ids = self.subgroup_lessons_table.find_subgroups_lessons_ids([subgroup_id])
        lessons_ids.extend(self.group_lessons_table.find_group_lessons_ids(group_id))
        lessons = self.lessons_table.find_lessons_by_ids(lessons_ids)
        return lessons

    def extend_lessons_data(self, lessons: list[dict]):

        # makes empty sets for all elements to be fetched
        teachers_initials = set()
        classrooms_ids = set()
        subjects_short_names = set()
        lesson_ids = set()

        # add all elements to be fetched to the sets
        for lesson in lessons:
            teachers_initials.add(lesson['teacher_init'])
            classrooms_ids.add(lesson['classroom_id'])
            subjects_short_names.add(lesson['short_subject_name'])
            lesson_ids.add(lesson['lesson_id'])

        subgroups_ids_by_lesson_ids = self.subgroup_lessons_table.find_subgroups_by_lessons_ids(list(lesson_ids))
        subgroup_ids = [subgroup_id for subgroup_id_list in subgroups_ids_by_lesson_ids.values() for subgroup_id in
                        subgroup_id_list] # makes a list of all subgroup ids needed
        subgroup_names_by_ids = self.subgroups_table.find_subgroup_names(subgroup_ids)
        group_ids_for_subgroups = [i["parent_group_id"] for i in subgroup_names_by_ids.values()] # makes a list of all group ids needed for subgroups

        groups_ids_by_lesson_ids = self.group_lessons_table.find_groups_by_lessons_ids(list(lesson_ids))
        groups_ids: list = [group_id for group_id_list in groups_ids_by_lesson_ids.values() for group_id in group_id_list]
        groups_ids.extend(group_ids_for_subgroups) # adds group ids that are needed for subgroups
        group_names_by_ids = self.groups_table.find_group_names(groups_ids)

        for subgroup_id in subgroup_names_by_ids.keys():
            subgroup_names_by_ids[subgroup_id]["parent_group_name"] = group_names_by_ids[int(subgroup_names_by_ids[subgroup_id]["parent_group_id"])]

        teachers_names = self.teachers_table.find_teacher_names(list(teachers_initials))
        classrooms_names = self.classrooms_table.find_classroom_names(list(classrooms_ids))
        subjects_names = self.subjects_table.find_subject_names(list(subjects_short_names))

        for lesson in lessons:
            lesson['teacher_name'] = teachers_names[lesson['teacher_init']]
            lesson['classroom_name'] = classrooms_names[lesson['classroom_id']]
            lesson['subject_name'] = subjects_names[lesson['short_subject_name']]
            lesson_group_ids = groups_ids_by_lesson_ids[lesson['lesson_id']] if lesson['lesson_id'] in groups_ids_by_lesson_ids.keys() else []
            lesson['groups'] = [group_names_by_ids[group_id] for group_id in lesson_group_ids]
            lesson_subgroup_ids = subgroups_ids_by_lesson_ids[lesson['lesson_id']] if lesson['lesson_id'] in subgroups_ids_by_lesson_ids.keys() else []
            lesson['subgroups'] = [subgroup_names_by_ids[subgroup_id] for subgroup_id in lesson_subgroup_ids]

        return lessons

    def get_child_subgroups(self, group_name):
        group_id = self.groups_table.find_group_id(group_name)
        child_subgroup_info = self.subgroups_table.find_subgroup_info_by_parent(group_id)
        for i in range(len(child_subgroup_info)):
            child_subgroup_info[i]['parent_group_name'] = group_name
        return child_subgroup_info


from database.sample_dataset import load_sample_data
Database._load_sample_data = load_sample_data

if __name__ == "__main__":
    db = Database()
    # db.subgroups_table.add_subgroup(1, "arch", "6N / ARCH")
    # db.subgroup_lessons_table.add_subgroup_lesson(2, 1)
    # db.lessons_tabl
    # db._load_sample_data()
    lessons = db.get_group_schedule("6N")
    print(lessons)
    # print(db.get_subgroup_schedule("inz", "6N"))
    extended_lessons = db.extend_lessons_data(lessons)
    print(extended_lessons)
    # db.mydb.commit()