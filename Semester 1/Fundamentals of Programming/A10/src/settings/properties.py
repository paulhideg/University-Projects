from configparser import ConfigParser

from infrastructure.binary_repositories.binary_activity_repo import BinaryActivityRepository
from infrastructure.binary_repositories.binary_person_repo import BinaryPersonRepository
from infrastructure.file_repositories.file_activity_repo import FileActivityRepository
from infrastructure.file_repositories.file_person_repo import FilePersonRepository
from infrastructure.json_repositories.json_activity_repo import JSONActivityRepository
from infrastructure.json_repositories.json_person_repo import JSONPersonRepository
from infrastructure.repositories.activity_repo import ActivityRepository
from infrastructure.repositories.person_repo import PersonRepository
from ui.console import Console
from ui.gui import ActivityGUI


class Settings:

    def __init__(self, txt):
        self.__txt = txt
        self.__repository = 'inmemory'
        self.__person_file = ''
        self.__activity_file = ''
        self.__ui = 'ui'
        self.__read_properties_file()

    def __read_properties_file(self):
        config = ConfigParser()
        config.read(self.__txt)
        self.__repository = config.get("settings", "repository")
        self.__person_file = config.get("settings", "people")
        self.__activity_file = config.get("settings", "activities")
        self.__ui = config.get("settings", "ui")

    @property
    def repository(self):
        return self.__repository

    @property
    def person_file(self):
        return self.__person_file

    @property
    def activity_file(self):
        return self.__activity_file

    @property
    def ui(self):
        return self.__ui
