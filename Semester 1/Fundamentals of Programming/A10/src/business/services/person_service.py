from a10_modules.filtering import Filtering
from a10_modules.sorting import Sorting
from domain.entities.person import Person


class PersonService:
    """
    Service of People
    """

    def __init__(self, p_repo, p_validator):
        self.__p_repo = p_repo
        self.__p_validator = p_validator

    def add_person(self, person_id, person_name, phone_number):
        """
        Adds person to the repo
        :param person_id: int >= 1
        :param person_name: string
        :param phone_number: string of length 10 containing digits characters
        :return:
        """
        person = Person(person_id, person_name, phone_number)
        self.__p_validator.validate(person)
        self.__p_repo.store(person)

    def get_all_people(self):
        return self.__p_repo.get_people()

    def update_person(self, person_id, person_name, phone_number):
        """
        Updates person
        :param person_id: int >= 1
        :param person_name: string
        :param phone_number: string of 10 digits characters
        :return:
        """
        person = Person(person_id, person_name, phone_number)
        self.__p_validator.validate(person)
        self.__p_repo.update(person)

    def remove_person(self, person_id):
        """
        Removes person by id
        :param person_id: int >= 1
        :return:
        """
        self.__p_repo.delete(person_id)

    def search_people(self, string):
        """
        Searches all people partially by phone and name
        :param string: string obviously
        :return: list of people
        """
        people = self.__p_repo.get_people()

        def keep_person(person):
            return string.lower() in person.name.lower() or string.lower() in person.phone_number.lower()

        Filtering.filter(people, key=keep_person)
        return people

    def sort_people(self):
        people = self.__p_repo.get_people()
        Sorting.sort(people, key=lambda x: x.name)
        return people

    def is_person(self, person_id):
        """
        Checks whether a given id represents a person in our repo
        :param person_id:
        :return:
        """
        return self.__p_repo.is_in_list(person_id)

    def search(self, p_id):
        people = self.__p_repo.get_people()
        for p in people:
            if p_id == p.person_id:
                return p
        return None
