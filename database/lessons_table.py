from database.base_table import BaseTable


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

    def get_all_lessons(self):
        self.cursor.execute("SELECT * FROM lessons;")
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

    def find_lessons_by_classroom_id(self, classroom_id: int) -> list[dict]:
        self.cursor.execute("SELECT * FROM lessons WHERE classroom_id=%s;", (classroom_id,))
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
                      'end_minute': item[8],
                      }
            lessons.append(lesson)
        return lessons


