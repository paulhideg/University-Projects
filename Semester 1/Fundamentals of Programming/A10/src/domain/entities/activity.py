"""
Activity: activity_id, person_id - list, date, time, description
"""


class Activity:
    """
    Class that encapsulate an activity having an id, a list of people's ids, date, time and description
    """

    def __init__(self, activity_id, person_id, date, time, description):
        """
        Initializes attributes
        :param activity_id: natural number >=1
        :param person_id: list of natural number >=1
        :param date: object of my custom type Date
        :param time: object of my custom type Time
        :param description: string
        """
        self.__activity_id = activity_id
        self.__person_id = person_id[:]
        self.__date = date
        self.__time = time
        self.__description = description

    @property
    def activity_id(self):
        return self.__activity_id

    @property
    def person_id(self):
        return self.__person_id

    @person_id.setter
    def person_id(self, value):
        self.__person_id = value[:]

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    def __eq__(self, other):
        return self.__activity_id == other.__activity_id

    def __ne__(self, other):
        if self.__activity_id != other.__activity_id or self.__date != other.__date or self.__time != other.__time or self.__description != other.__description:
            return True
        return False

    def __str__(self):
        # TODO: format person_id (list of integers representing ides)
        return "{0}:\nPeople: {1}\nDate: {2}\nTime: {3}\nDescription: {4}\n".format(self.__activity_id,
                                                                                    self.__person_id, self.__date,
                                                                                    self.__time, self.__description)
