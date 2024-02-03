from infrastructure.data_access_entities import ActivityDataAccess
from infrastructure.repositories.activity_repo import ActivityRepository


class FileActivityRepository(ActivityRepository):
    def __init__(self, txt):
        super().__init__()
        self.__txt = txt
        self.__read_from_file()

    def __read_from_file(self):
        with open(self.__txt, "r") as f:
            for line in f:
                activity = ActivityDataAccess.read_from(line)
                if activity is not None:
                    super().store(activity)

    def __append_to_file(self, activity):
        with open(self.__txt, "a") as f:
            ActivityDataAccess.write_to(f, activity)

    def __write_to_file(self):
        with open(self.__txt, 'w') as f:
            f.write('')
        for activity in super().get_activities():
            self.__append_to_file(activity)

    def store(self, activity):
        super().store(activity)
        self.__append_to_file(activity)

    def update(self, activity):
        super().update(activity)
        self.__write_to_file()

    def delete(self, a_id):
        super().delete(a_id)
        self.__write_to_file()
