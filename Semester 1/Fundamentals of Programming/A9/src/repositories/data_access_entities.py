from abc import ABC, abstractmethod
from domain.student import Student
from domain.discipline import Discipline
from domain.grade import Grade


class DataAccessEntities(ABC):
    @staticmethod
    @abstractmethod
    def read_from(line):
        pass

    @staticmethod
    @abstractmethod
    def write_to(f, entity):
        pass


class StudentDataAccess(Student, DataAccessEntities):
    @staticmethod
    def read_from(line):
        line = line.strip()
        if line != "":
            parts = line.split(";")
            return Student(int(parts[0]), parts[1])

    @staticmethod
    def write_to(f, student):
        f.write(str(student.get_student_id()) +
                ';' + student.get_name() + '\n')


class DisciplineDataAccess(Discipline, DataAccessEntities):
    @staticmethod
    def read_from(line):
        line = line.strip()
        if line != "":
            parts = line.split(";")
            return Discipline(int(parts[0]), parts[1])

    @staticmethod
    def write_to(f, discipline):
        f.write(str(discipline.get_discipline_id()) +
                ';' + discipline.get_name() + '\n')


class GradeDataAccess(Grade, DataAccessEntities):
    @staticmethod
    def read_from(line):
        line = line.strip()
        if line != "":
            parts = line.split(";")
            str_grades_value = parts[2]
            parts_grade_value = str_grades_value.split(",")
            grades_value = []
            for part in parts_grade_value:
                grades_value.append(int(part))
            return Grade(int(parts[0]), int(parts[1]), grades_value)

    @staticmethod
    def write_to(f, grade):
        str_grades_value = str(grade.get_grade_value()[0])
        for i in range(1, len(grade.get_grade_value())):
            str_grades_value += "," + str(grade.get_grade_value()[i])
        f.write(str(grade.get_student_id()) + ";" +
                str(grade.get_discipline_id()) + ";" + str_grades_value + '\n')
