from domain.useful_stuff.undoredo_operation import UndoHandler, UndoComplexHandler
from errors.exceptions import RepositoryException, ValidatorException, UndoException
from generators.activity_generator import ActivityGenerator
from generators.person_generator import PersonGenerator
from domain.useful_stuff.time import Time
from domain.useful_stuff.date import Date


class Console:
    def __init__(self, p_service, a_service, undo_redo_service):
        self.p_service = p_service
        self.a_service = a_service
        self.undo_redo_service = undo_redo_service

    def print_help(self):
        print("'1p' add person")
        print("'2p' remove person")
        print("'3p' update person")
        print("'4p' list person")
        print("'1a' add activity")
        print("'2a' remove activity")
        print("'3a' update activity")
        print("'4a' list activity")
        print("'sp' search people using name or phone number")
        print("'sa' search activities using date/time or description")
        print("'1stats' activities for a given date. List the activities for a given date, in the order of their "
              "start time")
        print("'2stats' busiest days. This will provide the list of upcoming dates with activities, sorted in "
              "descending order of the free time in that day (all intervals with no activities)")
        print("'3stats' activities with a given person. List all upcoming activities to which a given person "
              "will participate.")
        print("'undo' undoes last performed operation")
        print("'redo' redoes last performed operation")
        print("'exit' exit application")

    def generate_all(self):
        p_gen = PersonGenerator(self.p_service, self.undo_redo_service)
        p_gen.generate_people()
        a_gen = ActivityGenerator(self.a_service, self.p_service, self.undo_redo_service)
        a_gen.generate_activities()

    def add_person_ui(self):
        p_id = input("Enter person id: ")
        if not p_id.isnumeric():
            raise ValueError("id has to be number!")
        p_id = int(p_id)
        p_name = input("Enter person name: ")
        phone = input("Enter person phone: ")
        self.p_service.add_person(p_id, p_name, phone)
        print("Added person with success.")
        undo_redo_op = self.undo_redo_service.create_operation(self.p_service, UndoHandler.ADD_PERSON, p_id, p_name,
                                                               phone)
        self.undo_redo_service.push(undo_redo_op)

    def remove_person_ui(self):
        p_id = input("Enter id of person you want removed: ")
        if not p_id.isnumeric():
            raise ValueError("id has to be number!")
        person, activity_list = self.a_service.remove_person_from_activity(int(p_id))
        print("Removed person with success.")
        undo_redo_cop = self.undo_redo_service.create_complex_operation(self.p_service, self.a_service,
                                                                        UndoComplexHandler.DELETE_PERSON_COMPLEX,
                                                                        person, activity_list)
        self.undo_redo_service.push(undo_redo_cop)

    def update_person_ui(self):
        p_id = input("Enter person id to update: ")
        if not p_id.isnumeric():
            raise ValueError("id has to be number!")
        p_id = int(p_id)
        person = self.p_service.search(p_id)
        p_name = input("Enter person name to update: ")
        phone = input("Enter person phone to update: ")
        self.p_service.update_person(p_id, p_name, phone)
        print("Updated person with success.")
        undo_redo_op = self.undo_redo_service.create_operation(self.p_service, UndoHandler.UPDATE_PERSON,
                                                               person.person_id, person.name, person.phone_number,
                                                               p_name, phone)
        self.undo_redo_service.push(undo_redo_op)

    def list_person_ui(self):
        p_list = self.p_service.get_all_people()
        if not p_list:
            print("List is empty. :(\n")
        else:
            for p in p_list:
                print(p)

    def add_activity_ui(self):
        # activity_id, person_id - list, date, time, description
        a_id = input("Enter activity id: ")
        if not a_id.isnumeric():
            raise ValueError("id has to be number!\n")
        a_id = int(a_id)
        n = input("Enter the number of people involved in this activity: ")
        if not n.isnumeric():
            raise ValueError("that's not a number!\n")
        person_id_list = []
        for i in range(int(n)):
            p_id = input(f"Enter id for person {i}: ")
            if not p_id.isnumeric():
                raise ValueError("id has to be number!\n")
            person_id_list.append(int(p_id))
        day = input("Enter the day: ")
        month = input("Enter the month: ")
        year = input("Enter the year: ")
        if not day.isnumeric() or not month.isnumeric() or not year.isnumeric():
            raise ValueError("day, month and year should be numbers\n")
        date = Date(int(day), int(month), int(year))
        start_h = input("Enter starting hour: ")
        start_m = input("Enter starting minute: ")
        end_h = input("Enter ending hour: ")
        end_m = input("Enter ending minute: ")
        if not start_h.isnumeric() or not start_m.isnumeric() or not end_h.isnumeric() or not end_m.isnumeric():
            raise ValueError("hours and minutes should be numbers\n")
        time = Time(int(start_h), int(start_m), int(end_h), int(end_m))
        description = input("Enter the description of the activity: ")
        self.a_service.add_activity(a_id, person_id_list, date, time, description)
        print("Added activity with success.")
        undo_redo_op = self.undo_redo_service.create_operation(self.a_service, UndoHandler.ADD_ACTIVITY,
                                                               a_id, person_id_list, date, time, description)
        self.undo_redo_service.push(undo_redo_op)

    def remove_activity_ui(self):
        a_id = input("Enter id of activity you want removed: ")
        if not a_id.isnumeric():
            raise ValueError("id has to be number!")
        old_activity = self.a_service.search(int(a_id))
        self.a_service.remove_activity(int(a_id))
        print("Removed activity with success.")
        undo_redo_op = self.undo_redo_service.create_operation(self.a_service, UndoHandler.DELETE_ACTIVITY,
                                                               old_activity.activity_id, old_activity.person_id,
                                                               old_activity.date, old_activity.time,
                                                               old_activity.description)
        self.undo_redo_service.push(undo_redo_op)

    def update_activity_ui(self):
        a_id = input("Enter activity id for update: ")
        if not a_id.isnumeric():
            raise ValueError("id has to be number!\n")
        a_id = int(a_id)
        old_activity = self.a_service.search(a_id)
        n = input("Enter the updated number of people involved in this activity: ")
        if not n.isnumeric():
            raise ValueError("that's not a number!\n")
        person_id_list = []
        for i in range(int(n)):
            p_id = input(f"Enter updated id for person {i}: ")
            if not p_id.isnumeric():
                raise ValueError("id has to be number!\n")
            person_id_list.append(int(p_id))
        day = input("Enter the updated day: ")
        month = input("Enter the updated month: ")
        year = input("Enter the updated year: ")
        if not day.isnumeric() or not month.isnumeric() or not year.isnumeric():
            raise ValueError("day, month and year should be numbers\n")
        date = Date(int(day), int(month), int(year))
        start_h = input("Enter updated starting hour: ")
        start_m = input("Enter updated starting minute: ")
        end_h = input("Enter updated ending hour: ")
        end_m = input("Enter updated ending minute: ")
        if not start_h.isnumeric() or not start_m.isnumeric() or not end_h.isnumeric() or not end_m.isnumeric():
            raise ValueError("hours and minutes should be numbers\n")
        time = Time(int(start_h), int(start_m), int(end_h), int(end_m))
        description = input("Enter the updated description of the activity: ")
        self.a_service.update_activity(a_id, person_id_list, date, time, description)
        print("Updated activity with success.")
        undo_redo_op = self.undo_redo_service.create_operation(self.a_service, UndoHandler.UPDATE_ACTIVITY,
                                                               old_activity.activity_id, old_activity.person_id,
                                                               old_activity.date, old_activity.time,
                                                               old_activity.description, person_id_list, date, time,
                                                               description)
        self.undo_redo_service.push(undo_redo_op)

    def list_activity_ui(self):
        a_list = self.a_service.get_all_activities()
        if not a_list:
            print("List is empty. :(\n")
        else:
            for a in a_list:
                print(a)

    def search_people_ui(self):
        string = input("Enter either name or phone partially: ")
        result = self.p_service.search_people(string)
        if not result:
            print(f"Did not find anyone searching for {string}\n")
        for r in result:
            print(r)

    def search_activities_ui(self):
        string = input("Enter either date, time or description partially: ")
        result = self.a_service.search_activities(string)
        if not result:
            print(f"Did not find any activity searching for {string}\n")
        for r in result:
            print(r)

    def date_statistics(self):
        day = input("Enter the day: ")
        month = input("Enter the month: ")
        year = input("Enter the year: ")
        if not day.isnumeric() or not month.isnumeric() or not year.isnumeric():
            raise ValueError("day, month and year should be numbers\n")
        date = Date(int(day), int(month), int(year))
        result = self.a_service.activities_for_date(date)
        if not result:
            print("List is emptyyyyy.")
            return
        for r in result:
            print(r)

    def busiest_days_statistics(self):
        result = self.a_service.busiest_days()
        if not result:
            print("List is emptyyyyy.")
            return
        for r in result:
            print(r)

    def given_person_statistics(self):
        id = input("Enter id of person you want statistics of: ")
        if not id.isnumeric():
            raise ValueError("id has to be number!\n")
        id = int(id)
        result = self.a_service.activities_with_a_person(id)
        if not result:
            print("List is emptyyyyy.")
            return
        for r in result:
            print(r)

    def undo_operation_ui(self):
        self.undo_redo_service.undo()
        print("Operation undone!")

    def redo_operation_ui(self):
        self.undo_redo_service.redo()
        print("Operation redone!")

    def run(self):
        # self.generate_all() # generator should run only once for file repos
        cmd_dict = {'h': self.print_help, '1p': self.add_person_ui, '2p': self.remove_person_ui,
                    '3p': self.update_person_ui, '4p': self.list_person_ui, '1a': self.add_activity_ui,
                    '2a': self.remove_activity_ui, '3a': self.update_activity_ui, '4a': self.list_activity_ui,
                    'sp': self.search_people_ui, 'sa': self.search_activities_ui, '1stats': self.date_statistics,
                    '2stats': self.busiest_days_statistics, '3stats': self.given_person_statistics,
                    'undo': self.undo_operation_ui, 'redo': self.redo_operation_ui}
        print("Press 'h' for help...")
        while True:
            cmd = input("Enter command: ")
            if cmd in cmd_dict:
                try:
                    cmd_dict[cmd]()
                except RepositoryException as re:
                    print(re)
                except ValidatorException as ve:
                    print(ve)
                except ValueError as ee:
                    print(ee)
                except UndoException as ue:
                    print(ue)
            elif cmd == 'h':
                self.print_help()
            elif cmd == 'exit':
                print("Bye.")
                return
            else:
                print("Command not implemented.")
