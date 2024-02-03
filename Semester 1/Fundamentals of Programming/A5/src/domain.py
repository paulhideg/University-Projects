import random


class Student:
    def __init__(self, id, name, group):
        """
            We create an object Student of the class Student with the following properties:
            :param id: Integer,unique. The id of the student
            :param name: String. The name of the student
            :param group: Positive Integer. The group in which the student is
            """
        self._id = id
        self._name = name
        self._group = group

    def __str__(self):
        """
        return: A string of the object
        """
        return "Student with id " + str(self._id) + " and name " + self._name + " in group " + str(self._group)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value

    @staticmethod
    def sample_students():
        """

        :return: Randomly generated students list
        """
        names = ["Carlee Oliver", "Josephine Moss", "Destiney Russo", "Dax Hurley", "Steve Novak", "Angel Zuniga", "Jazmin Baldwin", "Karina Cherry",
                 "Alannah Mcfarland", "Carmelo Morrison", "Ahmad Villanueva", "Marlee Dominguez", "Quintin Schaefer", "Kamren Jordan", "Rhianna Reilly"]
        students = []
        student_ids = random.sample(range(1, 100), 10)
        for i in range(0, 10):
            students.append(Student(student_ids[i],
                            random.choice(names), random.randint(1, 10)))
        return students
