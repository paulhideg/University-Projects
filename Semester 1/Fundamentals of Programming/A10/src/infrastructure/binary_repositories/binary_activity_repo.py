import pickle

from infrastructure.repositories.activity_repo import ActivityRepository


class BinaryActivityRepository(ActivityRepository):
    def __init__(self, txt):
        super().__init__()
        self.__txt = txt
        self.__read_from_binary()

    def __read_from_binary(self):
        with open(self.__txt, "rb") as f:
            self.__activity_repo = []
            try:
                while True:
                    super().store(pickle.load(f))
            except EOFError:
                pass

    def __append_to_binary(self, activity):
        with open(self.__txt, "ab") as f:
            pickle.dump(activity, f)

    def __write_to_binary(self):
        with open(self.__txt, "wb") as f:
            f.truncate(0)
            for a in super().get_activities():
                self.__append_to_binary(a)

    def store(self, activity):
        super().store(activity)
        self.__write_to_binary()

    def update(self, activity):
        super().update(activity)
        self.__write_to_binary()

    def delete(self, a_id):
        super().delete(a_id)
        self.__write_to_binary()
