from services import Services
from domain import Student
from tests import test_add_student
from copy import deepcopy


class UI:
    def __init__(self, service):
        self._service = service
        self._history = [Student.sample_students()]

    @staticmethod
    def print_menu():
        print("Welcome to the menu:")
        print("Enter 'add' to add a new student")
        print("Enter 'list' to list the students")
        print("Enter 'filter' to filter the list so that it contains only students in a certain group")
        print("Enter 'undo' to undo the last operation that modified program data")
        print("Or enter 'exit' to exit the program!")

    def ui_add_student(self):
        id = input("Enter the id of the student:")
        try:
            id = int(id)
        except ValueError:
            print("Invalid id")
            return
        if id < 1:
            print("Student id can't be lower than 1")
            return
        name = input("Enter the name of the student:")
        group = input("Enter the group in which the student is:")
        try:
            group = int(group)
        except ValueError:
            print("Invalid amount")
            return
        if group < 1:
            print("Group must be greater than 0")
            return
        try:
            self._service.add_student(Student(id, name, group))
            self._history.append(self._service.students)
            print("Student added successfully")
        except Exception as e:
            print(e)

    def ui_list_students(self):
        print("So far there are " + str(len(self._service.students)) +
              " students registered")
        for student in self._service.students:
            print(student)

    def ui_filter_students(self):
        group = input("Enter the desired group:")
        try:
            group = int(group)
        except ValueError:
            print("Invalid group")
        self._service.filter_student(group)
        self._history.append(self._service.students)
        print("Students have been filtered successfully")

    def start_menu(self):
        UI.print_menu()
        while True:
            cmd = input(">>>")
            self._service.students = deepcopy(self._history[-1])
            if cmd == "add":
                self.ui_add_student()
            elif cmd == "list":
                self.ui_list_students()
            elif cmd == "filter":
                self.ui_filter_students()
            elif cmd == "undo":
                if len(self._history) == 1:
                    print("You cannot undo anymore")
                else:
                    self._history.pop()
                    print("You have undone the operation")
            elif cmd == "exit":
                return
            else:
                print("Invalid command")


serv = Services()
test_add_student(serv)
ui = UI(serv)
ui.start_menu()
