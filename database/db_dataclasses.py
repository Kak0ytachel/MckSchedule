import datetime

from database.db import Database

db: Database = None

def init_db(db_: Database):
    global db
    db = db_


class Subject:
    subject_short_name: str
    subject_name: str

    def __init__(self, subject_short_name: str, subject_name: str):
        self.subject_short_name = subject_short_name
        self.subject_name = subject_name

        existing_name = db.subjects_table.find_subject_name(subject_short_name)
        if existing_name is None:
            db.subjects_table.add_subject(subject_short_name, subject_name)
        elif existing_name != subject_name:
            print(f"Error: Subject {subject_short_name} already exists with different name: {existing_name}.")
            self.subject_name = existing_name

    def __str__(self):
        return self.subject_short_name


class Classroom:
    classroom_id: int
    classroom_short_name: str
    classroom_display_name: str

    def __init__(self, classroom_short_name: str, classroom_display_name: str):
        self.classroom_short_name = classroom_short_name
        self.classroom_display_name = classroom_display_name

        result = db.classrooms_table.get_classroom_data_by_short_name(classroom_short_name)
        if result is None:
            self.classroom_id = db.classrooms_table.add_classroom(classroom_short_name, classroom_display_name)
        else:
            self.classroom_id = result['classroom_id']
            if result['classroom_display_name'] != classroom_display_name:
                print(f"Error: Classroom {classroom_short_name} already exists with different name: {result['classroom_display_name']}.")
            self.classroom_display_name = result['classroom_display_name']

    def __int__(self):
        return self.classroom_id


class Group:
    group_name: str
    group_id: int

    def __init__(self, group_name: str):
        self.group_name = group_name

        result_id = db.groups_table.find_group_id(group_name)
        if result_id is not None:
            self.group_id = result_id
        else:
            self.group_id = db.groups_table.add_group(group_name)

    def __int__(self):
        return self.group_id

    def make_subgroup(self, subgroup_name, subgroup_display_name):
        return Subgroup(subgroup_name, subgroup_display_name, self.group_id)


class Subgroup:
    subgroup_name: str
    subgroup_display_name: str
    subgroup_id: int
    group_id: int

    def __init__(self, subgroup_name: str, subgroup_display_name: str, group: Group | int):
        group_id: int
        if isinstance(group, int):
            group_id = group
        else:
            group_id = group.group_id

        self.subgroup_name = subgroup_name
        self.subgroup_display_name = subgroup_display_name
        self.group_id = group_id

        result = db.subgroups_table.find_subgroup_info_by_name_and_parent(subgroup_name, group_id)
        if result is None:
            self.subgroup_id = db.subgroups_table.add_subgroup(group_id, subgroup_name, subgroup_display_name)
            return
        if result['subgroup_display_name'] != subgroup_display_name:
            print(f"Error: Subgroup {subgroup_name} already exists with different display name: {result['subgroup_display_name']}.")
            self.subgroup_display_name = result['subgroup_display_name']
        self.subgroup_id = result['subgroup_id']

    def __int__(self):
        return self.subgroup_id


class Teacher:
    teacher_initials: str
    teacher_name: str

    def __init__(self, teacher_initials: str, teacher_name: str):
        self.teacher_initials = teacher_initials
        self.teacher_name = teacher_name

        result_name = db.teachers_table.find_teacher_name(teacher_initials)
        if result_name is None:
            db.teachers_table.add_teacher(teacher_initials, teacher_name)
        elif result_name != teacher_name:
            print(f"Error: Teacher {teacher_initials} already exists with different name: {result_name}.")
            self.teacher_name = result_name

    def __str__(self):
        return self.teacher_initials


class Semester:
    semester_id: int
    semester_name: str
    start_date: datetime.date
    end_date: datetime.date
    translation_name: str

    def __init__(self, name, start_date, end_date, translation_name):
        self.semester_name = name
        self.start_date = start_date
        self.end_date = end_date
        self.translation_name = translation_name

        result = db.semesters_table.get_semester_by_dates(start_date, end_date)
        if result is None:
            self.semester_id = db.semesters_table.add_semester(name, start_date, end_date, translation_name)
            return

        if result["semester_name"] != self.semester_name or result["translation_name"] != self.translation_name:
            print(f"Error: Semester {start_date} - {end_date} already exists with different name: "
                  f"{result['semester_name']} ({result['translation_name']}).")
            self.semester_name = result["semester_name"]
            self.translation_name = result["translation_name"]
        self.semester_id = result["semester_id"]

    def __int__(self):
        return self.semester_id


class Lesson:
    lesson_id: int
    subject: Subject
    classroom: Classroom
    teacher: Teacher
    weekday: int
    start_hour: int
    start_minute: int
    end_hour: int
    end_minute: int
    semester: Semester

    def __init__(self, subject: Subject, classroom: Classroom, teacher: Teacher, weekday: int, start_hour: int,
                 start_minute: int, end_hour: int, end_minute: int, semester: Semester):
        self.subject = subject
        self.classroom = classroom
        self.teacher = teacher
        self.weekday = weekday
        self.start_hour = start_hour
        self.start_minute = start_minute
        self.end_hour = end_hour
        self.end_minute = end_minute
        self.semester = semester

        self.lesson_id = db.lessons_table.add_lesson(
            subject.subject_short_name, classroom.classroom_id, teacher.teacher_initials, weekday, start_hour,
            start_minute, end_hour, end_minute, semester.semester_id)

    def add_group(self, group: Group):
        db.group_lessons_table.add_group_lesson(group_id=group.group_id, lesson_id=self.lesson_id)
        return self

    def add_subgroup(self, subgroup: Subgroup):
        db.subgroup_lessons_table.add_subgroup_lesson(subgroup_id=subgroup.subgroup_id, lesson_id=self.lesson_id)
        return self

    def add_subgroups(self, *subgroups: Subgroup):
        for subgroup in subgroups:
            self.add_subgroup(subgroup)
