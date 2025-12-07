import mysql.connector
from mysql.connector.cursor import MySQLCursor


class BaseTable:
    def __init__(self, cursor):
        self.name = self.__class__.__name__
        self.cursor: MySQLCursor = cursor

    def _create_table(self):
        print(f"No method to create table {self.name}")

    def _drop_table(self):
        print(f"No method to drop table {self.name}")

class LessonsTable(BaseTable):
    def __init__(self, cursor):
        super().__init__(cursor)
        self._create_table()

    def _create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS lessons ("
                            "lesson_id INT AUTO_INCREMENT PRIMARY KEY,"
                            "short_subject_name VARCHAR(255) NOT NULL DEFAULT 'N/A',"
                            "classroom_id INT NOT NULL DEFAULT 0,"
                            "teacher_initials VARCHAR(255) NOT NULL DEFAULT 'N/A',"
                            "weekday INT NOT NULL DEFAULT 7,"
                            "start_hour INT NOT NULL DEFAULT 23,"
                            "start_minute INT NOT NULL DEFAULT 59,"
                            "end_hour INT NOT NULL DEFAULT 23,"
                            "end_minute INT NOT NULL DEFAULT 59,"
                            "FOREIGN KEY (short_subject_name) REFERENCES subjects(subject_short_name),"
                            "FOREIGN KEY (classroom_id) REFERENCES classrooms(classroom_id), "
                            "FOREIGN KEY (teacher_initials) REFERENCES teachers(teacher_initials)"
                            ");")
        # TODO Add foreign keys

    def add_lesson(self, short_subject_name: str, classroom_id: int, teacher_initials: str, weekday: int,  start_hour: int,
                   start_minute: int, end_hour: int, end_minute: int) -> int:
        self.cursor.execute("INSERT INTO lessons (short_subject_name, classroom_id, teacher_initials, weekday, start_hour, "
                            "start_minute, end_hour, end_minute) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                            (short_subject_name, classroom_id, teacher_initials, weekday, start_hour, start_minute,
                             end_hour, end_minute))
        lesson_id = self.cursor.lastrowid
        return lesson_id

    def find_lesson_by_id(self, lesson_id: int) -> dict:
        self.cursor.execute("SELECT * FROM lessons WHERE lesson_id=%s;", (lesson_id,))
        item = self.cursor.fetchone()
        if item is None:
            return {}
        lesson = {'lesson_id': item[0],
                  'short_subject_name': item[1],
                  'classroom_id': item[2],
                  'teacher_init': item[3],
                  'weekday': item[4],
                  'start_hour': item[5],
                  'start_minute': item[6],
                  'end_hour': item[7],
                  'end_minute': item[8]
        }
        return lesson

    def find_lessons_by_ids(self, lesson_ids: list[str | int]) -> list[dict]:
        if len(lesson_ids) == 0:
            return []
        if len(lesson_ids) == 1:
            return [self.find_lesson_by_id(lesson_ids[0])]
        self.cursor.execute("SELECT * FROM lessons WHERE lesson_id IN (%s);" % ", ".join(["%s"] * len(lesson_ids)),
                            lesson_ids)
        lessons = []
        for item in self.cursor.fetchall():
            lesson = {'lesson_id': item[0],
                      'short_subject_name': item[1],
                      'classroom_id': item[2],
                      'teacher_init': item[3],
                      'weekday': item[4],
                      'start_hour': item[5],
                      'start_minute': item[6],
                      'end_hour': item[7],
                      'end_minute': item[8]
            }
            lessons.append(lesson)
        return lessons

class GroupsTable(BaseTable):
    def __init__(self, cursor):
        super().__init__(cursor)
        self._create_table()

    def _create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS student_groups ("
                            "group_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                            "group_name VARCHAR(255)"
                            ");")

    def add_group(self, group_name: str) -> int:
        self.cursor.execute("INSERT INTO student_groups (group_name) VALUES (%s);", (group_name,))
        return self.cursor.lastrowid

    def find_group_id(self, group_name: str) -> int:
        self.cursor.execute("SELECT group_id FROM student_groups WHERE group_name=%s;", (group_name,))
        return self.cursor.fetchone()[0]

    def find_group_names(self, group_ids: list[int]) -> dict[int, str]:
        if len(group_ids) == 0:
            return {}
        self.cursor.execute("SELECT group_id, group_name FROM student_groups WHERE group_id IN (%s);" % ", ".join(["%s"] * len(group_ids)), group_ids)
        groups = {}
        for item in self.cursor.fetchall():
            group_id: int = item[0]
            group_name: str = item[1]
            groups[group_id] = group_name
        return groups

    def get_all_group_names(self):
        self.cursor.execute("SELECT group_name FROM student_groups;")
        groups = [ i[0] for i in self.cursor.fetchall()]
        # print(groups)
        return groups

