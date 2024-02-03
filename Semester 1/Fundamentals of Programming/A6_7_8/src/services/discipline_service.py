from domain.discipline import Discipline


class ServiceDisciplines(object):
    def __init__(self, valid_discipline, repo_disciplines, repo_undo):
        self.__valid_discipline = valid_discipline
        self.__repo_disciplines = repo_disciplines
        self.__repo_undo = repo_undo

    def nr_of_disciplines(self):
        """
       Returns the number of disciplines
        """
        return len(self.__repo_disciplines)

    def add_discipline(self, discipline_id, name):
        """
       Adds a discipline
        """
        discipline = Discipline(discipline_id, name)
        self.__valid_discipline.validate(discipline)
        self.__repo_disciplines.add_discipline(discipline)

    def add_full_discipline(self, discipline):
        self.__repo_disciplines.add_discipline(discipline)

    def remove_discipline(self, discipline_id):
        """
        removes a discipline based on it's id,
        along with all the grades at that disicpline
        """
        self.__repo_disciplines.remove_discipline(discipline_id)

    def update_discipline(self, discipline_id, name):
        """
       Updates a discipline's name
        """
        discipline = Discipline(discipline_id, name)
        self.__valid_discipline.validate(discipline)
        self.__repo_disciplines.update_discipline(discipline_id, name)

    def get_all_disciplines(self):
        """
       Returns a list of all the disciplines
        """
        return self.__repo_disciplines.get_all_disciplines()

    def search_disciplines(self, value):
        """
       Searches disciplines by a given string
        """
        return self.__repo_disciplines.search_disciplines(value)

    def search_discipline_by_id(self, discipline_id):
        return self.__repo_disciplines.search_by_id(discipline_id)
