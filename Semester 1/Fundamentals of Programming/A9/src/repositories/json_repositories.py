import json
from json import JSONDecodeError

from domain.student import Student
from domain.discipline import Discipline
from domain.grade import Grade
from repositories.repositories import RepoStudents, RepoDisciplines, RepoGrades


class JSONRepoStudents(RepoStudents):
    def __init__(self, txt):
        super().__init__()
        self.__txt = txt
        self.__read_from_json()

    def __read_from_json(self):
        with open(self.__txt, "r") as f:
            try:
                data = json.load(f)
                for key in data.keys():
                    super().add_student(Student(int(key), data[key][0]))
            except JSONDecodeError:
                pass

    # def __write_to_json(self):
    #     with open(self.__txt, "w") as f:
    #         json.dump(RepoStudents.to_dict(self), f)
