from mysql.connector.cursor import MySQLCursor


class BaseTable:
    def __init__(self, cursor: MySQLCursor):
        self.name = self.__class__.__name__
        self.cursor: MySQLCursor = cursor

    def _create_table(self):
        print(f"No method to create table {self.name}")

    def _drop_table(self):
        print(f"No method to drop table {self.name}")

