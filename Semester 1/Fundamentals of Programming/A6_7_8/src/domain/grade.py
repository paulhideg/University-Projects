class Grade:
    def __init__(self, student_id, discipline_id, grade_value):
        self.__student_id = student_id
        self.__discipline_id = discipline_id
        self.__grade_value = [grade_value]

    def __str__(self):
        return str("Student id: " + str(self.__student_id) + "   Discipline id: " + str(self.__discipline_id) + "   Has grade(s): " + str(self.__grade_value))

    def get_student_id(self):
        return self.__student_id

    def get_discipline_id(self):
        return self.__discipline_id

    def get_grade_value(self):
        return self.__grade_value

    def set_grade_value(self, value):
        self.__grade_value.append(value)
