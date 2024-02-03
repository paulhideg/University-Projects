import pickle
from repositories.repositories import RepoStudents, RepoDisciplines, RepoGrades


class BinaryRepoStudents(RepoStudents):
    def __init__(self, txt):
        super().__init__()
        self.__txt = txt
        self.__read_from_binary()

    def __read_from_binary(self):
        with open(self.__txt, "rb") as f:
            try:
                while True:
                    super().add_student(pickle.load(f))
            except EOFError:
                pass

    def __append_to_binary(self, student):
        with open(self.__txt, "ab") as f:
            pickle.dump(student, f)

    def __write_to_binary(self):
        with open(self.__txt, "wb") as f:
            f.truncate(0)
            for student in super().get_all_students():
                pickle.dump(student, f)

    def add_student(self, student):
        super().add_student(student)
        self.__append_to_binary(student)

    def update_student(self, student_id, name):
        super().update_student(student_id, name)
        self.__write_to_binary()

    def remove_student(self, student_id):
        super().remove_student(student_id)
        self.__write_to_binary()


class BinaryRepoDisciplines(RepoDisciplines):
    def __init__(self, txt):
        super().__init__()
        self.__txt = txt
        self.__read_from_binary()

    def __read_from_binary(self):
        with open(self.__txt, "rb") as f:
            try:
                while True:
                    super().add_discipline(pickle.load(f))
            except EOFError:
                pass

    def __append_to_binary(self, discipline):
        with open(self.__txt, "ab") as f:
            pickle.dump(discipline, f)

    def __write_to_binary(self):
        with open(self.__txt, "wb") as f:
            f.truncate(0)
            for discipline in super().get_all_disciplines():
                pickle.dump(discipline, f)

    def add_discipline(self, discipline):
        super().add_discipline(discipline)
        self.__append_to_binary(discipline)

    def update_discipline(self, discipline_id, name):
        super().update_discipline(discipline_id, name)
        self.__write_to_binary()

    def remove_discipline(self, discipline_id):
        super().remove_discipline(discipline_id)
        self.__write_to_binary()


class BinaryRepoGrades(RepoGrades):
    def __init__(self, txt):
        super().__init__()
        self.__txt = txt
        self.__read_from_binary()

    def __read_from_binary(self):
        with open(self.__txt, "rb") as f:
            try:
                while True:
                    grade = pickle.load(f)
                    super().add_grade(grade, grade.get_grade_value())
            except EOFError:
                pass

    def __append_to_binary(self, grade):
        with open(self.__txt, "ab") as f:
            pickle.dump(grade, f)

    def __write_to_binary(self):
        with open(self.__txt, "wb") as f:
            f.truncate(0)
            for grade in super().get_all_grades():
                pickle.dump(grade, f)

    def add_grade(self, grade, grade_value):
        grades_len = super().__len__()
        super().add_grade(grade, grade_value)
        grades_len_2 = super().__len__()
        if grades_len != grades_len_2:
            self.__append_to_binary(grade)
        else:
            self.__write_to_binary()

    def remove_grade(self, student, discipline, grade, grade_value):
        super().remove_grade(student, discipline, grade, grade_value)
        self.__write_to_binary()

    def remove_grades_student(self, student_id):
        super().remove_grades_student(student_id)
        self.__write_to_binary()

    def remove_grades_discipline(self, discipline_id):
        super().remove_grades_discipline(discipline_id)
        self.__write_to_binary()
