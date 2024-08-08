# pylint: skip-file
import os
import urllib


class Config:
    def __init__(self):
        self.PGSQL_CONN_STR = 'postgresql://barbro:blackmoor@192.168.96.2:5432/reservation_system'
    def serialize(self):
        return self.__dict__

class DevelopmentConfig(Config):
    def __init__(self):
        super().__init__()
        self.DEBUG = True

    