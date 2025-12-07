from database.base_table import BaseTable


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

