from database.base_table import BaseTable


class SubgroupsTable(BaseTable):
    def __init__(self, cursor):
        super().__init__(cursor)
        self._create_table()

    def _create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS subgroups ("
                            "subgroup_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                            "group_id INT NOT NULL,"
                            "subgroup_name VARCHAR(255),"
                            "subgroup_display_name VARCHAR(255) NOT NULL,"
                            "FOREIGN KEY (group_id) REFERENCES student_groups(group_id) "
                            ");")

    def add_subgroup(self, group_id: int, subgroup_name: str, subgroup_display_name: str) -> int:
        self.cursor.execute("INSERT INTO subgroups (group_id, subgroup_name, subgroup_display_name) VALUES (%s, %s, %s);",
                            (group_id, subgroup_name, subgroup_display_name))
        return self.cursor.lastrowid

    def find_subgroup_names(self, subgroup_ids: list[int]) -> dict[int, dict[str, str]]:
        if (subgroup_ids is None) or (len(subgroup_ids) == 0):
            return {}
        self.cursor.execute("SELECT subgroup_id, subgroup_name, subgroup_display_name, group_id FROM subgroups WHERE subgroup_id IN (%s);" % ", ".join(["%s"] * len(subgroup_ids)), subgroup_ids)
        subgroups = {}
        for item in self.cursor.fetchall():
            subgroup_id: int = item[0]
            subgroup_name: str = item[1]
            subgroup_display_name: str = item[2]
            parent_group_id: int = item[3]
            subgroups[subgroup_id] = {'subgroup_name': subgroup_name, 'subgroup_display_name': subgroup_display_name, 'parent_group_id': parent_group_id}
        return subgroups

    def find_subgroup_info(self, subgroup_id: int) -> dict[str, str]:
        self.cursor.execute("SELECT group_id, subgroup_name, subgroup_display_name FROM subgroups WHERE subgroup_id=%s;", (subgroup_id,))
        subgroup_info = self.cursor.fetchone()
        if subgroup_info is None:
            return {}
        group_id: int = subgroup_info[0]
        subgroup_name: str = subgroup_info[1]
        subgroup_display_name: str = subgroup_info[2]
        return {'group_id': group_id, 'subgroup_name': subgroup_name, 'subgroup_display_name': subgroup_display_name}

    def find_subgroup_info_by_name_and_parent(self, subgroup_name: str, group_id: int) -> dict:
        self.cursor.execute("SELECT subgroup_id, group_id, subgroup_name, subgroup_display_name FROM subgroups WHERE subgroup_name=%s AND group_id=%s;", (subgroup_name, group_id))
        subgroup_info = self.cursor.fetchone()
        if subgroup_info is None:
            return {}
        subgroup_id: int = subgroup_info[0]
        group_id: int = subgroup_info[1]
        subgroup_name: str = subgroup_info[2]
        subgroup_display_name: str = subgroup_info[3]
        return {'subgroup_id': subgroup_id, 'group_id': group_id, 'subgroup_name': subgroup_name,
                'subgroup_display_name': subgroup_display_name}

    def find_subgroup_info_by_parent(self, group_id: int) -> list[dict]:
        self.cursor.execute("SELECT subgroup_id, group_id, subgroup_name, subgroup_display_name FROM subgroups WHERE group_id=%s;", (group_id,))
        subgroup_infos = []
        for i in self.cursor:
            subgroup_id: int = i[0]
            group_id: int = i[1]
            subgroup_name: str = i[2]
            subgroup_display_name: str = i[3]
            subgroup_infos.append({'subgroup_id': subgroup_id, 'group_id': group_id, 'subgroup_name': subgroup_name, 'subgroup_display_name': subgroup_display_name})
        return subgroup_infos

    def find_child_subgroups(self, group_id: int) -> list[int]:
        self.cursor.execute("SELECT subgroup_id FROM subgroups WHERE group_id=%s;", (group_id,))
        child_subgroup_ids = []
        for i in self.cursor:
            child_subgroup_ids.append(i[0])
        return child_subgroup_ids

    def get_all_subgroups(self):
        self.cursor.execute("SELECT subgroup_id, group_id, subgroup_name, subgroup_display_name FROM subgroups;")
        subgroup_info = []
        for i in self.cursor:
            subgroup_id: int = i[0]
            group_id: int = i[1]
            subgroup_name: str = i[2]
            subgroup_display_name: str = i[3]
            subgroup_info.append({'subgroup_id': subgroup_id, 'group_id': group_id, 'subgroup_name': subgroup_name,
                                   'subgroup_display_name': subgroup_display_name})
        return subgroup_info

