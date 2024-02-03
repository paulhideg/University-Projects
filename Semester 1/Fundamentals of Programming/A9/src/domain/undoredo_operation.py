from dataclasses import dataclass
from enum import Enum


def add_student_handler(student_service, student_id, student_name):
    student_service.remove_student(student_id)


def remove_student_handler(student_service, student_id, student_name):
    student_service.add_student(student_id, student_name)


def update_student_handler(student_service, student_id, old_student_name, new_student_name):
    student_service.update_student(student_id, old_student_name)


def update_student_rev_handler(student_service, student_id, old_student_name, new_student_name):
    student_service.update_student(student_id, new_student_name)


def add_discipline_handler(discipline_service, discipline_id, discipline_name):
    discipline_service.remove_discipline(discipline_id)


def remove_discipline_handler(discipline_service, discipline_id, discipline_name):
    discipline_service.add_discipline(discipline_id, discipline_name)


def update_discipline_handler(discipline_service, discipline_id, old_discipline_name, new_discipline_name):
    discipline_service.update_discipline(discipline_id, old_discipline_name)


def update_discipline_rev_handler(discipline_service, discipline_id, old_discipline_name, new_discipline_name):
    discipline_service.update_discipline(discipline_id, new_discipline_name)


def add_grade_handler(grade_service, student_id, discipline_id, grades):
    grade_service.remove_multiple_grades(student_id, discipline_id, grades)


def remove_grade_handler(grade_service, student_id, discipline_id, grades):
    grade_service.add_multiple_grades(student_id, discipline_id, grades)


class UndoHandler(Enum):
    ADD_STUDENT = add_student_handler
    REMOVE_STUDENT = remove_student_handler
    UPDATE_STUDENT = update_student_handler
    UPDATE_STUDENT_REV = update_student_rev_handler
    ADD_DISCIPLINE = add_discipline_handler
    REMOVE_DISCIPLINE = remove_discipline_handler
    UPDATE_DISCIPLINE = update_discipline_handler
    UPDATE_DISCIPLINE_REV = update_discipline_rev_handler
    ADD_GRADE = add_grade_handler
    REMOVE_GRADE = remove_grade_handler

    @staticmethod
    def get_opposite_handler(handler):
        if handler == UndoHandler.ADD_STUDENT:
            return UndoHandler.REMOVE_STUDENT
        if handler == UndoHandler.UPDATE_STUDENT:
            return UndoHandler.UPDATE_STUDENT_REV
        if handler == UndoHandler.ADD_DISCIPLINE:
            return UndoHandler.REMOVE_DISCIPLINE
        if handler == UndoHandler.UPDATE_DISCIPLINE:
            return UndoHandler.UPDATE_DISCIPLINE_REV
        if handler == UndoHandler.ADD_GRADE:
            return UndoHandler.REMOVE_GRADE


@dataclass
class UndoRedoOperation:
    target_object: object
    handler: object
    args: tuple

    def perform_operation(self):
        self.handler(self.target_object, *self.args)

    def perform_reverse_operation(self):
        opposite_handler = UndoHandler.get_opposite_handler(self.handler)
        opposite_handler(self.target_object, *self.args)


"COMPLEX OPERATIONS"


def remove_student_complex_handler(student_services, grade_services, student, list_of_deleted_grades):
    student_services.add_full_student(student)
    grade_services.add_multiple_grades_complex(list_of_deleted_grades)


def add_student_complex_handler(student_services, grade_services, student, studentt):
    student_services.remove_student(student.get_student_id())
    grade_services.remove_student(student.get_student_id())


def remove_discipline_complex_handler(discipline_services, grade_services, discipline, list_of_deleted_grades):
    discipline_services.add_full_discipline(discipline)
    grade_services.add_multiple_grades_complex(list_of_deleted_grades)


def add_discipline_complex_handler(discipline_services, grade_services, discipline, disciplinee):
    discipline_services.remove_discipline(discipline.get_discipline_id())
    grade_services.remove_discipline(discipline.get_discipline_id())


class UndoComplexHandler(Enum):
    # DELETE_PERSON_COMPLEX = delete_person_complex_handler
    # ADD_PERSON_COMPLEX = add_person_complex_handler
    REMOVE_STUDENT_COMPLEX = remove_student_complex_handler
    ADD_STUDENT_COMPLEX = add_student_complex_handler
    REMOVE_DISCIPLINE_COMPLEX = remove_discipline_complex_handler
    ADD_DISCIPLINE_COMPLEX = add_discipline_complex_handler

    @staticmethod
    def get_opposite_handler(handler):
        if handler == UndoComplexHandler.REMOVE_STUDENT_COMPLEX:
            return UndoComplexHandler.ADD_STUDENT_COMPLEX
        if handler == UndoComplexHandler.REMOVE_DISCIPLINE_COMPLEX:
            return UndoComplexHandler.ADD_DISCIPLINE_COMPLEX


@dataclass
class UndoRedoComplexOperation:
    target_object1: object
    target_object2: object
    handler: object
    obj1: object
    obj2: object

    def perform_operation(self):
        self.handler(self.target_object1, self.target_object2,
                     self.obj1, self.obj2)

    def perform_reverse_operation(self):
        opposite_handler = UndoComplexHandler.get_opposite_handler(
            self.handler)
        opposite_handler(self.target_object1,
                         self.target_object2, self.obj1, self.obj2)
