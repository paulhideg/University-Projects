import random

from domain.entities.person import Person
from domain.useful_stuff.date import Date
from domain.useful_stuff.time import Time
from datetime import date, datetime

from domain.useful_stuff.undoredo_operation import UndoHandler


class ActivityGenerator:
    """
    Class that randomly generates good activities
    """

    def __init__(self, a_service, p_service, undo_redo_service):
        """
        Initializes attributes
        :param a_service: object of type ActivityService
        :param p_service: object of type PersonService
        """
        self.__a_service = a_service
        self.__p_service = p_service
        self.undo_redo_service = undo_redo_service
        self.__descriptions = ['play', 'learn', 'cry', 'do homework', 'learn for the partial exam', 'cry some more',
                               'sleep', 'cry before sleep', 'cry while doing homework', 'cry while taking exams']

    def generate_date(self):
        """
        Generates a valid date
        :return: date
        """
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(2020, 2021)
        my_date = Date(day, month, year)
        today = date.today().strftime("%d.%m.%Y")
        cd, cm, cy = today.split('.')
        today = Date(int(cd), int(cm), int(cy))
        while my_date < today:
            day = random.randint(1, 28)
            month = random.randint(1, 12)
            year = random.randint(2020, 2021)
            my_date = Date(day, month, year)
        return my_date

    def generate_time(self, gen_date):
        """
        Generates a random valid time
        :return:
        """
        start_h = random.randint(0, 21)
        end_h = random.randint(start_h + 1, start_h + 2)
        start_m = random.choice([0, 30])
        end_m = random.choice([0, 30])
        today = date.today().strftime("%d.%m.%Y")
        cd, cm, cy = today.split('.')
        today = Date(int(cd), int(cm), int(cy))
        if gen_date != today:
            return Time(start_h, start_m, end_h, end_m)
        time = Time(start_h, start_m, end_h, end_m)
        now = datetime.now().strftime("%H:%M")
        ch, cm = now.split(':')
        ch = int(ch)
        cm = int(cm)
        while time.start_h < ch or (time.start_h == ch and time.start_m < cm):
            start_h = random.randint(ch, 21)
            end_h = random.randint(start_h + 1, start_h + 2)
            start_m = random.choice([0, 30])
            end_m = random.choice([0, 30])
            time = Time(start_h, start_m, end_h, end_m)
        return time

    def generate_people_ids(self):
        """
        Generates people's ids randomly and validly: Chooses people that actually exist
        :return: list of integers representing people's ids
        """
        people_id_list = []
        n = random.randint(1, 3)
        people = self.__p_service.get_all_people()
        people_id = []
        for p in people:
            people_id.append(p.person_id)
        for j in range(n):
            rand = random.choice(people_id)
            while rand in people_id_list:
                rand = random.choice(people_id)
            people_id_list.append(rand)
        return people_id_list[:]

    def get_activities_of_person_on_a_date(self, person, a_date):
        """
        Finds all the activities that a person has on a given date
        :param person: a person object
        :param a_date: a date object
        :return: list of activities
        """
        activities = self.__a_service.get_all_activities()
        pers_activity = []
        for a in activities:
            if person.person_id in a.person_id and a.date == a_date:
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

    def good_people(self, people_ids, date, time):
        """
        Checks whether the list of people_ids is valid, meaning that they don't already have an activity at that time
        :param people_ids: list of ints >= 1
        :param date: date object
        :param time: time object
        :return: True or False
        """
        for p_id in people_ids:
            person = Person(p_id, "", "")
            if self.person_already_has_activity(person, date, time):
                return False
        return True

    def generate_activities(self):
        '''
        "Not only it generates a bunch of stuff, but it also generates ANOTHER stuff." <3
        :return:
        '''
        random.shuffle(self.__descriptions)
        for i in range(10):
            a_id = random.randint(1, 100)
            while self.__a_service.is_activity(a_id):
                a_id = random.randint(1, 100)
            people_ids = self.generate_people_ids()
            date = self.generate_date()
            time = self.generate_time(date)
            while not self.good_people(people_ids, date, time):
                people_ids = self.generate_people_ids()
                date = self.generate_date()
                time = self.generate_time(date)
            self.__a_service.add_activity(a_id, people_ids, date, time, self.__descriptions[i])
            undo_redo_op = self.undo_redo_service.create_operation(self.__a_service, UndoHandler.ADD_ACTIVITY,
                                                                   a_id, people_ids, date, time, self.__descriptions[i])
            self.undo_redo_service.push(undo_redo_op)
