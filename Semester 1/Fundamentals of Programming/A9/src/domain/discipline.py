class Discipline:
    def __init__(self, discipline_id, name):
        self.__discipline_id = discipline_id
        self.__name = name

    def __str__(self):
        return str("Discipline with id " + str(self.__discipline_id) + " and name: " + self.__name)

    def get_discipline_id(self):
        return self.__discipline_id

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value
