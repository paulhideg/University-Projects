import json
from json import JSONDecodeError

from domain.entities.activity import Activity
from domain.useful_stuff.date import Date
from domain.useful_stuff.time import Time
from infrastructure.repositories.activity_repo import ActivityRepository


class JSONActivityRepository(ActivityRepository):
    def __init__(self, txt):
        super().__init__()
        self.__txt = txt
        self.__read_from_json()

    def __read_from_json(self):
        with open(self.__txt, "r") as f:
            data = json.load(f)
            for key in data.keys():
                people_ids = []
                for i in data[key][0]:
                    people_ids.append(int(i))
                date = Date(int(data[key][1][0]), int(data[key][1][1]), int(data[key][1][2]))
                time = Time(int(data[key][2][0]), int(data[key][2][1]), int(data[key][2][2]), int(data[key][2][3]))
                super().store(Activity(int(key), people_ids, date, time, data[key][3]))

    def __write_to_json(self):
        with open(self.__txt, "w") as f:
            json.dump(ActivityRepository.to_dict(self), f)

    def store(self, activity):
        super().store(activity)
        self.__write_to_json()

    def update(self, activity):
        super().update(activity)
        self.__write_to_json()

    def delete(self, a_id):
        super().delete(a_id)
        self.__write_to_json()
