from tkinter import *
from tkinter import messagebox

from domain.undoredo_operation import UndoHandler, UndoComplexHandler
from errors.exceptions import RepositoryError, UndoError, ValidationError


class StudentsGUI:
    """
      Implement the graphic user interface for add/list students
    """

    def __init__(self, student_services, discipline_services, grade_services, undo_redo_services):
        self.frame = None
        self.tk = Tk()
        self.services_student = student_services
        self.services_discipline = discipline_services
        self.services_grade = grade_services
        self.services_undo_redo = undo_redo_services

    def generate_all(self):
        self.services_grade.random_students_disciplines_grades()

    def run(self):
        # self.generate_all()
        self.tk.title("Students Register Management")

        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame
        lblp = Label(frame, text="Students manager")
        lblp.grid(row=0, column=0)
        '''
            ADD STUDENT
            ###########
        '''
        lbl_add_stud = Label(frame, text="Add student")
        lbl_add_stud.grid(row=1, column=0)

        lbl_add_id = Label(frame, text="ID:")
        lbl_add_id.grid(row=2, column=0)

        self.add_id_stud = Entry(frame, {})
        self.add_id_stud.grid(row=2, column=1)

        lbl_add_name = Label(frame, text="Name:")
        lbl_add_name.grid(row=2, column=2)

        self.add_name_student = Entry(frame, {})
        self.add_name_student.grid(row=2, column=3)

        self.add_btn = Button(frame, text="Add student",
                              command=self._add_student_gui)
        self.add_btn.grid(row=2, column=6)

        '''
        DELETE STUDENT
        ##############
        '''
        lbldelp = Label(frame, text="Delete student")
        lbldelp.grid(row=3, column=0)

        lbl_del_id = Label(frame, text="ID:")
        lbl_del_id.grid(row=4, column=0)

        self.delete_student = Entry(frame, {})
        self.delete_student.grid(row=4, column=1)

        self.del_btn = Button(frame, text="Delete",
                              command=self._remove_student_gui)
        self.del_btn.grid(row=4, column=6)
        '''
        UPDATE STUDENT
        #############
        '''
        lbl_up_p = Label(frame, text="Update student")
        lbl_up_p.grid(row=5, column=0)

        lbl_up_id = Label(frame, text="ID:")
        lbl_up_id.grid(row=6, column=0)

        self.update_student_id = Entry(frame, {})
        self.update_student_id.grid(row=6, column=1)

        lbl_up_name = Label(frame, text="Name:")
        lbl_up_name.grid(row=6, column=2)

        self.update_student_name = Entry(frame, {})
        self.update_student_name.grid(row=6, column=3)

        self.up_btn = Button(frame, text="Update",
                             command=self._update_student_gui)
        self.up_btn.grid(row=6, column=6)
        '''
        SEARCH STUDENTS
        ############
        '''
        lbl_sp = Label(frame, text="Search students: ")
        lbl_sp.grid(row=7, column=0)

        self.search_students = Entry(frame, {})
        self.search_students.grid(row=7, column=1)

        self.sp_btn = Button(frame, text="Search students",
                             command=self._search_students_gui)
        self.sp_btn.grid(row=7, column=6)
        '''
        ADD DISCIPLINE
        ############
        '''
        lbl_add_a = Label(frame, text="Add discipline")
        lbl_add_a.grid(row=8, column=0)

        lbl_add_id_a = Label(frame, text="ID:")
        lbl_add_id_a.grid(row=9, column=0)

        self.add_id_disc = Entry(frame, {})
        self.add_id_disc.grid(row=9, column=1)

        lbl_add_name = Label(frame, text="Name:")
        lbl_add_name.grid(row=9, column=2)

        self.add_name_disc = Entry(frame, {})
        self.add_name_disc.grid(row=9, column=3)

        self.add_btn = Button(frame, text="Add discipline",
                              command=self._add_discipline_gui)
        self.add_btn.grid(row=9, column=6)
        '''
        REMOVE DISCIPLINE
        ############
        '''
        lbldelp = Label(frame, text="Delete discipline")
        lbldelp.grid(row=10, column=0)

        lbl_del_id = Label(frame, text="ID:")
        lbl_del_id.grid(row=11, column=0)

        self.delete_discipline = Entry(frame, {})
        self.delete_discipline.grid(row=11, column=1)

        self.del_btn = Button(frame, text="Delete",
                              command=self._remove_discipline_gui)
        self.del_btn.grid(row=11, column=6)
        '''
        UPDATE DISCIPLINE
        ############
        '''
        lbl_up_p = Label(frame, text="Update discipline")
        lbl_up_p.grid(row=12, column=0)

        lbl_up_id = Label(frame, text="ID:")
        lbl_up_id.grid(row=13, column=0)

        self.update_discipline_id = Entry(frame, {})
        self.update_discipline_id.grid(row=13, column=1)

        lbl_up_name = Label(frame, text="Name:")
        lbl_up_name.grid(row=13, column=2)

        self.update_discipline_name = Entry(frame, {})
        self.update_discipline_name.grid(row=13, column=3)

        self.up_btn = Button(frame, text="Update",
                             command=self._update_discipline_gui)
        self.up_btn.grid(row=13, column=6)
        '''
        SEARCH DISCIPLINES
        ############
        '''
        lbl_sp = Label(frame, text="Search disciplines: ")
        lbl_sp.grid(row=14, column=0)

        self.search_disciplines = Entry(frame, {})
        self.search_disciplines.grid(row=14, column=1)

        self.sp_btn = Button(frame, text="Search disciplines",
                             command=self._search_disciplines_gui)
        self.sp_btn.grid(row=14, column=6)
        """
        ADD GRADE
        """
        lbl_add_p = Label(frame, text="Add grade")
        lbl_add_p.grid(row=15, column=0)

        lbl_add_id = Label(frame, text="Student ID:")
        lbl_add_id.grid(row=16, column=0)

        self.add_id_stud_g = Entry(frame, {})
        self.add_id_stud_g.grid(row=16, column=1)

        lbl_add_name = Label(frame, text="Discipline ID:")
        lbl_add_name.grid(row=16, column=2)

        self.add_id_disc_g = Entry(frame, {})
        self.add_id_disc_g.grid(row=16, column=3)

        lbl_grade_format = Label(frame, text="separated by one space")
        lbl_grade_format.grid(row=15, column=5)

        lbl_add_grade = Label(frame, text="Grade(s):")
        lbl_add_grade.grid(row=16, column=4)

        self.add_grade_value = Entry(frame, {})
        self.add_grade_value.grid(row=16, column=5)

        self.add_btn = Button(frame, text="Add", command=self._add_grade_gui)
        self.add_btn.grid(row=16, column=6)
        '''
        UNDO/REDO
        '''
        self.undo_btn = Button(
            frame, text="UNDO", command=self._undo_operation_gui)
        self.undo_btn.grid(row=18, column=2)

        self.redo_btn = Button(
            frame, text="REDO", command=self._redo_operation_gui)
        self.redo_btn.grid(row=18, column=4)
        '''
        DISPLAYS
        '''
        self.undo_btn = Button(
            frame, text="Show statistics", command=self._stats_gui)
        self.undo_btn.grid(row=18, column=3)

        self.list_people_btn = Button(
            frame, text="Show students", command=self._list_students)
        self.list_people_btn.grid(row=17, column=2)

        self.list_acts_btn = Button(
            frame, text="Show disciplines", command=self._list_disciplines)
        self.list_acts_btn.grid(row=17, column=3)

        self.list_acts_btn = Button(
            frame, text="Show grades", command=self._list_grades)
        self.list_acts_btn.grid(row=17, column=4)

        self.quit_btn = Button(
            frame, text="QUIT", fg="red", command=frame.quit)
        self.quit_btn.grid(row=18, column=6)

        frame.grid_rowconfigure(0, minsize=50)
        frame.grid_rowconfigure(7, minsize=50)
        frame.grid_rowconfigure(14, minsize=50)
        # frame.grid_rowconfigure(15, minsize=50)
        # frame.grid_rowconfigure(16, minsize=50)
        frame.grid_rowconfigure(17, minsize=50)
        frame.grid_rowconfigure(18, minsize=50)
        frame.grid_columnconfigure(6, minsize=100)
        # frame.grid_columnconfigure(10, minsize=100)
        self.tk.mainloop()

    def _add_student_gui(self):
        try:
            student_id = self.add_id_stud.get().strip()
            if not student_id.isnumeric():
                raise ValueError("id has to be number!")
            student_id = int(student_id)
            student_name = self.add_name_student.get().strip()
            self.services_student.add_student(student_id, student_name)
            messagebox.showinfo("Added", "Student added..")
            undo_redo_op = self.services_undo_redo.create_operation(
                self.services_student, UndoHandler.ADD_STUDENT, student_id, student_name)
            self.services_undo_redo.push(undo_redo_op)
        except ValidationError as ve:
            messagebox.showinfo("Error", "Validation Error:\n" + str(ve))
        except RepositoryError as re:
            messagebox.showinfo("Error", "Repository Error:\n" + str(re))
        except Exception as e:
            messagebox.showinfo("Error", "Error saving student - " + str(e))

    def _remove_student_gui(self):
        try:
            student_id = self.delete_student.get().strip()
            if not student_id.isnumeric():
                raise ValueError("id has to be number!")
            student_id = int(student_id)
            student = self.services_student.search_student_by_id(student_id)
            self.services_student.remove_student(student_id)
            list_of_deleted_grades = self.services_grade.get_grades_by_student_id(
                student_id)
            self.services_grade.remove_student(student_id)
            messagebox.showinfo("Deleted", "Student removed successfully!")
            undo_redo_cop = self.services_undo_redo.create_complex_operation(self.services_student, self.services_grade,
                                                                             UndoComplexHandler.REMOVE_STUDENT_COMPLEX,
                                                                             student, list_of_deleted_grades)
            self.services_undo_redo.push(undo_redo_cop)
        except ValidationError as ve:
            messagebox.showinfo("Error", "Validation Error:\n" + str(ve))
        except RepositoryError as re:
            messagebox.showinfo("Error", "Repository Error:\n" + str(re))
        except Exception as e:
            messagebox.showinfo("Error", "Error deleting student - " + str(e))

    def _update_student_gui(self):
        try:
            student_id = self.update_student_id.get().strip()
            if not student_id.isnumeric():
                raise ValueError("id has to be number!")
            student_id = int(student_id)
            student_name = self.update_student_name.get().strip()
            student = self.services_student.search_student_by_id(student_id)
            student_old_name = student.get_name()
            self.services_student.update_student(student_id, student_name)
            messagebox.showinfo("Update", "Student updated successfully")
            undo_redo_op = self.services_undo_redo.create_operation(
                self.services_student, UndoHandler.UPDATE_STUDENT, student_id, student_old_name, student_name)
            self.services_undo_redo.push(undo_redo_op)
        except ValidationError as ve:
            messagebox.showinfo("Error", "Validation Error:\n" + str(ve))
        except RepositoryError as re:
            messagebox.showinfo("Error", "Repository Error:\n" + str(re))
        except Exception as e:
            messagebox.showinfo("Error", "Error saving student - " + str(e))

    def _list_students(self):
        nr_of_students = self.services_student.nr_of_students()
        txt = ''
        txt += "The number of registered students is " + \
            str(nr_of_students) + "\n"
        if nr_of_students == 0:
            txt += "No students registered"
            return
        all_students = self.services_student.get_all_students()
        for student in all_students:
            txt += str(student) + "\n"
        messagebox.showinfo("List students", txt)

    def _search_students_gui(self):
        txt = ''
        value = self.search_students.get().strip().lower()
        if value == "":
            txt += "No input received"
        else:
            students = self.services_student.search_students(value)
            for student in students:
                txt += str(student) + "\n"
        messagebox.showinfo("Search results", txt)

    def _add_discipline_gui(self):
        try:
            discipline_id = self.add_id_disc.get().strip()
            if not discipline_id.isnumeric():
                raise ValueError("id has to be number!")
            discipline_id = int(discipline_id)
            name = self.add_name_disc.get().strip()
            self.services_discipline.add_discipline(discipline_id, name)
            messagebox.showinfo("Added", "Discipline added successfully!")
            undo_redo_op = self.services_undo_redo.create_operation(
                self.services_discipline, UndoHandler.ADD_DISCIPLINE, discipline_id, name)
            self.services_undo_redo.push(undo_redo_op)
        except ValidationError as ve:
            messagebox.showinfo("Error", "Validation Error:\n" + str(ve))
        except RepositoryError as re:
            messagebox.showinfo("Error", "Repository Error:\n" + str(re))
        except Exception as e:
            messagebox.showinfo("Error", "Error saving discipline - " + str(e))

    def _remove_discipline_gui(self):
        try:
            discipline_id = self.delete_discipline.get().strip()
            if not discipline_id.isnumeric():
                raise ValueError("id has to be number!")
            discipline_id = int(discipline_id)
            discipline = self.services_discipline.search_discipline_by_id(
                discipline_id)
            self.services_discipline.remove_discipline(discipline_id)
            list_of_deleted_grades = self.services_grade.get_grades_by_discipline_id(
                discipline_id)
            self.services_grade.remove_discipline(discipline_id)
            messagebox.showinfo("Deleted", "Discipline removed successfully!")
            undo_redo_cop = self.services_undo_redo.create_complex_operation(self.services_discipline, self.services_grade,
                                                                             UndoComplexHandler.REMOVE_DISCIPLINE_COMPLEX,
                                                                             discipline, list_of_deleted_grades)
            self.services_undo_redo.push(undo_redo_cop)
        except ValidationError as ve:
            messagebox.showinfo("Error", "Validation Error:\n" + str(ve))
        except RepositoryError as re:
            messagebox.showinfo("Error", "Repository Error:\n" + str(re))
        except Exception as e:
            messagebox.showinfo(
                "Error", "Error deleting discipline - " + str(e))

    def _update_discipline_gui(self):
        try:
            discipline_id = self.update_discipline_id.get().strip()
            if not discipline_id.isnumeric():
                raise ValueError("id has to be number!")
            discipline_id = int(discipline_id)
            discipline_name = self.update_discipline_name.get().strip()
            discipline = self.services_discipline.search_discipline_by_id(
                discipline_id)
            discipline_old_name = discipline.get_name()
            self.services_discipline.update_discipline(
                discipline_id, discipline_name)
            messagebox.showinfo("Updated", "Discipline updated successfully")
            undo_redo_op = self.services_undo_redo.create_operation(
                self.services_discipline, UndoHandler.UPDATE_DISCIPLINE, discipline_id, discipline_old_name, discipline_name)
            self.services_undo_redo.push(undo_redo_op)

        except ValidationError as ve:
            messagebox.showinfo("Error", "Validation Error:\n" + str(ve))
        except RepositoryError as re:
            messagebox.showinfo("Error", "Repository Error:\n" + str(re))
        except Exception as e:
            messagebox.showinfo("Error", "Error saving student - " + str(e))

    def _list_disciplines(self):
        nr_of_disciplines = self.services_discipline.nr_of_disciplines()
        txt = ''
        txt += "The number of registered disciplines is " + \
            str(nr_of_disciplines) + "\n"
        if nr_of_disciplines == 0:
            txt += "No disciplines registered"
            return
        all_disciplines = self.services_discipline.get_all_disciplines()
        for discipline in all_disciplines:
            txt += str(discipline) + "\n"
        messagebox.showinfo("List disciplines", txt)

    def _search_disciplines_gui(self):
        txt = ''
        value = self.search_disciplines.get().strip().lower()
        if value == "":
            txt += "No input received"
        else:
            disciplines = self.services_discipline.search_disciplines(value)
            for discipline in disciplines:
                txt += str(discipline) + "\n"
        messagebox.showinfo("Search results", txt)

    def _add_grade_gui(self):
        try:
            student_id = self.add_id_stud_g.get().strip()
            if not student_id.isnumeric():
                raise ValueError("student id has to be number!")
            student_id = int(student_id)
            discipline_id = self.add_id_disc_g.get().strip()
            if not discipline_id.isnumeric():
                raise ValueError("discipline id has to be number!")
            discipline_id = int(discipline_id)
            grades = []
            grades_str = self.add_grade_value.get().strip().split(" ")
            if grades_str == '':
                messagebox.showinfo("Error", "No grade received..")
                return
            for grade in grades_str:
                try:
                    grades.append(int(grade))
                except ValueError:
                    raise ValueError("invalid numerical grade(s)!")
            self.services_grade.add_multiple_grades(
                student_id, discipline_id, grades)
            messagebox.showinfo("Added", "Grade(s) added succesfully!")
            undo_redo_op = self.services_undo_redo.create_operation(
                self.services_grade, UndoHandler.ADD_GRADE, student_id, discipline_id, grades)
            self.services_undo_redo.push(undo_redo_op)
        except ValidationError as ve:
            messagebox.showinfo("Error", "Validation Error:\n" + str(ve))
        except RepositoryError as re:
            messagebox.showinfo("Error", "Repository Error:\n" + str(re))
        except Exception as e:
            messagebox.showinfo("Error", "Error saving student - " + str(e))

    def _list_grades(self):
        nr_of_grades = self.services_grade.nr_of_grades()
        txt = ''
        txt += "The number of registered grades is " + \
            str(nr_of_grades) + "\n"
        if nr_of_grades == 0:
            txt += "No disciplines registered"
            return
        all_grades = self.services_grade.get_all_grades()
        for grade in all_grades:
            txt += str(grade) + "\n"
        messagebox.showinfo("List grades", txt)

    def _stats_gui(self):
        students_failing = self.services_grade.students_failing()
        students_best = self.services_grade.students_top()
        disciplines_highest = self.services_grade.disciplines_highest()
        txt = ""
        txt += "Number of students failing at one or more disciplines is:" + \
            str(len(students_failing)) + "\n"
        for student in students_failing:
            txt += str(student) + "\n"
        txt += "\n"
        txt += "Students ordered by highest aggregated average:\n"
        for student in students_best:
            txt += str(student[0]) + \
                " with the aggregated average of: " + str(student[1]) + "\n"
        txt += "\n"
        txt += "Disciplines sorted in descending order of the average grade(s) received by all students:\n"
        for discipline in disciplines_highest:
            txt += str(discipline[0]) + \
                " with the aggregated average of: " + str(discipline[1]) + "\n"
        txt += "\n"
        messagebox.showinfo("Statistics", txt)

    def _undo_operation_gui(self):
        try:
            self.services_undo_redo.undo()
            messagebox.showinfo("Undo", "Operation undone")
        except RepositoryError as re:
            messagebox.showerror("Error", "Repository Error:\n" + str(re))
        except UndoError as ue:
            messagebox.showerror("Error", "UndoError:\n" + str(ue))

    def _redo_operation_gui(self):
        try:
            self.services_undo_redo.redo()
            messagebox.showinfo("Redo", "Operation redone!")
        except RepositoryError as re:
            messagebox.showerror("Error", "Repository Error:\n" + str(re))
        except UndoError as ue:
            messagebox.showerror("Error", "UndoError:\n" + str(ue))
