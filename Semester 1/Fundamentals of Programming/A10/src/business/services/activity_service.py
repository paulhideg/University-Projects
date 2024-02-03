from dataclasses import dataclass

from a10_modules.filtering import Filtering
from a10_modules.sorting import Sorting
from domain.entities.activity import Activity
from domain.entities.person import Person
from domain.useful_stuff.undoredo_operation import UndoComplexHandler
from errors.exceptions import ValidatorException
from domain.useful_stuff.date import Date
from validation.activity_validator import DateValidator


class ActivityService:
    """
    Service of activities
    """

    def __init__(self, a_repo, p_repo, a_validator):
        self.__a_repo = a_repo
        self.__p_repo = p_repo
        self.__a_validator = a_validator

    def get_activities_of_person_on_a_date(self, person, date):
        """
        Finds all the activities a person has on a date
        :param person: person object
        :param date: date object
        :return: list of activities
        """
        activities = self.__a_repo.get_activities()
        pers_activity = []
        for a in activities:
            if person.person_id in a.person_id and a.date == date:
                pers_activity.append(a)
        return pers_activity[:]

    def is_same_time(self, time1, time2):
        """
        Checks whether 2 given times are identical or intercalate (12:00 - 12:30 intercalates with 12:29 - 13:00)
        :param time1: a time object
        :param time2: a time object
        :return: True or False
        """
        if time1 == time2 or not (time1 < time2 or time1 > time2):
            return True
        return False

    def person_already_has_activity(self, person, date, time):
        """
        Checks whether a person has 2 activities at the same time (or at times that intercalate)
        :param person: person object
        :param date: date object
        :param time: time object
        :return: True or False
        """
        activities = self.get_activities_of_person_on_a_date(person, date)
        for a in activities:
            if self.is_same_time(a.time, time):
                return True
        return False

    def search(self, a_id):
        activities = self.__a_repo.get_activities()
        for a in activities:
            if a_id == a.activity_id:
                return a
        return None

    def add_activity(self, activity_id, people_id, date, time, description):
        """
        Adds activity in the repository
        :param activity_id: int >= 1
        :param people_id: list of ints >= 1
        :param date: date object
        :param time: time object
        :param description: string
        :return: -
        :raises: ValidatorException if stuff dont go well
        """
        activity = Activity(activity_id, people_id, date, time, description)
        self.__a_validator.validate(activity)
        for i in activity.person_id:
            if not self.__p_repo.is_in_list(i):
                raise ValidatorException("people that don't exist can't take part in activities\n")
        for i in activity.person_id:
            person = Person(i, "", "")
            if self.person_already_has_activity(person, activity.date, activity.time):
                raise ValidatorException("user cannot have more than one activity at any given time\n")
        self.__a_repo.store(activity)

    def get_all_activities(self):
        return self.__a_repo.get_activities()

    def update_activity(self, activity_id, people_id, date, time, description):
        """
        Updates activity with new values for attributes
        :param activity_id: int >= 1
        :param people_id: list of ints >= 1
        :param date: date object
        :param time: time object
        :param description: string
        :return: -
        """
        activity = Activity(activity_id, people_id, date, time, description)
        self.__a_validator.validate(activity)
        for i in activity.person_id:
            if not self.__p_repo.is_in_list(i):
                raise ValidatorException("people that don't exist can't take part in activities\n")
        self.__a_repo.update(activity)

    def remove_activity(self, activity_id):
        """
        Removes activity by id
        :param activity_id: int >= 1
        :return: -
        """
        self.__a_repo.delete(activity_id)

    def remove_person_from_activity(self, person_id):
        """
        Removes a person from the people list removes that person from all activities including it
        If he was the only one in an activity, deletes the activity
        :param person_id: int >= 1
        :return: -
        """
        person = self.__p_repo.search(person_id)
        self.__p_repo.delete(person_id)
        activity_list = []
        activities = self.__a_repo.get_activities()
        for a in activities:
            if person_id in a.person_id:
                activity_list.append(a)
                people_ids = a.person_id[:]
                people_ids.remove(person_id)
                if len(people_ids) != 0:
                    self.update_activity(a.activity_id, people_ids, a.date, a.time, a.description)
                else:
                    self.remove_activity(a.activity_id)
        return person, activity_list

    def is_activity(self, activity_id):
        return self.__a_repo.is_in_list(activity_id)

    def search_activities(self, string):
        activities = self.__a_repo.get_activities()

        def keep_activity(a):
            return string.lower() in a.description.lower() or string.lower() in str(
                a.date).lower() or string.lower() in str(a.time).lower()

        Filtering.filter(activities, key=keep_activity)
        return activities

    def sort_activities(self):
        activities = self.__a_repo.get_activities()

        def activity_lt(a1, a2):
            return a1.activity_id > a2.activity_id

        Activity.__lt__ = activity_lt
        Activity.__gt__ = lambda x, y: not activity_lt(x, y)
        Sorting.sort(activities)
        return activities

    """
Create statistics:
Activities for a given date. List the activities for a given date, in the order of their start time.
Busiest days. This will provide the list of upcoming dates with activities, sorted in descending order 
of the free time in that day (all intervals with no activities).
Activities with a given person. List all upcoming activities to which a given person will participate.
    """

    def activities_for_date(self, date):
        """
        Gets the activities on a given date in the order of their start time. (sorted by 1.starting hour 2.starting minute)
        :param date: Date object
        :return: list of Activity objects
        """
        DateValidator.validate(date)
        activities = self.__a_repo.get_activities()
        date_activities = []
        for a in activities:
            if a.date == date:
                date_activities.append(a)

        # date_activities.sort(key=lambda x: x.time.start_m)
        # date_activities.sort(key=lambda x: x.time.start_h)
        def good_order(a1, a2):
            if a1.time.start_h == a2.time.start_h:
                return a1.time.start_m < a2.time.start_m
            return a1.time.start_h < a2.time.start_h
        Activity.__lt__ = good_order
        Activity.__gt__ = lambda x, y: not good_order(x, y)
        Sorting.sort(date_activities)
        return date_activities[:]

    @staticmethod
    def get_interval_of_time(time):
        return time.end_m - time.start_m + (time.end_h - time.start_h) * 60

    @staticmethod
    def find_id_of_dto(activity_dto, activity_dtos):
        """
        Gets the index of the dto in the list of dtos
        :param activity_dto: ActivityDTO object
        :param activity_dtos: list of ActivityDTO objects
        :return: the index(>=0), if it is in list, -1 otherwise
        """
        for i in range(len(activity_dtos)):
            if activity_dtos[i] == activity_dto:
                return i
        return -1

    def get_activity_dtos(self):
        """
        Gets the list of the activity_dtos. (objects that have date, list of activities on that date and interval of
        'activity hours' on that date, in minutes)
        :return: list of ActivityDTOs objects
        """
        activities = self.__a_repo.get_activities()
        activity_dtos = []
        for activity in activities:
            date = activity.date
            interval = ActivityService.get_interval_of_time(activity.time)
            activity_dto = ActivityDTO(date, [activity], interval)
            index = ActivityService.find_id_of_dto(activity_dto, activity_dtos)
            if index == -1:
                activity_dtos.append(activity_dto)
            else:
                activity_dtos[index].a_list.append(activity)
                activity_dtos[index].interval += ActivityService.get_interval_of_time(activity.time)
        return activity_dtos[:]

    def busiest_days(self):
        """
        Gets the list of the most busiest days; (sorted 1. descending by free time, 2. ascending by date)
        descending by free time <-> ascending by non-free time
        :return: list of ActivityDTOs objects
        """
        activities = self.get_activity_dtos()

        def good_order(a1, a2):
            if a1.interval == a2.interval:
                return a1.date < a2.date
            return a1.interval < a2.interval

        # activities.sort(key=lambda x: x.date)
        # activities.sort(key=lambda x: x.interval)
        ActivityDTO.__lt__ = good_order
        ActivityDTO.__gt__ = lambda x, y: not good_order(x, y)
        Sorting.sort(activities)
        return activities[:]

    def activities_with_a_person(self, person_id):
        """
        Gets the list of activities that a given person has, sorted by date and time.
        :param person_id: int >=1, has to be valid person
        :return: list of activities
        :raises: ValidatorException if the given person doesnt exist
        """
        if not self.__p_repo.is_in_list(person_id):
            raise ValidatorException("Person that doesn't exist does not have activities.\n")
        activities = self.__a_repo.get_activities()
        person_activities = []
        for activity in activities:
            if person_id in activity.person_id:
                person_activities.append(activity)
        person_activities = person_activities[:]

        def good_order(p1, p2):
            if p1.date == p2.date:
                if p1.time.start_h == p2.time.start_h:
                    return p1.time.start_m < p2.time.start_m
                return p1.time.start_h < p2.time.start_h
            return p1.date < p2.date

        # person_activities.sort(key=lambda x: x.time.start_m)
        # person_activities.sort(key=lambda x: x.time.start_h)
        # person_activities.sort(key=lambda x: x.date)
        Activity.__lt__ = good_order
        Activity.__gt__ = lambda x, y: not good_order(x, y)
        Sorting.sort(person_activities)
        return person_activities[:]


@dataclass
class ActivityDTO:
    """
    Asta e o micunealta ce ne va ajuta mai tarziu. ;)
    """
    date: Date
    a_list: list
    interval: int

    def __eq__(self, other):
        return self.date == other.date

    def __str__(self):
        if self.interval // 60 == 0:
            return "On the date {0}, the activities take {1} minute{2}.\n".format(self.date,
                                                                                  self.interval % 60,
                                                                                  '' if self.interval == 1 else 's')
        elif self.interval % 60 == 0:
            return "On the date {0}, the activities take {1} hour{2}.\n".format(self.date,
                                                                                self.interval // 60,
                                                                                '' if self.interval // 60 == 1 else 's')
        return "On the date {0}, the activities take {1} hour{3} and {2} minute{4}.\n".format(self.date,
                                                                                              self.interval // 60,
                                                                                              self.interval % 60,
                                                                                              '' if self.interval // 60 == 1 else 's',
                                                                                              '' if self.interval % 60 == 1 else 's')
