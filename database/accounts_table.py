import typing

from database.base_table import BaseTable
from mysql.connector.cursor import MySQLCursor

from security import encode_password


class AccountData(typing.TypedDict):
    user_id: int
    username: str
    hashed_password: str
    is_admin: bool
    display_name: str
    email: str

class AccountsTable(BaseTable):
    def __init__(self, cursor: MySQLCursor):
        super().__init__(cursor)
        self._create_table()
        self.add_account_ignore('admin', encode_password('admin'), True, 'Admin', '')

    def _create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS accounts ("
                            "user_id INT AUTO_INCREMENT PRIMARY KEY,"
                            "username VARCHAR(255) NOT NULL UNIQUE,"
                            "hashed_password VARCHAR(255) NOT NULL,"
                            "is_admin BOOLEAN NOT NULL DEFAULT FALSE,"
                            "display_name VARCHAR(255) NOT NULL,"
                            "email VARCHAR(255) NOT NULL UNIQUE);")


    def add_account(self, username: str, hashed_password: str, is_admin: bool, display_name: str, email: str) -> int:
        self.cursor.execute("INSERT INTO accounts (username, hashed_password, is_admin, display_name, email) VALUES (%s, %s, %s, %s, %s);",
                            (username, hashed_password, is_admin, display_name, email))
        return self.cursor.lastrowid

    def find_account(self, login: str) -> list[AccountData]:
        self.cursor.execute("SELECT user_id, username, hashed_password, is_admin, display_name, email FROM accounts WHERE username=%s OR email=%s;", (login, login))
        items = self.cursor.fetchall()
        accounts = []
        for item in items:
            accounts.append({'user_id': item[0], 'username': item[1], 'hashed_password': item[2],
                             'is_admin': item[3], 'display_name': item[4], 'email': item[5]})
        return accounts

    def check_email_available(self, email: str) -> bool:
        self.cursor.execute("SELECT email FROM accounts WHERE email=%s;", (email,))
        return self.cursor.fetchone() is None

    def check_username_available(self, username: str) -> bool:
        self.cursor.execute("SELECT username FROM accounts WHERE username=%s;", (username,))
        return self.cursor.fetchone() is None

    def add_account_ignore(self, username: str, hashed_password: str, is_admin: bool, display_name: str, email: str) -> int:
        self.cursor.execute("INSERT IGNORE INTO accounts (username, hashed_password, is_admin, display_name, email) VALUES (%s, %s, %s, %s, %s);",
                            (username, hashed_password, is_admin, display_name, email))
        return self.cursor.lastrowid