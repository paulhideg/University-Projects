from domain.undoredo_operation import UndoHandler, UndoComplexHandler
from errors.exceptions import RepositoryError, UndoError, ValidationError


class UI(object):
    def __init__(self, services_student, services_discipline, services_grade, services_undo_redo):
        self.services_student = services_student
        self.services_discipline = services_discipline
        self.services_grade = services_grade
        self.services_undo_redo = services_undo_redo

    def __run_students_menu(self):
        print("Students menu")
        while True:
            print("")
            print("Press 1 for adding a student")
            print("Press 2 for removing a student")
            print("Press 3 for updating a student")
            print("Press 4 for listing all students")
            print("Press 5 for searching a student by id / name")
            print("Or input exit in order to quit the students menu")
            cmd = input(">>>>>>")
            if cmd == "exit":
                print("Returned to the main menu...")
                return
            elif cmd == "":
                continue
            elif cmd == "1":
                try:
                    self.__ui_add_student()
                except ValidationError as ve:
                    print("Validation Error:\n" + str(ve))
                except RepositoryError as re:
                    print("Repository Error:\n" + str(re))
            elif cmd == "2":
                try:
                    self.__ui_remove_student()
                except ValidationError as ve:
                    print("Validation Error:\n" + str(ve))
                except RepositoryError as re:
                    print("Repository Error:\n" + str(re))
            elif cmd == "3":
                try:
                    self.__ui_update_student()
                except ValidationError as ve:
                    print("Validation Error:\n" + str(ve))
                except RepositoryError as re:
                    print("Repository Error:\n" + str(re))
            elif cmd == "4":
                self.__ui_list_students()
            elif cmd == "5":
                self.__ui_search_students()
            else:
                print("Invalid commmand")

    def __ui_add_student(self):
        print("Add a student:")
        try:
            student_id = int(input("Type the student's id:"))
        except ValueError:
            print("Invalid numerical id")
            return
        name = input("Type the student's name:")
        self.services_student.add_student(student_id, name)
        print("Student added successfully!")
        undo_redo_op = self.services_undo_redo.create_operation(
            self.services_student, UndoHandler.ADD_STUDENT, student_id, name)
        self.services_undo_redo.push(undo_redo_op)

    def __ui_remove_student(self):
        print("Remove a student:")
        try:
            student_id = int(input("Type the student's id:"))
        except ValueError:
            print("Invalid numerical id")
            return
        student = self.services_student.search_student_by_id(student_id)
        self.services_student.remove_student(student_id)
        list_of_deleted_grades = self.services_grade.get_grades_by_student_id(
            student_id)
        self.services_grade.remove_student(student_id)
        print("Student removed successfully!")
        undo_redo_cop = self.services_undo_redo.create_complex_operation(self.services_student, self.services_grade,
                                                                         UndoComplexHandler.REMOVE_STUDENT_COMPLEX,
                                                                         student, list_of_deleted_grades)
        self.services_undo_redo.push(undo_redo_cop)

    def __ui_update_student(self):
        print("Update a student:")
        try:
            student_id = int(input(
                "Type the id of the student you want to update:"))
        except ValueError:
            print("Invalid numerical id")
            return
        student_name = input("Type the student's new name:")
        student = self.services_student.search_student_by_id(student_id)
        student_old_name = student.get_name()
        self.services_student.update_student(student_id, student_name)
        print("Student updated successfully")
        undo_redo_op = self.services_undo_redo.create_operation(
            self.services_student, UndoHandler.UPDATE_STUDENT, student_id, student_old_name, student_name)
        self.services_undo_redo.push(undo_redo_op)

    def __ui_list_students(self):
        nr_of_students = self.services_student.nr_of_students()
        print("The number of registered students is " + str(nr_of_students))
        if nr_of_students == 0:
            print("No students registered")
            return
        all_students = self.services_student.get_all_students()
        for student in all_students:
            print(student)

    def __ui_search_students(self):
        print("Search for a student by typing an id or a name:")
        value = input("Type the id / name:").strip().lower()
        if value == "":
            print("No input received")
        else:
            students = self.services_student.search_students(value)
            for student in students:
                print(student)

    def __run_disciplines_menu(self):
        print("Disciplines menu")
        while True:
            print("")
            print("Press 1 for adding a discipline")
            print("Press 2 for removing a discipline")
            print("Press 3 for updating a discipline")
            print("Press 4 for listing all disciplines")
            print("Press 5 for searching a discipline by id / name")
            print("Or input exit in order to quit the disciplines menu")
            cmd = input(">>>>>>")
            if cmd == "exit":
                print("Returned to the main menu...")
                return
            elif cmd == "":
                continue
            elif cmd == "1":
                try:
                    self.__ui_add_discipline()
                except ValidationError as ve:
                    print("Validation Error:\n" + str(ve))
                except RepositoryError as re:
                    print("Repository Error:\n" + str(re))
            elif cmd == "2":
                try:
                    self.__ui_remove_discipline()
                except ValidationError as ve:
                    print("Validation Error:\n" + str(ve))
                except RepositoryError as re:
                    print("Repository Error:\n" + str(re))
            elif cmd == "3":
                try:
                    self.__ui_update_discipline()
                except ValidationError as ve:
                    print("Validation Error:\n" + str(ve))
                except RepositoryError as re:
                    print("Repository Error:\n" + str(re))
            elif cmd == "4":
                self.__ui_list_disciplines()
            elif cmd == "5":
                self.__ui_search_disciplines()
            else:
                print("Invalid commmand")

    def __ui_add_discipline(self):
        print("Add a discipline:")
        try:
            discipline_id = int(input("Type the discipline's id:"))
        except ValueError:
            print("Invalid numerical id")
            return
        name = input("Type the discipline's name:")
        self.services_discipline.add_discipline(discipline_id, name)
        print("Discipline added successfully!")
        undo_redo_op = self.services_undo_redo.create_operation(
            self.services_discipline, UndoHandler.ADD_DISCIPLINE, discipline_id, name)
        self.services_undo_redo.push(undo_redo_op)

    def __ui_remove_discipline(self):
        print("Remove a discipline:")
        try:
            discipline_id = int(input("Type the discipline's id:"))
        except ValueError:
            print("Invalid numerical id")
            return
        discipline = self.services_discipline.search_discipline_by_id(
            discipline_id)
        self.services_discipline.remove_discipline(discipline_id)
        list_of_deleted_grades = self.services_grade.get_grades_by_discipline_id(
            discipline_id)
        self.services_grade.remove_discipline(discipline_id)
        print("Discipline removed successfully!")
        undo_redo_cop = self.services_undo_redo.create_complex_operation(self.services_discipline, self.services_grade,
                                                                         UndoComplexHandler.REMOVE_DISCIPLINE_COMPLEX,
                                                                         discipline, list_of_deleted_grades)
        self.services_undo_redo.push(undo_redo_cop)

    def __ui_update_discipline(self):
        print("Update a discipline:")
        try:
            discipline_id = int(input(
                "Type the id of the discipline you want to update:"))
        except ValueError:
            print("Invalid numerical id")
            return
        discipline_name = input("Type the discipline's new name:")
        discipline = self.services_discipline.search_discipline_by_id(
            discipline_id)
        discipline_old_name = discipline.get_name()
        self.services_discipline.update_discipline(
            discipline_id, discipline_name)
        print("Discipline updated successfully")
        undo_redo_op = self.services_undo_redo.create_operation(
            self.services_discipline, UndoHandler.UPDATE_DISCIPLINE, discipline_id, discipline_old_name, discipline_name)
        self.services_undo_redo.push(undo_redo_op)

    def __ui_list_disciplines(self):
        nr_of_disciplines = self.services_discipline.nr_of_disciplines()
        print("The number of registered disciplines is " + str(nr_of_disciplines))
        if nr_of_disciplines == 0:
            print("No disciplines registered")
            return
        all_disciplines = self.services_discipline.get_all_disciplines()
        for discipline in all_disciplines:
            print(discipline)

    def __ui_search_disciplines(self):
        print("Search for a discipline by typing an id or a name:")
        value = input("Type the id / name:").strip().lower()
        if value == "":
            print("No input received")
        else:
            disciplines = self.services_discipline.search_disciplines(value)
            for discipline in disciplines:
                print(discipline)

    def __run_grades_menu(self):
        print("Grades menu")
        while True:
            print("Input 1 for adding a grade")
            print("Input 2 to list all the grades")
            print("Or input exit in order to quit the grades menu")
            cmd = input(">>>>>>")
            if cmd == "exit":
                print("Returned to the main menu...")
                return
            elif cmd == "":
                continue
            elif cmd == "1":
                try:
                    self.__ui__add_grade()
                except ValidationError as ve:
                    print("Validation Error:\n" + str(ve))
                except RepositoryError as re:
                    print("Repository Error:\n" + str(re))
            elif cmd == "2":
                self.__ui_list_grades()
            else:
                print("Invalid commmand")

    def __ui__add_grade(self):
        print("Add a grade:")
        try:
            student_id = int(input("Type the student's id:"))
        except ValueError:
            print("Invalid numerical student id")
            return
        try:
            discipline_id = int(input("Type the discipline's id:"))
        except ValueError:
            print("Invalid numerical discipline id")
            return
        # try:
        #     grade = int(input("Type the grade:"))
        # except:
        #     print("Invalid numerical grade")
        #     return
        # self.__services_grade.add_grade(student_id, discipline_id, grade)
        # print("Grade added successfully!")
        grades = []
        grades_str = input("Type grades separated by space :").split(" ")
        try:
            for grade in grades_str:
                try:
                    grades.append(int(grade))
                except ValueError:
                    raise ValueError
            self.services_grade.add_multiple_grades(
                student_id, discipline_id, grades)
            print("Grade(s) added succesfully!")
        except ValueError:
            print("invalid numerical grade(s)!")
        undo_redo_op = self.services_undo_redo.create_operation(
            self.services_grade, UndoHandler.ADD_GRADE, student_id, discipline_id, grades)
        self.services_undo_redo.push(undo_redo_op)

    def __ui_list_grades(self):
        nr_of_grades = self.services_grade.nr_of_grades()
        print("The number of registered grades is " + str(nr_of_grades))
        if nr_of_grades == 0:
            print("No grades registered")
            return
        all_grades = self.services_grade.get_all_grades()
        for grade in all_grades:
            print(grade)

    def __run_stats_menu(self):
        students_failing = self.services_grade.students_failing()
        print("Number of students failing at one or more disciplines is:" +
              str(len(students_failing)) + "\n")
        for student in students_failing:
            print(student)
        print("\n")
        students_best = self.services_grade.students_top()
        print("Students ordered by highest aggregated average:\n")
        for student in students_best:
            print(
                str(student[0]) + " with the aggregated average of: " + str(student[1]))
        print("\n")
        print("Disciplines sorted in descending order of the average grade(s) received by all students:\n")
        disciplines_highest = self.services_grade.disciplines_highest()
        for discipline in disciplines_highest:
            print(
                str(discipline[0]) + " with the aggregated average of: " + str(discipline[1]))
        print("\n")

    def __run_undo(self):
        try:
            self.__ui_undo()
        except RepositoryError as re:
            print("Repository Error:\n" + str(re))
        except UndoError as ue:
            print("UndoError:\n" + str(ue))

    def __ui_undo(self):
        self.services_undo_redo.undo()
        print("Operation undone!\n")

    def __run_redo(self):
        try:
            self.__ui_redo()
        except RepositoryError as re:
            print("Repository Error:\n" + str(re))
        except UndoError as ue:
            print("UndoError:\n" + str(ue))

    def __ui_redo(self):
        self.services_undo_redo.redo()
        print("Operation redone!\n")

    def run(self):
        self.services_grade.random_students_disciplines_grades()
        print("Welcome to the main menu")
        while True:
            print("Press 1 to get to the students menu")
            print("Press 2 to get to the disciplines menu")
            print("Press 3 to get to the grades menu")
            print("Press 4 for displaying statistics")
            print("Input 'undo' in order to undo the last operation")
            print("Input 'redo' in order to redo the last operation")
            print("Or input exit in order to quit the program")
            cmd = input(">>>>")
            if cmd == "exit":
                print("Program closed...")
                return
            elif cmd == "":
                continue
            elif cmd == "1":
                self.__run_students_menu()
            elif cmd == "2":
                self.__run_disciplines_menu()
            elif cmd == "3":
                self.__run_grades_menu()
            elif cmd == "4":
                self.__run_stats_menu()
            elif cmd == "undo":
                self.__run_undo()
            elif cmd == "redo":
                self.__run_redo()
            else:
                print("Invalid command")
