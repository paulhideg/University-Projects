from repositories.data_access_entities import StudentDataAccess, DisciplineDataAccess, GradeDataAccess
from repositories.repositories import RepoStudents, RepoDisciplines, RepoGrades


class FileRepoStudents(RepoStudents):
    def __init__(self, txt):
        super().__init__()
        self.__txt = txt
        self.__read_from_file()

    def __read_from_file(self):
        with open(self.__txt, "r") as f:
            for line in f:
                student = StudentDataAccess.read_from(line)
                if student is not None:
                    super().add_student(student)

    def __append_to_file(self, student):
        with open(self.__txt, "a") as f:
            StudentDataAccess.write_to(f, student)

    def __write_to_file(self):
        with open(self.__txt, "w") as f:
            f.truncate(0)
        for student in super().get_all_students():
            self.__append_to_file(student)

    def add_student(self, student):
        super().add_student(student)
        self.__append_to_file(student)

    def update_student(self, student_id, name):
        super().update_student(student_id, name)
        self.__write_to_file()

    def remove_student(self, student_id):
        super().remove_student(student_id)
        self.__write_to_file()

    def random_students(self):
        super().random_students()
        self.__write_to_file()


class FileRepoDisciplines(RepoDisciplines):
    def __init__(self, txt):
        super().__init__()
        self.__txt = txt
        self.__read_from_file()

    def __read_from_file(self):
        with open(self.__txt, "r") as f:
            for line in f:
                discipline = DisciplineDataAccess.read_from(line)
                if discipline is not None:
                    super().add_discipline(discipline)

    def __append_to_file(self, discipline):
        with open(self.__txt, "a") as f:
            DisciplineDataAccess.write_to(f, discipline)

    def __write_to_file(self):
        with open(self.__txt, "w") as f:
            f.truncate(0)
        for discipline in super().get_all_disciplines():
            self.__append_to_file(discipline)

    def add_discipline(self, discipline):
        super().add_discipline(discipline)
        self.__append_to_file(discipline)

    def update_discipline(self, discipline_id, name):
        super().update_discipline(discipline_id, name)
        self.__write_to_file()

    def remove_discipline(self, discipline_id):
        super().remove_discipline(discipline_id)
        self.__write_to_file()

    def random_disciplines(self):
        super().random_disciplines()
        self.__write_to_file()


class FileRepoGrades(RepoGrades):
    def __init__(self, txt):
        super().__init__()
        self.__txt = txt
        self.__read_from_file()

    def __read_from_file(self):
        with open(self.__txt, "r") as f:
            for line in f:
                grade = GradeDataAccess.read_from(line)
                if grade is not None:
                    super().add_grade(grade, grade.get_grade_value())

    def __append_to_file(self, grade):
        with open(self.__txt, "a") as f:
            GradeDataAccess.write_to(f, grade)

    def __write_to_file(self):
        with open(self.__txt, "w") as f:
            f.truncate(0)
        for grade in super().get_all_grades():
            self.__append_to_file(grade)

    def add_grade(self, grade, grade_value):
        grades_len = super().__len__()
        super().add_grade(grade, grade_value)
        grades_len_2 = super().__len__()
        if grades_len != grades_len_2:
            self.__append_to_file(grade)
        else:
            self.__write_to_file()

    def remove_grade(self, student, discipline, grade, grade_value):
        super().remove_grade(student, discipline, grade, grade_value)
        self.__write_to_file()

    def remove_grades_student(self, student_id):
        super().remove_grades_student(student_id)
        self.__write_to_file()

    def remove_grades_discipline(self, discipline_id):
        super().remove_grades_discipline(discipline_id)
        self.__write_to_file()

    def random_grades(self):
        super().random_grades()
        self.__write_to_file()
