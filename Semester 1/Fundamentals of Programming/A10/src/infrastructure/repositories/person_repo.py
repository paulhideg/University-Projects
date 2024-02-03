from a10_modules.iterable_ds import IterableDS
from errors.exceptions import RepositoryException


class PersonRepository:
    """
    Class of People repository
    """

    def __init__(self):
        self.__person_repo = IterableDS()

    def __len__(self):
        return len(self.__person_repo)

    def to_dict(self):
        return {self.__person_repo[i].person_id: (self.__person_repo[i].name, self.__person_repo[i].phone_number)
                for i in range(len(self.__person_repo))}

    def find_by_id(self, p_id):
        for p in self.__person_repo:
            if p.person_id == p_id:
                return p
        return None

    def store(self, person):
        """
        Adds the person in list if it is not already there
        :param person: person object
        :return: -
        :raises: RepositoryException if there is a duplicate person
        """
        if self.find_by_id(person.person_id) is not None:
            raise RepositoryException("person already exists\n")
        self.__person_repo.append(person)

    def search(self, p_id):
        """
        Searches a person in a repo
        :param p_id: int >= 1
        :return: person object if it is found
        :raises: RepositoryException if it doesnt exist
        """
        for p in self.__person_repo:
            if p.person_id == p_id:
                return p
        raise RepositoryException("person doesn't exist\n")

    def is_in_list(self, p_id):
        """
        Checks whether there exists a person with a given id
        :param p_id: int >= 1
        :return: True or false
        """
        for p in self.__person_repo:
            if p.person_id == p_id:
                return True
        return False

    def search_by_name_phone(self, string):
        """
        Searches all people that partially contain given string in name or phone
        :param string: string
        :return: list of people
        """
        result = []
        for p in self.__person_repo:
            if string.lower() in p.name.lower() or string.lower() in \
                    p.phone_number.lower():
                result.append(p)
        return result[:]

    def get_people(self):
        return self.__person_repo.elems

    def update(self, person):
        """
        Updates person
        :param person: activity object
        :return:  -
        :raises: RepositoryException if the person doesnt exist
        """
        for i in range(len(self.__person_repo)):
            if self.__person_repo[i] == person:
                self.__person_repo[i] = person
                return
        raise RepositoryException("person doesn't exist\n")

    def delete(self, p_id):
        """
        Deletes a person by the id from given key person
        :param p_id: person object used mainly for id
        :return: -
        :raises: RepositoryException if person doesnt exist
        """
        for i in range(len(self.__person_repo)):
            if self.__person_repo[i].person_id == p_id:
                del self.__person_repo[i]
                return
        raise RepositoryException("person doesn't exist\n")
