from database.base_table import BaseTable


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

