from database.base_table import BaseTable


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

    def get_all_teachers(self) -> dict[str, str]:
        self.cursor.execute("SELECT teacher_initials, teacher_name FROM teachers;")
        result = {}
        for item in self.cursor.fetchall():
            teacher_initials: str = item[0]
            teacher_name: str = item[1]
            result[teacher_initials] = teacher_name
        return result