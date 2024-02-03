from configparser import ConfigParser

from repositories.repositories import RepoStudents, RepoDisciplines, RepoGrades
from repositories.file_repositories import FileRepoStudents, FileRepoDisciplines, FileRepoGrades
from repositories.binary_repositories import BinaryRepoStudents, BinaryRepoDisciplines, BinaryRepoGrades
from ui.ui import UI
from ui.gui import StudentsGUI


class Settings:
    def __init__(self, txt):
        self.__txt = txt
        self.__repository = ''
        self.__students_file = ''
        self.__disciplines_file = ''
        self.__grades_file = ''
        self.__ui = 'ui'
        self.__read_properties_file()

    def __read_properties_file(self):
        config = ConfigParser()
        config.read(self.__txt)
        self.__repository = config.get("settings", "repository")
        self.__students_file = config.get("settings", "students")
        self.__disciplines_file = config.get("settings", "disciplines")
        self.__grades_file = config.get("settings", "grades")
        self.__ui = config.get("settings", "ui")

    @property
    def repository(self):
        return self.__repository

    @property
    def students_file(self):
        return self.__students_file

    @property
    def disciplines_file(self):
        return self.__disciplines_file

    @property
    def grades_file(self):
        return self.__grades_file

    @property
    def ui(self):
        return self.__ui
