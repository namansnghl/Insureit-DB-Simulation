import mysql.connector as rdb
from mysql.connector.errors import Error
from getpass import getpass
import sys



class Connection:
    database = "insurit"
    _host = None
    _port = None
    __username = None
    __pswd = None

    def __init__(self, hostname: str = None, port: str = None, username: str = None):
        default_hostname = "localhost"
        default_port = "3306"

        if not hostname:
            self._host = default_hostname
            print("Setting hostname to default {}".format(default_hostname))
        if not port:
            self._port = default_port
            print("Setting port number to default {}".format(default_port))
        if username:
            self.__set_username(username)

    def fetch_creds(self):
        print("Enter database Credentials...")
        if not self.__username:
            self.__username = self._get_username()
        self.__pswd = self._get_pass()

    def _get_pass(self) -> str:
        return getpass("Password: ")

    def _get_username(self) -> str:
        return input("Username: ")

    def __set_username(self, username: str) -> int:
        self.__username = username
        return 1

    def __read_pass(self) -> str:
        return self.__pswd

    def connect(self):
        try:
            conn = rdb.connect(user=self.__username, password=self.__read_pass(),
                               host=self._host, port=self._port, database=self.database)
        except (Exception, Error) as msg:
            print(str(msg), file=sys.stderr)
        else:
            print("Connection established...\n")
            return conn
        return 0