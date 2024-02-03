import random

from domain.useful_stuff.undoredo_operation import UndoHandler


class PersonGenerator:
    """
    Class that generates a person
    """

    def __init__(self, p_service, undo_redo_service):
        """
        Initializes attributes
        :param p_service: PersonService object
        """
        self.__p_service = p_service
        self.undo_redo_service = undo_redo_service
        self.__ids = []
        self.__names = ["Amy Pond", "River Song", "Clara Oswald", "Martha Jones", "Jack Harkness", "Melody Pond",
                        "Rose Tyler", "Jane Smith", "Gwen Cooper", "Donna Noble"]
        self.__phones = []

    def generate_phones(self):
        """
        Generates a string of 10 digit characters representing phone number
        :return:
        """
        phone = ''
        for j in range(10):
            phone += str(random.randint(0, 9))
        return phone

    def generate_people(self):
        '''
        "Not only it generates a bunch of stuff, but it also generates ANOTHER stuff." <3
        :return:
        '''
        self.generate_phones()
        for i in range(10):
            p_id = random.randint(1, 100)
            while self.__p_service.is_person(p_id):
                p_id = random.randint(1, 100)
            phone = self.generate_phones()
            self.__p_service.add_person(p_id, self.__names[i], phone)
            undo_redo_op = self.undo_redo_service.create_operation(self.__p_service, UndoHandler.ADD_PERSON, p_id,
                                                                   self.__names[i], phone)
            self.undo_redo_service.push(undo_redo_op)
