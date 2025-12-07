from database.base_table import BaseTable


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

