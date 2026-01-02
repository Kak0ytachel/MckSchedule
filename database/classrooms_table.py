from typing import TypedDict

from database.base_table import BaseTable

class ClassroomData(TypedDict):
    id: int
    short_name: str
    display_name: str

class ClassroomsTable(BaseTable):
    def __init__(self, cursor):
        super().__init__(cursor)
        self._create_table()

    def _create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS classrooms ("
                            "classroom_id INT AUTO_INCREMENT PRIMARY KEY,"
                            "classroom_short_name VARCHAR(255) NOT NULL,"
                            "classroom_display_name VARCHAR(255) NOT NULL, "
                            "UNIQUE (classroom_short_name));")

    def add_classroom(self, classroom_short_name, classroom_display_name: str) -> int:
        self.cursor.execute("INSERT INTO classrooms (classroom_short_name, classroom_display_name) VALUES (%s, %s);",
                            (classroom_short_name, classroom_display_name))
        return self.cursor.lastrowid

    def find_classroom_id_by_short_name(self, classroom_short_name: str) -> int:
        self.cursor.execute("SELECT classroom_id FROM classrooms WHERE classroom_short_name=%s;", (classroom_short_name,))
        return self.cursor.fetchone()[0]

    def find_classroom_id(self, classroom_display_name: str) -> int:
        self.cursor.execute("SELECT classroom_id FROM classrooms WHERE classroom_display_name=%s;", (classroom_display_name,))
        return self.cursor.fetchone()[0]

    def find_classroom_display_name(self, classroom_id: int) -> str:
        self.cursor.execute("SELECT classroom_display_name FROM classrooms WHERE classroom_id=%s;", (classroom_id,))
        return self.cursor.fetchone()[0]

    def find_classroom_display_names(self, classroom_ids: list[int]) -> dict[int, str]:
        if (classroom_ids is None) or (len(classroom_ids) == 0):
            return {}
        self.cursor.execute("SELECT classroom_id, classroom_display_name FROM classrooms WHERE classroom_id IN (%s);" % ", ".join(["%s"] * len(classroom_ids)), classroom_ids)
        classrooms = {}
        for item in self.cursor.fetchall():
            classroom_id: int = item[0]
            classroom_display_name: str = item[1]
            classrooms[classroom_id] = classroom_display_name
        return classrooms

    def get_classroom_names(self) -> dict[str, str]:
        """
        :return: Dictionary (classroom_short_name: classroom_display_name)
        """
        self.cursor.execute("SELECT classroom_short_name, classroom_display_name FROM classrooms;")
        result = {}
        for item in self.cursor.fetchall():
            classroom_short_name: str = item[0]
            classroom_display_name: str = item[1]
            result[classroom_short_name] = classroom_display_name
        return result

    def get_classroom_data(self) -> dict[int, ClassroomData]:
        self.cursor.execute("SELECT classroom_id, classroom_short_name, classroom_display_name FROM classrooms;")
        result = {}
        for item in self.cursor.fetchall():
            classroom_id: int = item[0]
            classroom_short_name: str = item[1]
            classroom_display_name: str = item[2]
            result[classroom_id] = {'id': classroom_id, 'short_name': classroom_short_name,
                                    'display_name': classroom_display_name}
        return result
