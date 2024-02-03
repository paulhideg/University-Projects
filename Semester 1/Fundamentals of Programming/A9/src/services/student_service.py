from domain.student import Student


class ServiceStudents(object):
    def __init__(self, valid_student, repo_students, repo_undo):
        self.__valid_student = valid_student
        self.__repo_students = repo_students
        self.__repo_undo = repo_undo

    def nr_of_students(self):
        """
       Returns the number of students
        """
        return len(self.__repo_students)

    def add_student(self, student_id, name):
        """
       Adds a student 
        """
        student = Student(student_id, name)
        self.__valid_student.validate(student)
        self.__repo_students.add_student(student)

    def add_full_student(self, student):
        self.__repo_students.add_student(student)

    def remove_student(self, student_id):
        """
        removes a student based on his id, 
        along with removing all his grades
        """
        self.__repo_students.remove_student(student_id)

    def update_student(self, student_id, name):
        """
       Updates a student's name
        """
        student = Student(student_id, name)
        self.__valid_student.validate(student)
        self.__repo_students.update_student(student_id, name)

    def get_all_students(self):
        """
       Returns a list of all the students
        """
        return self.__repo_students.get_all_students()

    def search_students(self, value):
        """
       Searches students by a given string
        """
        return self.__repo_students.search_students(value)

    def search_student_by_id(self, student_id):
        return self.__repo_students.search_by_id(student_id)
