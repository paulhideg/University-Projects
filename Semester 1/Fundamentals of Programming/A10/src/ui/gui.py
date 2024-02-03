from tkinter import *
from tkinter import messagebox

from domain.useful_stuff.undoredo_operation import UndoHandler, UndoComplexHandler
from domain.useful_stuff.date import Date
from domain.useful_stuff.time import Time
from generators.activity_generator import ActivityGenerator
from generators.person_generator import PersonGenerator


class ActivityGUI:
    """
      Implement the graphic user interface for add/list students
    """

    def __init__(self, p_service, a_service, undo_redo_service):
        self.frame = None
        self.tk = Tk()
        self.p_service = p_service
        self.a_service = a_service
        self.undo_redo_service = undo_redo_service

    def generate_all(self):
        p_gen = PersonGenerator(self.p_service, self.undo_redo_service)
        p_gen.generate_people()
        a_gen = ActivityGenerator(self.a_service, self.p_service, self.undo_redo_service)
        a_gen.generate_activities()

    def run(self):
        # self.generate_all() # not ok to generate every time when working with files
        self.tk.title("Activity planner")

        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame
        lblp = Label(frame, text="People Manager")
        lblp.grid(row=0, column=0)
        '''
        ADD PERSON
        #################################################################################
        '''
        lbl_add_p = Label(frame, text="Add person")
        lbl_add_p.grid(row=1, column=0)

        lbl_add_id = Label(frame, text="ID:")
        lbl_add_id.grid(row=2, column=0)

        self.id_add = Entry(frame, {})
        self.id_add.grid(row=2, column=1)

        lbl_add_name = Label(frame, text="Name:")
        lbl_add_name.grid(row=2, column=2)

        self.name_add = Entry(frame, {})
        self.name_add.grid(row=2, column=3)

        lbl_phone_format = Label(frame, text="10 digits")
        lbl_phone_format.grid(row=1, column=5)

        lbl_add_phone = Label(frame, text="Phone number:")
        lbl_add_phone.grid(row=2, column=4)

        self.phone_add = Entry(frame, {})
        self.phone_add.grid(row=2, column=5)

        self.add_btn = Button(frame, text="Add", command=self._add_person_gui)
        self.add_btn.grid(row=2, column=6)
        '''
        DELETE PERSON
        #################################################################################
        '''
        lbldelp = Label(frame, text="Delete person")
        lbldelp.grid(row=3, column=0)

        lbl_del_id = Label(frame, text="ID:")
        lbl_del_id.grid(row=4, column=0)

        self.id_del = Entry(frame, {})
        self.id_del.grid(row=4, column=1)

        self.del_btn = Button(frame, text="Delete", command=self._remove_person_gui)
        self.del_btn.grid(row=4, column=6)
        '''
        UPDATE PERSON
        #################################################################################
        '''
        lbl_up_p = Label(frame, text="Update person")
        lbl_up_p.grid(row=5, column=0)

        lbl_up_id = Label(frame, text="ID:")
        lbl_up_id.grid(row=6, column=0)

        self.id_up = Entry(frame, {})
        self.id_up.grid(row=6, column=1)

        lbl_up_name = Label(frame, text="Name:")
        lbl_up_name.grid(row=6, column=2)

        self.name_up = Entry(frame, {})
        self.name_up.grid(row=6, column=3)

        lbl_phone_up_format = Label(frame, text="10 digits")
        lbl_phone_up_format.grid(row=5, column=5)

        lbl_up_phone = Label(frame, text="Phone number:")
        lbl_up_phone.grid(row=6, column=4)

        self.phone_up = Entry(frame, {})
        self.phone_up.grid(row=6, column=5)

        self.up_btn = Button(frame, text="Update", command=self._update_person_gui)
        self.up_btn.grid(row=6, column=6)

        lbla = Label(frame, text="Activity Manager")
        lbla.grid(row=7, column=0)
        '''
        ADD ACTIVITY
        #################################################################################
        '''
        lbl_add_a = Label(frame, text="Add activity")
        lbl_add_a.grid(row=8, column=0)

        lbl_add_id_a = Label(frame, text="ID:")
        lbl_add_id_a.grid(row=9, column=0)

        self.id_add_a = Entry(frame, {})
        self.id_add_a.grid(row=9, column=1)

        lbl_ids_add_format = Label(frame, text="comma separated")
        lbl_ids_add_format.grid(row=8, column=3)

        lbl_add_people_ids = Label(frame, text="People ids:")
        lbl_add_people_ids.grid(row=9, column=2)

        self.people_ids_add = Entry(frame, {})
        self.people_ids_add.grid(row=9, column=3)

        lbl_date_add_format = Label(frame, text="dd.mm.yyyy")
        lbl_date_add_format.grid(row=8, column=5)

        lbl_add_date = Label(frame, text="Date:")
        lbl_add_date.grid(row=9, column=4)

        self.date_add = Entry(frame, {})
        self.date_add.grid(row=9, column=5)

        lbl_time_add_format = Label(frame, text="hh:mm-hh:mm")
        lbl_time_add_format.grid(row=8, column=7)

        lbl_add_time = Label(frame, text="Time:")
        lbl_add_time.grid(row=9, column=6)

        self.time_add = Entry(frame, {})
        self.time_add.grid(row=9, column=7)

        lbl_add_desc = Label(frame, text="Description:")
        lbl_add_desc.grid(row=9, column=8)

        self.desc_add = Entry(frame, {})
        self.desc_add.grid(row=9, column=9)

        self.add_a_btn = Button(frame, text="Add", command=self._add_activity_gui)
        self.add_a_btn.grid(row=9, column=10)
        '''
        DELETE ACTIVITY
        #################################################################################
        '''
        lbl_del_a = Label(frame, text="Delete activity")
        lbl_del_a.grid(row=10, column=0)

        lbl_del_id_a = Label(frame, text="ID:")
        lbl_del_id_a.grid(row=11, column=0)

        self.id_del_a = Entry(frame, {})
        self.id_del_a.grid(row=11, column=1)

        self.del_a_btn = Button(frame, text="Delete", command=self._remove_activity_gui)
        self.del_a_btn.grid(row=11, column=10)
        '''
        UPDATE ACTIVITY
        #################################################################################
        '''
        lbl_up_a = Label(frame, text="Update activity")
        lbl_up_a.grid(row=12, column=0)

        lbl_up_id_a = Label(frame, text="ID:")
        lbl_up_id_a.grid(row=13, column=0)

        self.id_up_a = Entry(frame, {})
        self.id_up_a.grid(row=13, column=1)

        lbl_ids_up_format = Label(frame, text="comma separated")
        lbl_ids_up_format.grid(row=12, column=3)

        lbl_up_people_ids = Label(frame, text="People ids:")
        lbl_up_people_ids.grid(row=13, column=2)

        self.people_ids_up = Entry(frame, {})
        self.people_ids_up.grid(row=13, column=3)

        lbl_date_up_format = Label(frame, text="dd.mm.yyyy")
        lbl_date_up_format.grid(row=12, column=5)

        lbl_up_date = Label(frame, text="Date:")
        lbl_up_date.grid(row=13, column=4)

        self.date_up = Entry(frame, {})
        self.date_up.grid(row=13, column=5)

        lbl_time_up_format = Label(frame, text="hh:mm-hh:mm")
        lbl_time_up_format.grid(row=12, column=7)

        lbl_up_time = Label(frame, text="Time:")
        lbl_up_time.grid(row=13, column=6)

        self.time_up = Entry(frame, {})
        self.time_up.grid(row=13, column=7)

        lbl_up_desc = Label(frame, text="Description:")
        lbl_up_desc.grid(row=13, column=8)

        self.desc_up = Entry(frame, {})
        self.desc_up.grid(row=13, column=9)

        self.up_a_btn = Button(frame, text="Update", command=self._update_activity_gui)
        self.up_a_btn.grid(row=13, column=10)
        '''
        SEARCH PEOPLE
        '''
        lbl_sp = Label(frame, text="Search people: ")
        lbl_sp.grid(row=14, column=0)

        self.sp = Entry(frame, {})
        self.sp.grid(row=14, column=1)

        self.sp_btn = Button(frame, text="Search people", command=self._search_people_gui)
        self.sp_btn.grid(row=14, column=3)
        '''
        SEARCH ACTIVITIES
        '''
        lbl_sa = Label(frame, text="Search activities: ")
        lbl_sa.grid(row=15, column=0)

        self.sa = Entry(frame, {})
        self.sa.grid(row=15, column=1)

        self.sa_btn = Button(frame, text="Search activities", command=self._search_activities_gui)
        self.sa_btn.grid(row=15, column=3)
        '''
        DATE STATISTICS
        '''
        lbl_dss = Label(frame, text="Date statistics: ")
        lbl_dss.grid(row=16, column=0)

        lbl_ds = Label(frame, text="Date: ")
        lbl_ds.grid(row=17, column=0)

        self.ds = Entry(frame, {})
        self.ds.grid(row=17, column=1)

        self.ds_btn = Button(frame, text="Date statistics", command=self._date_statistics_gui)
        self.ds_btn.grid(row=17, column=3)
        '''
        BUSIEST DAYS
        '''
        lbl_bdd = Label(frame, text="Busiest days: ")
        lbl_bdd.grid(row=18, column=0)

        self.bd_btn = Button(frame, text="Busiest days", command=self._busiest_days_statistics_gui)
        self.bd_btn.grid(row=18, column=3)
        '''
        GIVEN PERSON STATISTICS
        '''
        lbl_pss = Label(frame, text="Person statistics: ")
        lbl_pss.grid(row=19, column=0)

        lbl_ps = Label(frame, text="Person ID: ")
        lbl_ps.grid(row=20, column=0)

        self.ps = Entry(frame, {})
        self.ps.grid(row=20, column=1)

        self.ps_btn = Button(frame, text="Person statistics", command=self._given_person_statistics_gui)
        self.ps_btn.grid(row=20, column=3)
        '''
        UNDO/REDO
        '''
        self.undo_btn = Button(frame, text="UNDO", command=self._undo_operation_gui)
        self.undo_btn.grid(row=21, column=4)

        self.redo_btn = Button(frame, text="REDO", command=self._redo_operation_gui)
        self.redo_btn.grid(row=21, column=6)
        '''
        DISPLAYS
        '''
        self.list_people_btn = Button(frame, text="Show people", command=self._list_people)
        self.list_people_btn.grid(row=25, column=4)

        self.list_acts_btn = Button(frame, text="Show activities", command=self._list_activities)
        self.list_acts_btn.grid(row=25, column=6)

        self.quit_btn = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.quit_btn.grid(row=26, column=5)

        frame.grid_rowconfigure(0, minsize=50)
        frame.grid_rowconfigure(7, minsize=50)
        frame.grid_rowconfigure(14, minsize=50)
        frame.grid_rowconfigure(15, minsize=50)
        frame.grid_rowconfigure(16, minsize=50)
        frame.grid_rowconfigure(17, minsize=50)
        frame.grid_rowconfigure(18, minsize=50)
        frame.grid_rowconfigure(19, minsize=50)
        frame.grid_rowconfigure(20, minsize=50)
        frame.grid_rowconfigure(21, minsize=50)
        frame.grid_rowconfigure(26, minsize=50)
        frame.grid_columnconfigure(6, minsize=100)
        frame.grid_columnconfigure(10, minsize=100)
        self.tk.mainloop()

    def _add_person_gui(self):
        try:
            p_id = self.id_add.get().strip()
            if not p_id.isnumeric():
                raise ValueError("id has to be number!")
            p_id = int(p_id)
            p_name = self.name_add.get().strip()
            phone = self.phone_add.get().strip()
            self.p_service.add_person(p_id, p_name, phone)
            undo_redo_op = self.undo_redo_service.create_operation(self.p_service, UndoHandler.ADD_PERSON, p_id, p_name,
                                                                   phone)
            self.undo_redo_service.push(undo_redo_op)
            messagebox.showinfo("Added", "Person saved..")
        except Exception as e:
            messagebox.showinfo("Error", "Error saving person - " + str(e))

    def _remove_person_gui(self):
        try:
            p_id = self.id_del.get().strip()
            if not p_id.isnumeric():
                raise ValueError("id has to be number!")
            p_id = int(p_id)
            person, activity_list = self.a_service.remove_person_from_activity(p_id)
            undo_redo_cop = self.undo_redo_service.create_complex_operation(self.p_service, self.a_service,
                                                                            UndoComplexHandler.DELETE_PERSON_COMPLEX,
                                                                            person, activity_list)
            self.undo_redo_service.push(undo_redo_cop)
            messagebox.showinfo("Deleted", "Person deleted...")
        except Exception as e:
            messagebox.showinfo("Error", "Error deleting person - " + str(e))

    def _update_person_gui(self):
        try:
            p_id = self.id_up.get().strip()
            if not p_id.isnumeric():
                raise ValueError("id has to be number!")
            p_id = int(p_id)
            person = self.p_service.search(p_id)
            p_name = self.name_up.get().strip()
            phone = self.phone_up.get().strip()
            self.p_service.update_person(p_id, p_name, phone)
            undo_redo_op = self.undo_redo_service.create_operation(self.p_service, UndoHandler.UPDATE_PERSON,
                                                                   person.person_id, person.name, person.phone_number,
                                                                   p_name, phone)
            self.undo_redo_service.push(undo_redo_op)
            messagebox.showinfo("Updated", "Person updated...")
        except Exception as e:
            messagebox.showinfo("Error", "Error updating person - " + str(e))

    def _list_people(self):
        people = self.p_service.get_all_people()
        txt = ''
        if not people:
            txt += 'No people.\n'
            return
        for p in people:
            txt += str(p)
            txt += "\n"
        messagebox.showinfo("List people", txt)

    def _add_activity_gui(self):
        try:
            a_id = self.id_add_a.get().strip()
            if not a_id.isnumeric():
                raise ValueError("id has to be number!\n")
            a_id = int(a_id)
            person_id_list = []
            str_ids = self.people_ids_add.get()
            str_ids = str_ids.split(',')
            for i in str_ids:
                p_id = i.strip()
                if not p_id.isnumeric():
                    raise ValueError("id has to be number!\n")
                person_id_list.append(int(p_id))
            str_date = self.date_add.get().strip()
            str_date = str_date.split('.')
            if len(str_date) != 3:
                raise ValueError("not a valid date\n")
            day = str_date[0].strip()
            month = str_date[1].strip()
            year = str_date[2].strip()
            if not day.isnumeric() or not month.isnumeric() or not year.isnumeric():
                raise ValueError("day, month and year should be numbers\n")
            date = Date(int(day), int(month), int(year))
            str_time = self.time_add.get().strip()
            str_time = str_time.split('-')
            if len(str_time) != 2:
                raise ValueError("not a valid time\n")
            start_h = str_time[0].split(':')[0].strip()
            start_m = str_time[0].split(':')[1].strip()
            end_h = str_time[1].split(':')[0].strip()
            end_m = str_time[1].split(':')[1].strip()
            if not start_h.isnumeric() or not start_m.isnumeric() or not end_h.isnumeric() or not end_m.isnumeric():
                raise ValueError("hours and minutes should be numbers\n")
            time = Time(int(start_h), int(start_m), int(end_h), int(end_m))
            description = self.desc_add.get().strip()
            self.a_service.add_activity(a_id, person_id_list, date, time, description)
            undo_redo_op = self.undo_redo_service.create_operation(self.a_service, UndoHandler.ADD_ACTIVITY,
                                                                   a_id, person_id_list, date, time, description)
            self.undo_redo_service.push(undo_redo_op)
            messagebox.showinfo("Added", "Activity added...")
        except Exception as e:
            messagebox.showinfo("Error", "Error adding activity - " + str(e))

    def _remove_activity_gui(self):
        try:
            a_id = self.id_del_a.get().strip()
            if not a_id.isnumeric():
                raise ValueError("id has to be number!\n")
            a_id = int(a_id)
            old_activity = self.a_service.search(a_id)
            self.a_service.remove_activity(a_id)
            undo_redo_op = self.undo_redo_service.create_operation(self.a_service, UndoHandler.DELETE_ACTIVITY,
                                                                   old_activity.activity_id, old_activity.person_id,
                                                                   old_activity.date, old_activity.time,
                                                                   old_activity.description)
            self.undo_redo_service.push(undo_redo_op)
            messagebox.showinfo("Deleted", "Activity deleted...")
        except Exception as e:
            messagebox.showinfo("Error", "Error deleting activity - " + str(e))

    def _update_activity_gui(self):
        try:
            a_id = self.id_up_a.get().strip()
            if not a_id.isnumeric():
                raise ValueError("id has to be number!\n")
            a_id = int(a_id)
            old_activity = self.a_service.search(a_id)
            person_id_list = []
            str_ids = self.people_ids_up.get()
            str_ids = str_ids.split(',')
            for i in str_ids:
                p_id = i.strip()
                if not p_id.isnumeric():
                    raise ValueError("id has to be number!\n")
                person_id_list.append(int(p_id))
            str_date = self.date_up.get().strip()
            str_date = str_date.split('.')
            if len(str_date) != 3:
                raise ValueError("not a valid date\n")
            day = str_date[0].strip()
            month = str_date[1].strip()
            year = str_date[2].strip()
            if not day.isnumeric() or not month.isnumeric() or not year.isnumeric():
                raise ValueError("day, month and year should be numbers\n")
            date = Date(int(day), int(month), int(year))
            str_time = self.time_up.get().strip()
            str_time = str_time.split('-')
            if len(str_time) != 2:
                raise ValueError("not a valid time\n")
            start_h = str_time[0].split(':')[0].strip()
            start_m = str_time[0].split(':')[1].strip()
            end_h = str_time[1].split(':')[0].strip()
            end_m = str_time[1].split(':')[1].strip()
            if not start_h.isnumeric() or not start_m.isnumeric() or not end_h.isnumeric() or not end_m.isnumeric():
                raise ValueError("hours and minutes should be numbers\n")
            time = Time(int(start_h), int(start_m), int(end_h), int(end_m))
            description = self.desc_up.get().strip()
            self.a_service.update_activity(a_id, person_id_list, date, time, description)
            undo_redo_op = self.undo_redo_service.create_operation(self.a_service, UndoHandler.UPDATE_ACTIVITY,
                                                                   old_activity.activity_id, old_activity.person_id,
                                                                   old_activity.date, old_activity.time,
                                                                   old_activity.description, person_id_list, date, time,
                                                                   description)
            self.undo_redo_service.push(undo_redo_op)
            messagebox.showinfo("Updated", "Activity updated...")
        except Exception as e:
            messagebox.showinfo("Error", "Error updating activity - " + str(e))

    def _list_activities(self):
        activities = self.a_service.get_all_activities()
        txt = ''
        if not activities:
            txt += 'No activities.\n'
            return
        for a in activities:
            txt += str(a)
            txt += "\n"
        messagebox.showinfo("List activities", txt)

    def _search_people_gui(self):
        try:
            string = self.sp.get().strip()
            result = self.p_service.search_people(string)
            txt = ''
            if not result:
                txt += 'Did not find anyone.\n'
            for r in result:
                txt += str(r)
                txt += '\n'
            messagebox.showinfo("Search people", txt)
        except Exception as e:
            messagebox.showinfo("Error", "Error searching - " + str(e))

    def _search_activities_gui(self):
        try:
            string = self.sa.get().strip()
            result = self.a_service.search_activities(string)
            txt = ''
            if not result:
                txt += 'Did not find any activity.\n'
            for r in result:
                txt += str(r)
                txt += '\n'
            messagebox.showinfo("Search activities", txt)
        except Exception as e:
            messagebox.showinfo("Error", "Error searching - " + str(e))

    def _date_statistics_gui(self):
        try:
            str_date = self.ds.get().strip()
            str_date = str_date.split('.')
            if len(str_date) != 3:
                raise ValueError("not a valid date\n")
            day = str_date[0].strip()
            month = str_date[1].strip()
            year = str_date[2].strip()
            if not day.isnumeric() or not month.isnumeric() or not year.isnumeric():
                raise ValueError("day, month and year should be numbers\n")
            date = Date(int(day), int(month), int(year))
            result = self.a_service.activities_for_date(date)
            txt = ''
            if not result:
                txt += 'No statistics for that date.\n'
                return
            for r in result:
                txt += str(r)
                txt += '\n'
            messagebox.showinfo("Date statistics", txt)
        except Exception as e:
            messagebox.showinfo("Error", "Statistics error - " + str(e))

    def _busiest_days_statistics_gui(self):
        try:
            result = self.a_service.busiest_days()
            txt = ''
            if not result:
                txt += 'No statistics.\n'
                return
            for r in result:
                txt += str(r)
                txt += '\n'
            messagebox.showinfo("Busiest days", txt)
        except Exception as e:
            messagebox.showinfo("Error", "Statistics error - " + str(e))

    def _given_person_statistics_gui(self):
        try:
            p_id = self.ps.get().strip()
            if not p_id.isnumeric():
                raise ValueError("id has to be number!")
            p_id = int(p_id)
            result = self.a_service.activities_with_a_person(p_id)
            txt = ''
            if not result:
                txt += 'No statistics with that person.\n'
                return
            for r in result:
                txt += str(r)
                txt += '\n'
            messagebox.showinfo("Statistics of person", txt)
        except Exception as e:
            messagebox.showinfo("Error", "Statistics error - " + str(e))

    def _undo_operation_gui(self):
        try:
            self.undo_redo_service.undo()
            messagebox.showinfo("Undo...", 'Operation undone!')
        except Exception as e:
            messagebox.showinfo("Error", "Undo error - " + str(e))

    def _redo_operation_gui(self):
        try:
            self.undo_redo_service.redo()
            messagebox.showinfo("Redo...", 'Operation redone!')
        except Exception as e:
            messagebox.showinfo("Error", "Redo error - " + str(e))
