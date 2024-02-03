class Services:
    def __init__(self):
        self._students = []

    @property
    def students(self):
        return self._students

    @students.setter
    def students(self, list):
        self._students = list

    def add_student(self, new_student):
        """
        Function that adds new objects (students)
        :param new_expense: Composed of the id, name and group
        :return:
        """

        for student in self._students:
            if student.id == new_student.id:
                raise ValueError("A student with this id already exist")
            if student.group < 1:
                raise ValueError("Group lower than 1 not allowed")
        self._students.append(new_student)

    def filter_student(self, group):
        """
        Function that filters the objects based on the value entered by the user using lambda
        :param group: The group entered by the user
        :return:
        """

        self._students = list(
            filter(lambda x: x.group != group, self._students))
