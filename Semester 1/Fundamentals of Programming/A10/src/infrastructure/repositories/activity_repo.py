from a10_modules.iterable_ds import IterableDS
from errors.exceptions import RepositoryException


class ActivityRepository:
    """
    Repository for activities
    """

    def __init__(self):
        self.__activity_repo = IterableDS()

    def to_dict(self):
        return {self.__activity_repo[i].activity_id: [[self.__activity_repo[i].person_id[j] for j in
                                                       range(len(self.__activity_repo[i].person_id))],
                                                      [self.__activity_repo[i].date.day,
                                                       self.__activity_repo[i].date.month,
                                                       self.__activity_repo[i].date.year],
                                                      [self.__activity_repo[i].time.start_h,
                                                       self.__activity_repo[i].time.start_m,
                                                       self.__activity_repo[i].time.end_h,
                                                       self.__activity_repo[i].time.end_m],
                                                      self.__activity_repo[i].description] for i in
                range(len(self.__activity_repo))}

    def find_by_id(self, a_id):
        for a in self.__activity_repo:
            if a.activity_id == a_id:
                return a
        return None

    def store(self, activity):
        """
        Adds the activity in list if it is not already there
        :param activity: activity object
        :return: -
        :raises: RepositoryException if there is a duplicate activity
        """
        if self.find_by_id(activity.activity_id) is not None:
            raise RepositoryException("activity already exists\n")
        self.__activity_repo.append(activity)

    def __len__(self):
        return len(self.__activity_repo)

    def search(self, a_id):
        """
        Searches an activity in a repo
        :param a_id: activity object having important id and other useless stuff
        :return: activity object if it is found
        :raises: RepositoryException if it doesnt exist
        """
        for a in self.__activity_repo:
            if a.activity_id == a_id:
                return a
        raise RepositoryException("activity doesn't exist\n")

    def is_in_list(self, a_id):
        """
        Checks whether there exists an activity with a given id
        :param a_id: int >= 1
        :return: True or false
        """
        for a in self.__activity_repo:
            if a.activity_id == a_id:
                return True
        return False

    def search_by_date_time_description(self, string):
        """
        Searches all activities that partially contain given string in date, time and description
        :param string: string
        :return: list of activities
        """
        result = []
        for a in self.__activity_repo:
            if string.lower() in a.description.lower() or string.lower() in str(
                    a.date).lower() or \
                    string.lower() in str(a.time).lower():
                result.append(a)
        return result

    def search_person_activities(self, person):
        """
        Searches all the activities a given person has
        :param person: person object
        :return: list of activities
        """
        activity_list = []
        for a in self.__activity_repo:
            if person.person_id in a.person_id:
                activity_list.append(a)
        return activity_list

    def get_activities(self):
        return self.__activity_repo.elems

    def update(self, activity):
        """
        Updates activity
        :param activity: activity object
        :return:  -
        :raises: RepositoryException if the activity doesnt exist
        """
        for i in range(len(self.__activity_repo)):
            if self.__activity_repo[i] == activity:
                self.__activity_repo[i] = activity
                return
        raise RepositoryException("activity doesn't exist\n")

    def delete(self, a_id):
        """
        Deletes an activity by the id from given key activity
        :param a_id: activity object used mainly for id
        :return: -
        :raises: RepositoryException if activity doesnt exist
        """
        for i in range(len(self.__activity_repo)):
            if self.__activity_repo[i].activity_id == a_id:
                del self.__activity_repo[i]
                return
        raise RepositoryException("activity doesn't exist\n")
