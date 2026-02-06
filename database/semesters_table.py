from database.base_table import BaseTable


class SemestersTable(BaseTable):
    def __init__(self, cursor):
        super().__init__(cursor)
        self._create_table()

    def _create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS semesters ("
                            "semester_id INT AUTO_INCREMENT PRIMARY KEY,"
                            "semester_name VARCHAR(255) NOT NULL,"
                            "start_date DATE NOT NULL,"
                            "end_date DATE NOT NULL"
                            ");")

    def add_semester(self, semester_name: str, start_date: str, end_date: str):
        self.cursor.execute("INSERT INTO semesters (semester_name, start_date, end_date) VALUES (%s, %s, %s);",
                            (semester_name, start_date, end_date))