class GroupLessonsTable(BaseTable):
    def __init__(self, cursor):
        super().__init__(cursor)
        self._create_table()

    def _create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS group_lessons ("
                            "group_id INT NOT NULL,"
                            "lesson_id INT NOT NULL, "
                            "PRIMARY KEY (group_id, lesson_id),"
                            "FOREIGN KEY (group_id) REFERENCES student_groups(group_id),"
                            "FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id)"
                            ");")

    def add_group_lesson(self, group_id: int, lesson_id: int):
        self.cursor.execute("INSERT INTO group_lessons (group_id, lesson_id) VALUES (%s, %s);", (group_id, lesson_id))

    def find_group_lessons_ids(self, group_id: int) -> list[int]:
        self.cursor.execute("SELECT lesson_id FROM group_lessons WHERE group_id=%s;", (group_id,))
        lesson_ids = []
        for i in self.cursor:
            lesson_ids.append(i[0])
        return lesson_ids

    def find_groups_by_lessons_ids(self, lesson_ids: list[int]) -> dict[int, list[int]]:
        if (lesson_ids is None) or (len(lesson_ids) == 0):
            return {}
        self.cursor.execute("SELECT group_id, lesson_id FROM group_lessons WHERE lesson_id IN (%s);" % ", ".join(["%s"] * len(lesson_ids)), lesson_ids)
        groups = {}
        for item in self.cursor.fetchall():
            group_id: int = item[0]
            lesson_id: int = item[1]
            if lesson_id not in groups.keys():
                groups[lesson_id] = []
            groups[lesson_id].append(group_id)
        return groups

class SubjectsTable(BaseTable):
    def __init__(self, cursor):
        super().__init__(cursor)
        self._create_table()

    def _create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS subjects ("
                            "subject_short_name VARCHAR(255) PRIMARY KEY,"
                            "subject_name VARCHAR(255) NOT NULL );")

    def add_subject(self, subject_short_name: str, subject_name: str):
        self.cursor.execute("INSERT INTO subjects (subject_short_name, subject_name) VALUES (%s, %s);",
                            (subject_short_name, subject_name))

    def find_subject_name(self, subject_short_name: str) -> str:
        self.cursor.execute("SELECT subject_name FROM subjects WHERE subject_short_name=%s;", (subject_short_name,))
        return self.cursor.fetchone()[0]

    def find_subject_names(self, subject_short_names: list[str]) -> dict[str, str]:
        if (subject_short_names is None) or (len(subject_short_names) == 0):
            return {}
        self.cursor.execute("SELECT subject_short_name, subject_name FROM subjects WHERE subject_short_name IN (%s);" % ", ".join(["%s"] * len(subject_short_names)), subject_short_names)
        subjects = {}
        for item in self.cursor.fetchall():
            subject_short_name: str = item[0]
            subject_name: str = item[1]
            subjects[subject_short_name] = subject_name
        return subjects

class ClassroomsTable(BaseTable):
    def __init__(self, cursor):
        super().__init__(cursor)
        self._create_table()

    def _create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS classrooms ("
                            "classroom_id INT AUTO_INCREMENT PRIMARY KEY,"
                            "classroom_name VARCHAR(255) NOT NULL );")

    def add_classroom(self, classroom_name: str) -> int:
        self.cursor.execute("INSERT INTO classrooms (classroom_name) VALUES (%s);",
                            (classroom_name, ))
        return self.cursor.lastrowid

    def find_classroom_id(self, classroom_name: str) -> int:
        self.cursor.execute("SELECT classroom_id FROM classrooms WHERE classroom_name=%s;", (classroom_name,))
        return self.cursor.fetchone()[0]

    def find_classroom_name(self, classroom_id: int) -> str:
        self.cursor.execute("SELECT classroom_name FROM classrooms WHERE classroom_id=%s;", (classroom_id,))
        return self.cursor.fetchone()[0]

    def find_classroom_names(self, classroom_ids: list[int]) -> dict[int, str]:
        if (classroom_ids is None) or (len(classroom_ids) == 0):
            return {}
        self.cursor.execute("SELECT classroom_id, classroom_name FROM classrooms WHERE classroom_id IN (%s);" % ", ".join(["%s"] * len(classroom_ids)), classroom_ids)
        classrooms = {}
        for item in self.cursor.fetchall():
            classroom_id: int = item[0]
            classroom_name: str = item[1]
            classrooms[classroom_id] = classroom_name
        return classrooms

