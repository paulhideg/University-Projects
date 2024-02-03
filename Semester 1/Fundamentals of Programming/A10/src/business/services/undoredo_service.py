from domain.useful_stuff.undoredo_operation import UndoRedoOperation, UndoRedoComplexOperation
from errors.exceptions import UndoException


class UndoRedoService:
    def __init__(self, undo_repo):
        self.__undo_repo = undo_repo

    def create_operation(self, target_object, handler, *args):
        return UndoRedoOperation(target_object, handler, args)

    def create_complex_operation(self, target_object1, target_object2, handler, obj1, obj2):
        return UndoRedoComplexOperation(target_object1, target_object2, handler, obj1, obj2)

    def push(self, undo_redo_op):
        self.__undo_repo.push(undo_redo_op)

    def undo(self):
        if self.__undo_repo.size() == 0:
            raise UndoException("No more undos!\n")
        undo_action = self.__undo_repo.peek()
        self.__undo_repo.pop()
        undo_action.perform_operation()

    def redo(self):
        if self.__undo_repo.full():
            raise UndoException("No more redos!\n")
        self.__undo_repo.pull()
        undo_action = self.__undo_repo.peek()
        undo_action.perform_reverse_operation()


'''
class UndoManager:
    __undo_operations = []

    @staticmethod
    def register_operation(target_object, handler, *args):
        UndoManager.__undo_operations.append(UndoOperation(target_object, handler, args))

    @staticmethod
    def undo():
        if not UndoManager.__undo_operations:
            raise UndoException("No more undos!\n")
        undo_operation = UndoManager.__undo_operations.pop()
        undo_operation.handler(undo_operation.target_object, *undo_operation.args)
'''
