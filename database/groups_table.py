from database.base_table import BaseTable


class GroupsTable(BaseTable):
    def __init__(self, cursor):
        super().__init__(cursor)
        self._create_table()

    def _create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS student_groups ("
                            "group_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                            "group_name VARCHAR(255)"
                            ");")

    def add_group(self, group_name: str) -> int:
        self.cursor.execute("INSERT INTO student_groups (group_name) VALUES (%s);", (group_name,))
        return self.cursor.lastrowid

    def find_group_id(self, group_name: str) -> int:
        self.cursor.execute("SELECT group_id FROM student_groups WHERE group_name=%s;", (group_name,))
        return self.cursor.fetchone()[0]

    def find_group_names(self, group_ids: list[int]) -> dict[int, str]:
        if len(group_ids) == 0:
            return {}
        self.cursor.execute("SELECT group_id, group_name FROM student_groups WHERE group_id IN (%s);" % ", ".join(["%s"] * len(group_ids)), group_ids)
        groups = {}
        for item in self.cursor.fetchall():
            group_id: int = item[0]
            group_name: str = item[1]
            groups[group_id] = group_name
        return groups

    def get_all_group_names(self):
        self.cursor.execute("SELECT group_name FROM student_groups;")
        groups = [ i[0] for i in self.cursor.fetchall()]
        # print(groups)
        return groups

    def get_all_groups(self) -> dict[int, str]:
        self.cursor.execute("SELECT * FROM student_groups;")
        groups = {}
        for item in self.cursor.fetchall():
            group_id: int = item[0]
            group_name: str = item[1]
            groups[group_id] = group_name
        return groups
