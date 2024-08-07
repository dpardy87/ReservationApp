# pylint: skip-file
import os
import urllib


class Config:
    def __init__(self):
        self.PGSQL_DB_NAME = "reservation_system"
        self.PGSQL_USER = "dp"
        self.PGSQL_PW = "password"
        self.PGSQL_HOST = "localhost"
        self.PGSQL_PORT = "5432"
        self.PGSQL_CONN_STR = f"postgresql://{self.PGSQL_USER}:{self.PGSQL_PW}@{self.PGSQL_HOST}:{self.PGSQL_PORT}/{self.PGSQL_DB_NAME}"

    def serialize(self):
        return self.__dict__

class DevelopmentConfig(Config):
    def __init__(self):
        super().__init__()
        self.DEBUG = True

    