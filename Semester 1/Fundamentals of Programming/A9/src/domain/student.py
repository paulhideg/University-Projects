class Student:
    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name

    def __str__(self):
        return str("Student with id " + str(self.__student_id) + " and name: " + self.__name)

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name
