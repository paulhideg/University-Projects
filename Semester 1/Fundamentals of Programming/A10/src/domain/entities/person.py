"""
person_id, name, phone_number
"""


class Person:
    """
    Class that encapsulate a Person having an id, a name and a phone number
    """

    def __init__(self, person_id, name, phone_number):
        """
        Initializes attributes
        :param person_id: natural number >=1
        :param name: string
        :param phone_number: string of 10 digits characters
        """
        self.__person_id = person_id
        self.__name = name
        self.__phone_number = phone_number

    @property
    def person_id(self):
        return self.__person_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    def __eq__(self, other):
        return self.__person_id == other.__person_id

    def __str__(self):
        return "{0}: Name: {1}, Phone: {2}\n".format(self.person_id, self.name, self.phone_number)
