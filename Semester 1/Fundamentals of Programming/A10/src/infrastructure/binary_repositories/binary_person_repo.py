import pickle

from infrastructure.repositories.person_repo import PersonRepository


class BinaryPersonRepository(PersonRepository):
    def __init__(self, txt):
        super().__init__()
        self.__txt = txt
        self.__read_from_binary()

    def __read_from_binary(self):
        with open(self.__txt, "rb") as f:
            try:
                while True:
                    super().store(pickle.load(f))
            except EOFError:
                pass

    def __append_to_binary(self, person):
        with open(self.__txt, "ab") as f:
            pickle.dump(person, f)

    def __write_to_binary(self):
        with open(self.__txt, "wb") as f:
            f.truncate(0)
            for p in super().get_people():
                pickle.dump(p, f)

    def store(self, person):
        super().store(person)
        self.__append_to_binary(person)

    def update(self, person):
        super().update(person)
        self.__write_to_binary()

    def delete(self, p_id):
        super().delete(p_id)
        self.__write_to_binary()