class TeachersTable(BaseTable):
    def __init__(self, cursor):
        super().__init__(cursor)
        self._create_table()

    def _create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS teachers ("
                            "teacher_initials VARCHAR(255) PRIMARY KEY,"
                            "teacher_name VARCHAR(255) NOT NULL );")

    def add_teacher(self, teacher_initials: str, teacher_name: str):
        self.cursor.execute("INSERT INTO teachers (teacher_initials, teacher_name) VALUES (%s, %s);",
                            (teacher_initials, teacher_name))

    def find_teacher_name(self, teacher_initials: str) -> str:
        self.cursor.execute("SELECT teacher_name FROM teachers WHERE teacher_initials=%s;", (teacher_initials,))
        return self.cursor.fetchone()[0]

    def find_teacher_names(self, teacher_initials: list[str]) -> dict[str, str]:
        if (teacher_initials is None) or (len(teacher_initials) == 0):
            return {}
        self.cursor.execute("SELECT teacher_initials, teacher_name FROM teachers WHERE teacher_initials IN (%s);" % ", ".join(["%s"] * len(teacher_initials)), teacher_initials)
        teachers = {}
        for item in self.cursor.fetchall():
            teacher_initials: str = item[0]
            teacher_name: str = item[1]
            teachers[teacher_initials] = teacher_name
        return teachers

class SubgroupsTable(BaseTable):
    def __init__(self, cursor):
        super().__init__(cursor)
        self._create_table()

    def _create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS subgroups ("
                            "subgroup_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                            "group_id INT NOT NULL,"
                            "subgroup_name VARCHAR(255),"
                            "subgroup_display_name VARCHAR(255) NOT NULL,"
                            "FOREIGN KEY (group_id) REFERENCES student_groups(group_id) "
                            ");")

    def add_subgroup(self, group_id: int, subgroup_name: str, subgroup_display_name: str) -> int:
        self.cursor.execute("INSERT INTO subgroups (group_id, subgroup_name, subgroup_display_name) VALUES (%s, %s, %s);",
                            (group_id, subgroup_name, subgroup_display_name))
        return self.cursor.lastrowid

    def find_subgroup_names(self, subgroup_ids: list[int]) -> dict[int, dict[str, str]]:
        if (subgroup_ids is None) or (len(subgroup_ids) == 0):
            return {}
        self.cursor.execute("SELECT subgroup_id, subgroup_name, subgroup_display_name, group_id FROM subgroups WHERE subgroup_id IN (%s);" % ", ".join(["%s"] * len(subgroup_ids)), subgroup_ids)
        subgroups = {}
        for item in self.cursor.fetchall():
            subgroup_id: int = item[0]
            subgroup_name: str = item[1]
            subgroup_display_name: str = item[2]
            parent_group_id: int = item[3]
            subgroups[subgroup_id] = {'subgroup_name': subgroup_name, 'subgroup_display_name': subgroup_display_name, 'parent_group_id': parent_group_id}
        return subgroups

    def find_subgroup_info(self, subgroup_id: int) -> dict[str, str]:
        self.cursor.execute("SELECT group_id, subgroup_name, subgroup_display_name FROM subgroups WHERE subgroup_id=%s;", (subgroup_id,))
        subgroup_info = self.cursor.fetchone()
        if subgroup_info is None:
            return {}
        group_id: int = subgroup_info[0]
        subgroup_name: str = subgroup_info[1]
        subgroup_display_name: str = subgroup_info[2]
        return {'group_id': group_id, 'subgroup_name': subgroup_name, 'subgroup_display_name': subgroup_display_name}

    def find_subgroup_info_by_name_and_parent(self, subgroup_name: str, group_id: int) -> dict:
        self.cursor.execute("SELECT subgroup_id, group_id, subgroup_name, subgroup_display_name FROM subgroups WHERE subgroup_name=%s AND group_id=%s;", (subgroup_name, group_id))
        subgroup_info = self.cursor.fetchone()
        if subgroup_info is None:
            return {}
        subgroup_id: int = subgroup_info[0]
        group_id: int = subgroup_info[1]
        subgroup_name: str = subgroup_info[2]
        subgroup_display_name: str = subgroup_info[3]
        return {'subgroup_id': subgroup_id, 'group_id': group_id, 'subgroup_name': subgroup_name,
                'subgroup_display_name': subgroup_display_name}

    def find_subgroup_info_by_parent(self, group_id: int) -> list[dict]:
        self.cursor.execute("SELECT subgroup_id, group_id, subgroup_name, subgroup_display_name FROM subgroups WHERE group_id=%s;", (group_id,))
        subgroup_infos = []
        for i in self.cursor:
            subgroup_id: int = i[0]
            group_id: int = i[1]
            subgroup_name: str = i[2]
            subgroup_display_name: str = i[3]
            subgroup_infos.append({'subgroup_id': subgroup_id, 'group_id': group_id, 'subgroup_name': subgroup_name, 'subgroup_display_name': subgroup_display_name})
        return subgroup_infos

    def find_child_subgroups(self, group_id: int) -> list[int]:
        self.cursor.execute("SELECT subgroup_id FROM subgroups WHERE group_id=%s;", (group_id,))
        child_subgroup_ids = []
        for i in self.cursor:
            child_subgroup_ids.append(i[0])
        return child_subgroup_ids

    def get_all_subgroups(self):
        self.cursor.execute("SELECT subgroup_id, group_id, subgroup_name, subgroup_display_name FROM subgroups;")
        subgroup_info = []
        for i in self.cursor:
            subgroup_id: int = i[0]
            group_id: int = i[1]
            subgroup_name: str = i[2]
            subgroup_display_name: str = i[3]
            subgroup_info.append({'subgroup_id': subgroup_id, 'group_id': group_id, 'subgroup_name': subgroup_name,
                                   'subgroup_display_name': subgroup_display_name})
        return subgroup_info

