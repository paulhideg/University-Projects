from abc import ABC, abstractmethod

from domain.entities.activity import Activity
from domain.entities.person import Person
from domain.useful_stuff.date import Date
from domain.useful_stuff.time import Time


class DataAccessEntities(ABC):
    @staticmethod
    @abstractmethod
    def read_from(line):
        pass

    @staticmethod
    @abstractmethod
    def write_to(f, entity):
        pass


class PersonDataAccess(Person, DataAccessEntities):
    @staticmethod
    def read_from(line):
        line = line.strip()
        if line != "":
            parts = line.split(";")
            return Person(int(parts[0]), parts[1], parts[2])

    @staticmethod
    def write_to(f, person):
        f.write(str(person.person_id) + ';' + person.name + ';' + person.phone_number + '\n')


class ActivityDataAccess(Activity, DataAccessEntities):
    @staticmethod
    def read_from(line):
        line = line.strip()
        if line != "":
            parts = line.split(";")
            str_people_ids = parts[1]
            parts_ids = str_people_ids.split(',')
            people_ids = []
            for part in parts_ids:
                people_ids.append(int(part))
            parts_date = parts[2].split('.')
            date = Date(int(parts_date[0]), int(parts_date[1]), int(parts_date[2]))
            parts_time = parts[3].split('-')
            parts_start = parts_time[0].strip().split(':')
            parts_end = parts_time[1].strip().split(':')
            time = Time(int(parts_start[0]), int(parts_start[1]), int(parts_end[0]), int(parts_end[1]))
            return Activity(int(parts[0]), people_ids, date, time, parts[4])

    @staticmethod
    def write_to(f, activity):
        str_ids = str(activity.person_id[0])
        for i in range(1, len(activity.person_id)):
            str_ids += ',' + str(activity.person_id[i])
        f.write(str(activity.activity_id) + ';' + str_ids + ';' + str(activity.date) + ';' + str(
            activity.time) + ';' + activity.description + '\n')
