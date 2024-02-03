from domain.student import Student
from domain.discipline import Discipline
from domain.grade import Grade


class ServiceGrades(object):
    def __init__(self, valid_grade, valid_student, valid_discipline, repo_grades, repo_students, repo_disciplines, repo_undo):
        self.__valid_grade = valid_grade
        self.__valid_student = valid_student
        self.__valid_discipline = valid_discipline
        self.__repo_grades = repo_grades
        self.__repo_students = repo_students
        self.__repo_disciplines = repo_disciplines
        self.__repo_undo = repo_undo

    def random_students_disciplines_grades(self):
        """
        generates the random students repos
        """
        self.__repo_students.random_students()
        self.__repo_disciplines.random_disciplines()
        self.__repo_grades.random_grades()

    def nr_of_grades(self):
        """
        returns the number of grades
        """
        return len(self.__repo_grades)

    def add_grade(self, student_id, discipline_id, grade_value):
        """
        adds a single grade 
        """
        grade = Grade(student_id, discipline_id, grade_value)
        self.__valid_grade.validate(grade, grade_value)
        student = self.__repo_students.search_by_id(student_id)
        discipline = self.__repo_disciplines.search_by_id(discipline_id)
        self.__repo_grades.add_grade(grade, grade_value)

    def remove_grade(self, student_id, discipline_id, grade_value):
        """
        removes a single grade value
        """
        grade = Grade(student_id, discipline_id, grade_value)
        self.__valid_grade.validate(grade, grade_value)
        student = self.__repo_students.search_by_id(student_id)
        discipline = self.__repo_disciplines.search_by_id(discipline_id)
        self.__repo_grades.remove_grade(
            student, discipline, grade, grade_value)

    def add_multiple_grades(self, student_id, discipline_id, grade_values):
        """
        adds a list of grades
        """
        for grade_value in grade_values:
            grade = Grade(student_id, discipline_id, grade_value)
            self.__valid_grade.validate(grade, grade_value)
            student = self.__repo_students.search_by_id(student_id)
            discipline = self.__repo_disciplines.search_by_id(discipline_id)
            self.__repo_grades.add_grade(grade, grade_value)

    def add_multiple_grades_complex(self, list_of_grades):
        """
        adds multiple grades based on the student id
        params: list of grades = [grade_obj(grade object), grade_values(list)]
        """
        for grade in list_of_grades:
            grade_obj = grade[0]
            grade_values = grade[1]
            self.add_multiple_grades(grade_obj.get_student_id(
            ), grade_obj.get_discipline_id(), grade_values)

    def remove_multiple_grades(self, student_id, discipline_id, grade_values):
        for grade_value in grade_values:
            grade = Grade(student_id, discipline_id, grade_value)
            self.__valid_grade.validate(grade, grade_value)
            student = self.__repo_students.search_by_id(student_id)
            discipline = self.__repo_disciplines.search_by_id(discipline_id)
            self.__repo_grades.remove_grade(
                student, discipline, grade, grade_value)

    def get_grades_by_student_id(self, student_id):
        """
        returns a list of grade objects that have a specific student id
        """
        return self.__repo_grades.get_grades_by_student_id(student_id)

    def get_grades_by_discipline_id(self, discipline_id):
        """
        returns a list of grade objects that have a specific student id
        """
        return self.__repo_grades.get_grades_by_discipline_id(discipline_id)

    def get_all_grades(self):
        """
        returns a list of all the registered grades
        """
        return self.__repo_grades.get_all_grades()

    def remove_student(self, student_id):
        """
        removes a student based on his id, 
        along with removing all his grades
        """
        self.__repo_grades.remove_grades_student(student_id)

    def remove_discipline(self, discipline_id):
        """
        removes a discipline based on it's id,
        along with all the grades at that disicpline
        """
        self.__repo_grades.remove_grades_discipline(discipline_id)

    """
                STATISTICS
                    |       |
                    |       |
                    V     V
    """

    def students_failing(self):
        """
        returns a list of the students that are failing
        """
        students_failing = []
        id_failling = self.__repo_grades.students_failing()
        for id in id_failling:
            students_failing.append(self.__repo_students.search_by_id(id))
        return students_failing

    def students_top(self):
        """
        returns a list of the students sorted by their aggregated average
        """
        students_top = self.__repo_grades.students_top()
        for id in students_top:
            id[0] = self.__repo_students.search_by_id(id[0])
        return students_top

    def disciplines_highest(self):
        """
        returns a list of the disicplines sorted by the avergage grade
        """
        disciplines_highest = self.__repo_grades.disciplines_highest()
        for id in disciplines_highest:
            id[0] = self.__repo_disciplines.search_by_id(id[0])
        return disciplines_highest
