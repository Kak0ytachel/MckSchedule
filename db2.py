import mysql.connector

from database.classrooms_table import ClassroomsTable
from database.group_lessons_table import GroupLessonsTable
from database.groups_table import GroupsTable
from database.lessons_table import LessonsTable
from database.subgroup_lessons_table import SubgroupLessonsTable
from database.subgroups_table import SubgroupsTable
from database.subjects_table import SubjectsTable
from database.teachers_table import TeachersTable


class Database:
    def __init__(self):
        print("INITING DATABASE")
        self.mydb = mysql.connector.connect(
            host="db",
            user="root",
            password="123456q",
            autocommit=True,
            port="3306"
            # database="schedule"
        )
        self.cursor = self.mydb.cursor(buffered=True)
        # self._drop_database()
        self._init_database()

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

    def _load_sample_data(self):
        self._drop_database()
        self._init_database()

        group_1n = self.groups_table.add_group("1N")
        group_2n = self.groups_table.add_group("2N")
        group_3n = self.groups_table.add_group("3N")
        group_4n = self.groups_table.add_group("4N")
        group_5n = self.groups_table.add_group("5N")
        group_6n = self.groups_table.add_group("6N")
        group_1s = self.groups_table.add_group("1S")
        group_2s = self.groups_table.add_group("2S")
        group_3s = self.groups_table.add_group("3S")
        group_4s = self.groups_table.add_group("4S")
        group_5s = self.groups_table.add_group("5S")

        subgroup_1n_inz = self.subgroups_table.add_subgroup(group_1n, "inz", "1N / inz")
        subgroup_1n_art = self.subgroups_table.add_subgroup(group_1n, "art", "1N / art")
        subgroup_1n_arch = self.subgroups_table.add_subgroup(group_1n, "arch", "1N / arch")

        subgroup_2n_inz = self.subgroups_table.add_subgroup(group_2n, "inz", "2N / inz")
        subgroup_2n_art = self.subgroups_table.add_subgroup(group_2n, "art", "2N / art")

        subgroup_3n_arch = self.subgroups_table.add_subgroup(group_3n, "arch", "3N / arch")
        subgroup_3n_ekon = self.subgroups_table.add_subgroup(group_3n, "ekon", "3N / ekon")

        subgroup_4n_inz = self.subgroups_table.add_subgroup(group_4n, "inz", "4N / inz")
        subgroup_4n_ekon = self.subgroups_table.add_subgroup(group_4n, "ekon", "4N / ekon")

        subgroup_5n_art = self.subgroups_table.add_subgroup(group_5n, "art", "5N / art")
        subgroup_5n_ekon = self.subgroups_table.add_subgroup(group_5n, "ekon", "5N / ekon")

        subgroup_6n_inz = self.subgroups_table.add_subgroup(group_6n, "inz", "6N / inz")
        subgroup_6n_arch = self.subgroups_table.add_subgroup(group_6n, "arch", "6N / arch")

        subgroup_4s_ekon = self.subgroups_table.add_subgroup(group_4s, "ekon", "4S / ekon")
        subgroup_4s_art = self.subgroups_table.add_subgroup(group_4s, "art", "4S / art")
        subgroup_4s_arch = self.subgroups_table.add_subgroup(group_4s, "arch", "4S / arch")

        subgroup_5s_ekon = self.subgroups_table.add_subgroup(group_5s, "ekon", "5S / ekon")
        subgroup_5s_art = self.subgroups_table.add_subgroup(group_5s, "art", "5S / art")


        classroom_warszawa = self.classrooms_table.add_classroom("Warszawa (14)")
        classroom_wroclaw = self.classrooms_table.add_classroom("Wrocław (14)")
        classroom_krakow = self.classrooms_table.add_classroom("Krakow (15)")
        classroom_lodz = self.classrooms_table.add_classroom("Łódź (13)")
        classroom_gdansk = self.classrooms_table.add_classroom("Gdańsk (16)")
        classroom_poznan = self.classrooms_table.add_classroom("Poznań")
        classroom_seminar = self.classrooms_table.add_classroom("Sała seminaryjna")
        classroom_komp = self.classrooms_table.add_classroom("Sała komputerowa")
        classroom_konfer = self.classrooms_table.add_classroom("Sała konferencyjna")
        classroom_proj = self.classrooms_table.add_classroom("Sała projektowa")

        self.teachers_table.add_teacher("KGR", "Kinga Górecka-Rokita")
        self.teachers_table.add_teacher("JK", "Justyna Krztoń")
        self.teachers_table.add_teacher("EG", "Edyta Gałat")
        self.teachers_table.add_teacher("JPM", "Joanna Piera-Mitka")
        self.teachers_table.add_teacher("TJ", "Tomasz Jeleński")

        self.teachers_table.add_teacher("IKA", "Izabela Kugiel-Abuhasna")
        self.teachers_table.add_teacher("WO", "Witold Obloza")
        self.teachers_table.add_teacher("MD", "Małgorzata Duraj")
        self.teachers_table.add_teacher("AN", "Artur Niewiarowski")
        self.teachers_table.add_teacher("WG", "WG (?)")


        self.subjects_table.add_subject("mat-i", "Matematyka inz.")
        self.subjects_table.add_subject("fiz", "Fizyka inz.")
        self.subjects_table.add_subject("inf-i", "Informatyka inz.")
        self.subjects_table.add_subject("jn", "Język naukowy")

        self.subjects_table.add_subject("kscz", "KSCz")
        self.subjects_table.add_subject("gp", "GP")
        self.subjects_table.add_subject("wop", "WOP")
        self.subjects_table.add_subject("konw", "Konwersatorium")
        self.subjects_table.add_subject("dkf", "DKF")

        self.subjects_table.add_subject("mat-ea", "Matematyka ekon./arch.")
        self.subjects_table.add_subject("fp", "Film polski")
        self.subjects_table.add_subject("sa", "Słownictwo architektoniczne")
        self.subjects_table.add_subject("ha", "Historia architektury")
        self.subjects_table.add_subject("rarch", "Rysunek architektoniczny")
        # self.subjects_table.add_subject("")


        i = self.lessons_table.add_lesson("mat-i", classroom_warszawa, "WO", 1,
                                                  9,50, 11, 20)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

        i = self.lessons_table.add_lesson("dkf", classroom_gdansk, "TJ", 1, 18, 0, 20, 15)
        self.group_lessons_table.add_group_lesson(group_6n, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_arch, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_inz, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

        i = self.lessons_table.add_lesson("wop", classroom_gdansk, "EG", 2, 8, 0, 9, 30)
        self.group_lessons_table.add_group_lesson(group_6n, i)
        self.group_lessons_table.add_group_lesson(group_5n, i)

        i = self.lessons_table.add_lesson("kscz", classroom_krakow, "KGR", 2,
                                                   9, 50, 11, 20)
        self.group_lessons_table.add_group_lesson(group_6n, i)

        i = self.lessons_table.add_lesson("jn", classroom_lodz, "IKA", 2, 11, 40, 13, 10)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

        i = self.lessons_table.add_lesson("fiz", classroom_lodz, "MD", 2, 15, 15, 16, 45)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

        i = self.lessons_table.add_lesson("mat-i", classroom_krakow, "WO", 2, 17, 00, 18, 30)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

        i = self.lessons_table.add_lesson("inf-i", classroom_komp, "AN", 3, 8, 15, 9, 45)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

        i = self.lessons_table.add_lesson("konw", classroom_poznan, "JPM", 3, 11, 40, 13, 10)
        self.group_lessons_table.add_group_lesson(group_6n, i)

        i = self.lessons_table.add_lesson("gp", classroom_krakow, "JK", 4, 8, 00, 9, 30)
        self.group_lessons_table.add_group_lesson(group_6n, i)

        i = self.lessons_table.add_lesson("inf-i", classroom_komp, "AN", 4, 10, 0, 11, 30)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

        i = self.lessons_table.add_lesson("gp", classroom_krakow, "JK", 4, 11, 40, 13, 10)
        self.group_lessons_table.add_group_lesson(group_6n, i)

        i = self.lessons_table.add_lesson("kscz", classroom_lodz, "KGR", 4,13, 30, 15, 0)
        self.group_lessons_table.add_group_lesson(group_6n, i)

        i = self.lessons_table.add_lesson("fiz", classroom_lodz, "MD", 4, 17, 00, 18, 30)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

        i = self.lessons_table.add_lesson("gp", classroom_lodz, "JK", 5, 8, 0, 9, 30)
        self.group_lessons_table.add_group_lesson(group_6n, i)

        i = self.lessons_table.add_lesson("kscz", classroom_krakow, "KGR", 5, 11, 40, 13, 10)
        self.group_lessons_table.add_group_lesson(group_6n, i)


        i = self.lessons_table.add_lesson("fp", classroom_gdansk, "TJ", 1, 15, 15, 17, 30)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_ekon, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_ekon, i)
        self.group_lessons_table.add_group_lesson(group_1s, i)
        self.group_lessons_table.add_group_lesson(group_2s, i)

        i = self.lessons_table.add_lesson("fp", classroom_gdansk, "TJ", 3, 15, 15, 17, 30)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_art, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_art, i) #TODO: fix conflicts
        # self.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_ekon, i) # wtf it duplicates
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_art, i) #wtf duplicats
        self.group_lessons_table.add_group_lesson(group_4s, i)

        i = self.lessons_table.add_lesson("fp", classroom_gdansk, "TJ", 3, 18, 0, 20, 15)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_art, i) # duplicates
        # self.group_lessons_table.add_group_lesson(group_5n, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_ekon, i)
        self.group_lessons_table.add_group_lesson(group_4s, i) # duplicates
        self.group_lessons_table.add_group_lesson(group_5s, i)

        i = self.lessons_table.add_lesson("ha", classroom_lodz, "EG", 1, 9, 50, 11, 20)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_arch, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_arch, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_arch, i)

        i = self.lessons_table.add_lesson("sa", classroom_lodz, "EG", 1, 11, 40, 13, 10)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_arch, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_arch, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_arch, i)
        # self.lessons_table.add_lesson("math", 1, "123456", 1, 23, 59, 23, 59)

        i = self.lessons_table.add_lesson("rarch", classroom_konfer, "WG", 2, 15, 15, 18, 15)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_arch, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_arch, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_arch, i)

        i = self.lessons_table.add_lesson("mat-ea", classroom_krakow, "WO", 4, 13, 30, 15, 0)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
        # self.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_???) #TODO add
        self.group_lessons_table.add_group_lesson(subgroup_3n_ekon, i)

        i = self.lessons_table.add_lesson("mat-ea", classroom_krakow, "WO", 4, 15, 15, 16, 45)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_ekon, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_ekon, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_arch, i)

        i = self.lessons_table.add_lesson("mat-ea", classroom_konfer, "WO", 1, 8, 0, 9, 30)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_ekon, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_ekon, i)
        self.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_arch, i)


if __name__ == "__main__":
    db = Database()
    # db.subgroups_table.add_subgroup(1, "arch", "6N / ARCH")
    # db.subgroup_lessons_table.add_subgroup_lesson(2, 1)
    # db.lessons_tabl
    db._load_sample_data()
    lessons = db.get_group_schedule("6N")
    print(lessons)
    # print(db.get_subgroup_schedule("inz", "6N"))
    extended_lessons = db.extend_lessons_data(lessons)
    print(extended_lessons)
    # db.mydb.commit()