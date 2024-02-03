class UndoRedoRepo:
    def __init__(self):
        self.__stack = []
        self.__stack_index = -1

    def push(self, undo_op):
        self.__stack = self.__stack[:self.__stack_index + 1]
        self.__stack.append(undo_op)
        self.__stack_index += 1

    def pop(self):
        self.__stack_index -= 1

    def pull(self):
        self.__stack_index += 1

    def peek(self):
        return self.__stack[self.__stack_index]

    def size(self):
        return self.__stack_index + 1

    def full(self):
        return self.__stack_index == len(self.__stack) - 1
