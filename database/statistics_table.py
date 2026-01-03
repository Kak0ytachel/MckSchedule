from mysql.connector.cursor import MySQLCursor
from datetime import datetime, timedelta

from database.base_table import BaseTable


class StatisticsTable(BaseTable):
    bufer = []

    def __init__(self, cursor: MySQLCursor):
        super().__init__(cursor)
        self._create_table()

    def _create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS statistics ("
                            "item_type VARCHAR(255) NOT NULL,"
                            "item_id BIGINT,"
                            "item_name VARCHAR(255),"
                            "datetime DATETIME NOT NULL,"
                            "CONSTRAINT stats_types CHECK (item_type IN ('classroom', 'teacher', 'group', 'subgroup'))"
                            ");")

    def count(self, after: datetime, before: datetime, item_type: str, item_id: int = None, item_name: str = None) -> int:
        if (item_id is None) and (item_name is None):
            raise ValueError("Either item_id or item_name must be specified.")

        if item_id is not None:
            self.cursor.execute("SELECT COUNT(*) FROM statistics WHERE datetime BETWEEN %s AND %s AND item_type=%s AND item_id=%s;", (after, before, item_type, item_id))
            return self.cursor.fetchone()[0]

        if item_name is not None:
            self.cursor.execute("SELECT COUNT(*) FROM statistics WHERE datetime BETWEEN %s AND %s AND item_type=%s AND item_name=%s;", (after, before, item_type, item_name))
            return self.cursor.fetchone()[0]

    def count_all_time(self, item_type: str, item_id: int = None, item_name: str = None):
        return self.count(datetime(1970, 1, 1), datetime.now(), item_type, item_id, item_name)

    def insert(self, item_type: str, item_id: int = None, item_name: str = None):
        if (item_id is None) and (item_name is None):
            raise ValueError("Either item_id or item_name must be specified.")
        if item_type not in ['classroom', 'teacher', 'group', 'subgroup']:
            raise ValueError("Invalid item_type.")
        if item_id is not None and item_name is not None:
            raise ValueError("Only one of item_id or item_name must be specified.")
        if item_type in ['teacher'] and item_name is None:
            raise ValueError("item_name must be specified for item_type='teacher'.")
        if item_type in ['group', 'subgroup', 'classroom'] and item_id is None:
            raise ValueError("item_id must be specified for item_type='group', 'subgroup' or 'classroom'.")

        def check_bufer() -> bool:
            # true if okay and should be recorded
            # false if already recorded
            now = datetime.now()
            self.bufer = [x for x in self.bufer if x["datetime"] > now - timedelta(seconds=60)]
            for x in self.bufer:
                if x["item_type"] == item_type and x["item_id"] == item_id and x["item_name"] == item_name:
                    print("skipped duplicate request")
                    return False
            self.bufer.append({"item_type": item_type, "item_id": item_id, "item_name": item_name, "datetime": datetime.now()})
            return True


        if not check_bufer():
            return

        if item_type in ['teacher']:
            self.cursor.execute("INSERT INTO statistics (item_type, item_name, datetime) VALUES (%s, %s, NOW());", (item_type, item_name))

        if item_type in ['group', 'subgroup', 'classroom']:
            self.cursor.execute("INSERT INTO statistics (item_type, item_id, datetime) VALUES (%s, %s, NOW());", (item_type, item_id))

    def count_all_elements(self, before: datetime, after: datetime) -> list[dict]:
        self.cursor.execute("SELECT item_type, item_name, item_id, COUNT(*) as count FROM statistics GROUP BY item_type, item_name, item_id ORDER BY count DESC;")
        items = []
        for i in self.cursor.fetchall():
            item = {"item_type": i[0], "item_name": i[1], "item_id": i[2], "count": i[3]}
            items.append(item)
        return items