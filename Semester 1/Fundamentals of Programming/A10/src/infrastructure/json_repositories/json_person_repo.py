import json
from json import JSONDecodeError

from domain.entities.person import Person
from infrastructure.repositories.person_repo import PersonRepository


class JSONPersonRepository(PersonRepository):
    def __init__(self, txt):
        super().__init__()
        self.__txt = txt
        self.__read_from_json()

    def __read_from_json(self):
        with open(self.__txt, "r") as f:
            data = json.load(f)
            for key in data.keys():
                super().store(Person(int(key), data[key][0], data[key][1]))

    def __write_to_json(self):
        with open(self.__txt, "w") as f:
            json.dump(PersonRepository.to_dict(self), f)

    def store(self, person):
        super().store(person)
        self.__write_to_json()

    def update(self, person):
        super().update(person)
        self.__write_to_json()

    def delete(self, p_id):
        super().delete(p_id)
        self.__write_to_json()
