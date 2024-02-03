from domain.undoredo_operation import UndoRedoOperation, UndoRedoComplexOperation
from errors.exceptions import UndoError


class ServiceUndoRedo(object):
    def __init__(self, repo_undo_redo):
        # self.__repo_students = repo_students
        # self.__repo_disciplines = repo_disciplines
        # self.__repo_grades = repo_grades
        self.__repo_undo_redo = repo_undo_redo
        # self.__service_grades = service_grades

    def create_operation(self, target_object, handler, *args):
        return UndoRedoOperation(target_object, handler, args)

    def create_complex_operation(self, target_object1, target_object2, handler, obj1, obj2):
        return UndoRedoComplexOperation(target_object1, target_object2, handler, obj1, obj2)

    def push(self, undo_redo_op):
        self.__repo_undo_redo.push(undo_redo_op)

    def undo(self):
        if self.__repo_undo_redo.size() == 0:
            raise UndoError("No more undos!\n")
        undo_action = self.__repo_undo_redo.peek()
        self.__repo_undo_redo.pop()
        undo_action.perform_operation()

    def redo(self):
        if self.__repo_undo_redo.full():
            raise UndoError("No more redos!\n")
        self.__repo_undo_redo.pull()
        undo_action = self.__repo_undo_redo.peek()
        undo_action.perform_reverse_operation()
