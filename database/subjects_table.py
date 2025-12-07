from database.base_table import BaseTable


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

