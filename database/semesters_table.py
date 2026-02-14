import datetime

from database.base_table import BaseTable

class SemesterData(dict):
    semester_id: int
    semester_name: str
    start_date: datetime.date
    end_date: datetime.date
    translation_name: str

class SemestersTable(BaseTable):
    def __init__(self, cursor):
        super().__init__(cursor)
        self._create_table()

    def _create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS semesters ("
                            "semester_id INT AUTO_INCREMENT PRIMARY KEY,"
                            "semester_name VARCHAR(255) NOT NULL,"
                            "start_date DATE NOT NULL,"
                            "end_date DATE NOT NULL,"
                            "translation_name VARCHAR(255) NOT NULL"
                            ");")

    def add_semester(self, semester_name: str, start_date: str, end_date: str, translation_name: str) -> int:
        self.cursor.execute("INSERT INTO semesters (semester_name, start_date, end_date, translation_name) VALUES (%s, %s, %s, %s);",
                            (semester_name, start_date, end_date, translation_name))
        return self.cursor.lastrowid

    def get_current_semester_id(self):
        self.cursor.execute("SELECT semester_id, start_date, end_date FROM semesters ORDER BY start_date, end_date DESC;")
        semesters: list = self.cursor.fetchall()
        current: tuple = None
        today = datetime.date.today()
        for i in semesters:
            start_date = i[1]
            end_date = i[2]
            if today < end_date:
                current = i
                break
        if current is None and semesters is not None and len(semesters) > 0:
            current = semesters[0]
        semester_id = current[0]
        return semester_id

    def get_semesters(self):
        self.cursor.execute("SELECT semester_id, semester_name, start_date, end_date, translation_name FROM semesters;")
        data = []
        for semester in self.cursor.fetchall():
            semester_id = semester[0]
            semester_name = semester[1]
            start_date = semester[2]
            end_date = semester[3]
            translation_name = semester[4]
            semester_data = {
                "semester_id": semester_id,
                "semester_name": semester_name,
                "start_date": start_date,
                "end_date": end_date,
                "translation_name": translation_name
            }
            data.append(semester_data)
        return data

    def get_semester_by_dates(self, start_date: datetime.date, end_date: datetime.date) -> SemesterData | None:
        self.cursor.execute("SELECT semester_id, semester_name, start_date, end_date, translation_name FROM "
                            "semesters WHERE start_date = %s AND end_date = %s;", (start_date, end_date))
        result = self.cursor.fetchone()
        if result is None:
            return None
        semester_id = result[0]
        semester_name = result[1]
        start_date = result[2]
        end_date = result[3]
        translation_name = result[4]
        return {"semester_id": semester_id, "semester_name": semester_name, "start_date": start_date,
                "end_date": end_date, "translation_name": translation_name}