class SubgroupLessonsTable(BaseTable):
    def __init__(self, cursor):
        super().__init__(cursor)
        self._create_table()

    def _create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS subgroup_lessons ("
                            "subgroup_id INT NOT NULL,"
                            "lesson_id INT NOT NULL, "
                            "PRIMARY KEY (subgroup_id, lesson_id),"
                            "FOREIGN KEY (subgroup_id) REFERENCES subgroups(subgroup_id),"
                            "FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id)"
                            ");")

    def add_subgroup_lesson(self, subgroup_id: int, lesson_id: int):
        self.cursor.execute("INSERT INTO subgroup_lessons (subgroup_id, lesson_id) VALUES (%s, %s);", (subgroup_id, lesson_id))

    def find_subgroup_lessons_ids(self, subgroup_id: int) -> list[int]:
        self.cursor.execute("SELECT lesson_id FROM subgroup_lessons WHERE subgroup_id=%s;", (subgroup_id,))
        lesson_ids = []
        for i in self.cursor:
            lesson_ids.append(i[0])
        return lesson_ids

    def find_subgroups_lessons_ids(self, subgroup_ids: list[int]) -> list[int]:
        if (subgroup_ids is None) or (len(subgroup_ids) == 0):
            return []
        self.cursor.execute("SELECT subgroup_id, lesson_id FROM subgroup_lessons WHERE subgroup_id IN (%s);" % ", ".join(["%s"] * len(subgroup_ids)), subgroup_ids)
        subgroup_lessons_ids = []
        for i in self.cursor:
            lesson_id: int = i[1]
            subgroup_lessons_ids.append(lesson_id)
        return subgroup_lessons_ids

    def find_subgroups_by_lessons_ids(self, lesson_ids: list[int]) -> dict[int, list[int]]:
        if (lesson_ids is None) or (len(lesson_ids) == 0):
            return {}
        self.cursor.execute("SELECT subgroup_id, lesson_id FROM subgroup_lessons WHERE lesson_id IN (%s);" % ", ".join(["%s"] * len(lesson_ids)), lesson_ids)
        subgroups = {}
        for item in self.cursor.fetchall():
            subgroup_id: int = item[0]
            lesson_id: int = item[1]
            if lesson_id not in subgroups.keys():
                subgroups[lesson_id] = []
            subgroups[lesson_id].append(subgroup_id)
        return subgroups

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