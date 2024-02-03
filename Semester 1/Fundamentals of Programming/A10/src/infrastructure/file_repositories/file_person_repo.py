from infrastructure.data_access_entities import PersonDataAccess
from infrastructure.repositories.person_repo import PersonRepository


class FilePersonRepository(PersonRepository):
    def __init__(self, txt):
        super().__init__()
        self.__txt = txt
        self.__read_from_file()

    def __read_from_file(self):
        with open(self.__txt, "r") as f:
            for line in f:
                person = PersonDataAccess.read_from(line)
                if person is not None:
                    super().store(person)

    def __append_to_file(self, person):
        with open(self.__txt, "a") as f:
            PersonDataAccess.write_to(f, person)

    def __write_to_file(self):
        with open(self.__txt, "w") as f:
            f.truncate(0)
        for p in super().get_people():
            self.__append_to_file(p)

    def store(self, person):
        super().store(person)
        self.__append_to_file(person)

    def update(self, person):
        super().update(person)
        self.__write_to_file()

    def delete(self, p_id):
        super().delete(p_id)
        self.__write_to_file()
