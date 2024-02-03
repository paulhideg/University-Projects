import json
import pickle
import unittest
from datetime import datetime, date

from jsonic import serialize, deserialize

from business.services.activity_service import ActivityService
from business.services.person_service import PersonService
from business.services.undoredo_service import UndoRedoService
from domain.entities.person import Person
from domain.entities.activity import Activity
from domain.useful_stuff.time import Time
from domain.useful_stuff.date import Date
from domain.useful_stuff.undoredo_operation import UndoHandler, UndoComplexHandler
from errors.exceptions import ValidatorException, RepositoryException, UndoException
from generators.activity_generator import ActivityGenerator
from generators.person_generator import PersonGenerator
from infrastructure.binary_repositories.binary_activity_repo import BinaryActivityRepository
from infrastructure.binary_repositories.binary_person_repo import BinaryPersonRepository
from infrastructure.data_access_entities import PersonDataAccess, ActivityDataAccess
from infrastructure.file_repositories.file_activity_repo import FileActivityRepository
from infrastructure.file_repositories.file_person_repo import FilePersonRepository
from infrastructure.json_repositories.json_activity_repo import JSONActivityRepository
from infrastructure.json_repositories.json_person_repo import JSONPersonRepository
from infrastructure.repositories.activity_repo import ActivityRepository
from infrastructure.repositories.person_repo import PersonRepository
from infrastructure.repositories.undoredo_repo import UndoRedoRepo
from validation.activity_validator import ActivityValidator, DateValidator
from validation.person_validator import PersonValidator


class Test(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_entity_person(self):
        # test creation
        person_id = 1
        name = "n1"
        phone_number = "0123"
        person = Person(person_id, name, phone_number)
        self.assertEqual(person.person_id, 1)
        self.assertEqual(person.name, "n1")
        self.assertEqual(person.phone_number, "0123")
        person.name = "set name"
        person.phone_number = "999"
        self.assertEqual(person.name, "set name")
        self.assertEqual(person.phone_number, "999")
        # test __eq__
        person1 = Person(1, "n2", "3210")
        self.assertEqual(person, person1)
        # test __str__
        self.assertEqual(str(person), "1: Name: set name, Phone: 999\n")

    def test_entity_activity(self):
        # test creation
        activity_id = 1
        person_id = [5, 6, 7]
        date = Date(4, 11, 2020)
        time = Time(0, 0, 0, 1)
        description = "nice activity"
        activity = Activity(activity_id, person_id, date, time, description)
        self.assertEqual(activity.activity_id, 1)
        self.assertEqual(activity.person_id, [5, 6, 7])
        self.assertEqual(activity.date, Date(4, 11, 2020))
        self.assertEqual(activity.time, Time(0, 0, 0, 1))
        self.assertEqual(activity.description, "nice activity")
        # test __eq__
        activity1 = Activity(1, "sda", date, time, "asd")
        self.assertEqual(activity, activity1)
        self.assertTrue(activity != Activity(1, "sda", date, time, "dss"))
        self.assertFalse(activity != Activity(activity_id, person_id, date, time, description))
        activity1.person_id = [1, 2, 3]
        activity1.date = Date(1, 1, 2001)
        activity1.time = Time(0, 1, 2, 3)
        activity1.description = "nice description"
        # test __str__
        self.assertEqual(str(
            activity), "1:\nPeople: [5, 6, 7]\nDate: 04.11.2020\nTime: 00:00 - 00:01\nDescription: nice activity\n")

    def test_date(self):
        date = Date(21, 11, 2020)
        self.assertEqual(date.day, 21)
        self.assertEqual(date.month, 11)
        self.assertEqual(date.year, 2020)
        date.day = 24
        date.month = 12
        date.year = 2021
        self.assertEqual(date.day, 24)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.year, 2021)
        self.assertEqual(str(date), "24.12.2021")
        self.assertEqual(str(Date(1, 2, 2020)), "01.02.2020")
        date1 = Date(22, 11, 2020)
        date2 = Date(22, 11, 2021)
        date3 = Date(5, 12, 2020)
        self.assertTrue(date1 < date2)
        self.assertTrue(date1 < date3)

    def test_time(self):
        time = Time(12, 00, 13, 00)
        self.assertEqual(time.start_h, 12)
        self.assertEqual(time.start_m, 00)
        self.assertEqual(time.end_h, 13)
        self.assertEqual(time.end_m, 00)
        time.start_h = 2
        time.start_m = 5
        time.end_h = 3
        time.end_m = 10
        self.assertEqual(time.start_h, 2)
        self.assertEqual(time.start_m, 5)
        self.assertEqual(time.end_h, 3)
        self.assertEqual(time.end_m, 10)
        self.assertEqual(str(time), "02:05 - 03:10")
        time2 = Time(3, 9, 4, 0)
        time3 = Time(0, 0, 1, 0)
        self.assertLess(time3, time)
        self.assertGreater(time, time3)
        self.assertFalse(time3 > time)

    def test_validation_person(self):
        person = Person(-3, "", "")
        person_validator = PersonValidator()
        with self.assertRaises(ValidatorException) as context:
            person_validator.validate(person)
        self.assertTrue(
            "invalid person id!\ninvalid person name!\ninvalid person phone number!\n" in str(context.exception))
        person1 = Person(4, "Nume", "0712345678")
        person_validator.validate(person1)

    def test_validation_activity(self):
        activity = Activity(-1, [], Date(29, 2, 2021), Time(24, 60, 15, 24), "")
        p_repo = PersonRepository()
        activity_validator = ActivityValidator()
        with self.assertRaises(ValidatorException) as context:
            activity_validator.validate(activity)
        self.assertTrue("invalid activity id!\ninvalid activity person id!\ninvalid activity date!\ninvalid activity"
                        " time. hours must be between 0 and 23 and minutes between 0 and 59\ninvalid activity "
                        "description!\n" in str(context.exception))
        activity2 = Activity(1, [-1], Date('ss', 'sa', 'as'), Time(12, 20, 11, 30), "desc1")
        with self.assertRaises(ValidatorException) as context:
            activity_validator.validate(activity2)
        self.assertTrue("invalid activity person id!\ninvalid activity date: must be numbers\ninvalid activity time:"
                        " activity must start before its end\n" in str(context.exception))
        activity3 = Activity(1, [1], Date(12, 11, 2020), Time('s', 'sd', 'a', 'd'), "desc1")
        with self.assertRaises(ValidatorException) as context:
            activity_validator.validate(activity3)
        self.assertTrue("invalid activity time: must be numbers\n" in str(context.exception))
        p_repo.store(Person(4, "", ""))
        p_repo.store(Person(5, "", ""))
        activity2 = Activity(3, [4, 5], Date(4, 11, 2028), Time(17, 51, 18, 00), "sada")
        activity_validator.validate(activity2)
        today = date.today().strftime("%d.%m.%Y")
        cd, cm, cy = today.split('.')
        today = Date(int(cd), int(cm), int(cy))

        now = datetime.now().strftime("%H:%M")
        ch, cm = now.split(':')
        ch = int(ch)
        cm = int(cm)
        activity4 = Activity(99, [4, 5], Date(24, 11, 2050), Time((ch + 1) % 24, 00, (ch + 1) % 24, 30), "desc1")
        activity5 = Activity(99, [4, 5], today, Time(ch - 1, 00, ch - 1, 30), "desc1")
        activity_validator.validate(activity4)
        with self.assertRaises(ValidatorException) as context:
            activity_validator.validate(activity5)
        self.assertTrue("activity can't be in the past" in str(context.exception))
        with self.assertRaises(ValidatorException) as context:
            DateValidator.validate(Date(12, 11, 2020))
        self.assertTrue("Date can't be in the past.\n" in str(context.exception))
        with self.assertRaises(ValidatorException) as context:
            DateValidator.validate(Date(12, 15, 2020))
        self.assertTrue("invalid date!\n" in str(context.exception))

    def test_repo_person(self):
        # crud - create, read, update, delete
        # test storing
        p_repo = PersonRepository()
        self.assertEqual(len(p_repo), 0)
        person = Person(1, "n1", "1234567899")
        p_repo.store(person)
        self.assertEqual(len(p_repo), 1)
        person1 = Person(1, "dfds", "1231231234")
        with self.assertRaises(RepositoryException) as context:
            p_repo.store(person1)
        self.assertTrue("person already exists\n" in str(context.exception))
        # test searching
        self.assertEqual(p_repo.search(1), person)
        with self.assertRaises(RepositoryException) as context:
            p_repo.search(5)
        self.assertTrue("person doesn't exist\n" in str(context.exception))
        # test getting the list
        people = p_repo.get_people()
        self.assertEqual(people, [person])
        # test updating
        p_repo.update(Person(1, "UpdateName", "7777777777"))
        self.assertEqual(p_repo.search(1), Person(1, "UpdateName", "7777777777"))
        with self.assertRaises(RepositoryException) as context:
            p_repo.update(Person(5, "ssd", 8765432198))
        self.assertTrue("person doesn't exist\n" in str(context.exception))
        # test deletion
        self.assertEqual(len(p_repo), 1)
        p_repo.delete(1)
        self.assertEqual(len(p_repo), 0)
        with self.assertRaises(RepositoryException) as context:
            p_repo.delete(5)
        self.assertTrue("person doesn't exist\n" in str(context.exception))
        # test searching by name/phone
        p1 = Person(1, "Nume Prenumescu", "1234567890")
        p2 = Person(2, "NUME PRENUME", "0123456789")
        p_repo.store(p1)
        p_repo.store(p2)
        result = p_repo.search_by_name_phone("nume")
        self.assertEqual(result, [p1, p2])
        result = p_repo.search_by_name_phone("2345")
        self.assertEqual(result, [p1, p2])
        # test is in list
        self.assertTrue(p_repo.is_in_list(2))
        self.assertFalse(p_repo.is_in_list(5))

    def test_file_repo_person(self):
        fp_repo = FilePersonRepository('txt_test_files/person_file_repo_test.txt')
        fp_repo.delete(1)
        with open('txt_test_files/person_file_repo_test.txt', "w") as f:
            f.truncate(0)
        self.assertEqual(len(fp_repo), 0)
        person = Person(1, "n1", "1234567899")
        fp_repo.store(person)
        self.assertEqual(len(fp_repo), 1)
        person1 = Person(1, "dfds", "1231231234")
        with self.assertRaises(RepositoryException) as context:
            fp_repo.store(person1)
        self.assertTrue("person already exists\n" in str(context.exception))
        # test searching
        self.assertEqual(fp_repo.search(1), person)
        with self.assertRaises(RepositoryException) as context:
            fp_repo.search(5)
        self.assertTrue("person doesn't exist\n" in str(context.exception))
        # test getting the list
        people = fp_repo.get_people()
        self.assertEqual(people[0], person)
        # test updating
        fp_repo.update(Person(1, "UpdateName", "7777777777"))
        self.assertEqual(fp_repo.search(1), Person(1, "UpdateName", "7777777777"))
        with self.assertRaises(RepositoryException) as context:
            fp_repo.update(Person(5, "ssd", 8765432198))
        self.assertTrue("person doesn't exist\n" in str(context.exception))
        # test deletion
        self.assertEqual(len(fp_repo), 1)
        fp_repo.delete(1)
        self.assertEqual(len(fp_repo), 0)
        with self.assertRaises(RepositoryException) as context:
            fp_repo.delete(5)
        self.assertTrue("person doesn't exist\n" in str(context.exception))
        # test searching by name/phone
        p1 = Person(1, "Nume Prenumescu", "1234567890")
        p2 = Person(2, "NUME PRENUME", "0123456789")
        fp_repo.store(p1)
        fp_repo.store(p2)
        result = fp_repo.search_by_name_phone("nume")
        self.assertEqual(result, [p1, p2])
        result = fp_repo.search_by_name_phone("2345")
        self.assertEqual(result, [p1, p2])
        # test is in list
        self.assertTrue(fp_repo.is_in_list(2))
        self.assertFalse(fp_repo.is_in_list(5))
        with open('txt_test_files/person_file_repo_test.txt', "w") as f:
            f.write('1;Nume Prenumescu;1234567890\n')

    def test_binary_repo_person(self):
        with open('binary_test_files/binary_person_repo_test.pickle', 'wb') as f:
            f.truncate(0)
        bp_repo = BinaryPersonRepository('binary_test_files/binary_person_repo_test.pickle')
        self.assertEqual(len(bp_repo), 0)
        person = Person(1, "n1", "1234567899")
        bp_repo.store(person)
        self.assertEqual(len(bp_repo), 1)
        person1 = Person(1, "dfds", "1231231234")
        with self.assertRaises(RepositoryException) as context:
            bp_repo.store(person1)
        self.assertTrue("person already exists\n" in str(context.exception))
        # test searching
        self.assertEqual(bp_repo.search(1), person)
        with self.assertRaises(RepositoryException) as context:
            bp_repo.search(5)
        self.assertTrue("person doesn't exist\n" in str(context.exception))
        # test getting the list
        people = bp_repo.get_people()
        self.assertEqual(people[0].name, person.name)
        # test updating
        bp_repo.update(Person(1, "UpdateName", "7777777777"))
        self.assertEqual(bp_repo.search(1), Person(1, "UpdateName", "7777777777"))
        with self.assertRaises(RepositoryException) as context:
            bp_repo.update(Person(5, "ssd", 8765432198))
        self.assertTrue("person doesn't exist\n" in str(context.exception))
        # test deletion
        self.assertEqual(len(bp_repo), 1)
        bp_repo.delete(1)
        self.assertEqual(len(bp_repo), 0)
        with self.assertRaises(RepositoryException) as context:
            bp_repo.delete(5)
        self.assertTrue("person doesn't exist\n" in str(context.exception))
        # test searching by name/phone
        p1 = Person(1, "Nume Prenumescu", "1234567890")
        p2 = Person(2, "NUME PRENUME", "0123456789")
        bp_repo.store(p1)
        bp_repo.store(p2)
        result = bp_repo.search_by_name_phone("nume")
        self.assertEqual(result, [p1, p2])
        result = bp_repo.search_by_name_phone("2345")
        self.assertEqual(result, [p1, p2])
        # test is in list
        self.assertTrue(bp_repo.is_in_list(2))
        self.assertFalse(bp_repo.is_in_list(5))

    def test_json_repo_person(self):
        jp_repo = JSONPersonRepository('json_test_files/person_json_test.json')
        jp_repo.delete(1)
        with open('json_test_files/person_json_test.json', 'w') as f:
            f.truncate(0)
        self.assertEqual(len(jp_repo), 0)
        person = Person(1, "n1", "1234567899")
        jp_repo.store(person)
        self.assertEqual(len(jp_repo), 1)
        person1 = Person(1, "dfds", "1231231234")
        with self.assertRaises(RepositoryException) as context:
            jp_repo.store(person1)
        self.assertTrue("person already exists\n" in str(context.exception))
        # test searching
        self.assertEqual(jp_repo.search(1), person)
        with self.assertRaises(RepositoryException) as context:
            jp_repo.search(5)
        self.assertTrue("person doesn't exist\n" in str(context.exception))
        # test getting the list
        people = jp_repo.get_people()
        self.assertEqual(people, [person])
        # test updating
        jp_repo.update(Person(1, "UpdateName", "7777777777"))
        self.assertEqual(jp_repo.search(1), Person(1, "UpdateName", "7777777777"))
        with self.assertRaises(RepositoryException) as context:
            jp_repo.update(Person(5, "ssd", 8765432198))
        self.assertTrue("person doesn't exist\n" in str(context.exception))
        # test deletion
        self.assertEqual(len(jp_repo), 1)
        jp_repo.delete(1)
        self.assertEqual(len(jp_repo), 0)
        with self.assertRaises(RepositoryException) as context:
            jp_repo.delete(5)
        self.assertTrue("person doesn't exist\n" in str(context.exception))
        # test searching by name/phone
        p1 = Person(1, "Nume Prenumescu", "1234567890")
        p2 = Person(2, "NUME PRENUME", "0123456789")
        jp_repo.store(p1)
        jp_repo.store(p2)
        result = jp_repo.search_by_name_phone("nume")
        self.assertEqual(result, [p1, p2])
        result = jp_repo.search_by_name_phone("2345")
        self.assertEqual(result, [p1, p2])
        # test is in list
        self.assertTrue(jp_repo.is_in_list(2))
        self.assertFalse(jp_repo.is_in_list(5))
        data = {"1": ["Nume Prenumescu", "1234567890"]}
        with open('json_test_files/person_json_test.json', 'w') as f:
            json.dump(data, f)

    def test_repo_activity(self):
        # crud - create, read, update, delete
        # test storing
        a_repo = ActivityRepository()
        self.assertEqual(len(a_repo), 0)
        activity = Activity(1, [1, 2, 3], Date(11, 11, 2020), Time(0, 0, 0, 1), "d1")
        a_repo.store(activity)
        self.assertEqual(len(a_repo), 1)
        with self.assertRaises(RepositoryException) as context:
            a_repo.store(activity)
        self.assertTrue("activity already exists\n" in str(context.exception))
        # test searching
        self.assertEqual(a_repo.search(1), activity)
        with self.assertRaises(RepositoryException) as context:
            a_repo.search(17)
        self.assertTrue("activity doesn't exist\n" in str(context.exception))
        # test getting the list
        activities = a_repo.get_activities()
        self.assertEqual(activities, [activity])
        # test updating
        update_activity = Activity(1, [99], Date(1, 1, 2020), Time(2, 3, 2, 4), "Updated Description")
        a_repo.update(update_activity)
        result = a_repo.search(1)
        self.assertEqual(result, update_activity)
        with self.assertRaises(RepositoryException) as context:
            a_repo.update(Activity(4, [324], Date(2, 2, 2020), Time(1, 1, 1, 2), "des"))
        self.assertTrue("activity doesn't exist\n" in str(context.exception))
        # test deletion
        a_repo.delete(1)
        self.assertEqual(len(a_repo), 0)
        with self.assertRaises(RepositoryException) as context:
            a_repo.delete(4)
        self.assertTrue("activity doesn't exist\n" in str(context.exception))
        # test searching by date, time, description
        a1 = Activity(1, [1, 2], Date(12, 11, 2020), Time(0, 0, 3, 0), "do homework")
        a2 = Activity(2, [2, 3], Date(13, 11, 2020), Time(0, 0, 2, 0), "cry because of the homework")
        a3 = Activity(3, [3, 3], Date(13, 11, 2021), Time(0, 0, 3, 0), "do something fun")
        a_repo.store(a1)
        a_repo.store(a2)
        a_repo.store(a3)
        result = a_repo.search_by_date_time_description("2020")
        self.assertEqual(result, [a1, a2])
        result = a_repo.search_by_date_time_description("00:00")
        self.assertEqual(result, [a1, a2, a3])
        result = a_repo.search_by_date_time_description("work")
        self.assertEqual(result, [a1, a2])
        # test is in list
        self.assertTrue(a_repo.is_in_list(2))
        self.assertFalse(a_repo.is_in_list(5))
        self.assertEqual(a_repo.search_person_activities(Person(1, "n1", "012")), [a1])

    def test_file_repo_activity(self):
        fa_repo = FileActivityRepository("txt_test_files/activity_file_repo_test.txt")
        self.assertEqual(len(fa_repo), 1)
        fa_repo.delete(77)
        with open('txt_test_files/activity_file_repo_test.txt', "w") as f:
            f.truncate(0)
        activity = Activity(1, [1, 2, 3], Date(11, 11, 2020), Time(0, 0, 0, 1), "d1")
        fa_repo.store(activity)
        self.assertEqual(len(fa_repo), 1)
        with self.assertRaises(RepositoryException) as context:
            fa_repo.store(activity)
        self.assertTrue("activity already exists\n" in str(context.exception))
        # test searching
        self.assertEqual(fa_repo.search(1), activity)
        with self.assertRaises(RepositoryException) as context:
            fa_repo.search(17)
        self.assertTrue("activity doesn't exist\n" in str(context.exception))
        # test getting the list
        activities = fa_repo.get_activities()
        self.assertEqual(activities[0], activity)
        # test updating
        update_activity = Activity(1, [99], Date(1, 1, 2020), Time(2, 3, 2, 4), "Updated Description")
        fa_repo.update(update_activity)
        result = fa_repo.search(1)
        self.assertEqual(result, update_activity)
        with self.assertRaises(RepositoryException) as context:
            fa_repo.update(Activity(4, [324], Date(2, 2, 2020), Time(1, 1, 1, 2), "des"))
        self.assertTrue("activity doesn't exist\n" in str(context.exception))
        # test deletion
        fa_repo.delete(1)
        self.assertEqual(len(fa_repo), 0)
        with self.assertRaises(RepositoryException) as context:
            fa_repo.delete(4)
        self.assertTrue("activity doesn't exist\n" in str(context.exception))
        # test searching by date, time, description
        a1 = Activity(1, [1, 2], Date(12, 11, 2020), Time(0, 0, 3, 0), "do homework")
        a2 = Activity(2, [2, 3], Date(13, 11, 2020), Time(0, 0, 2, 0), "cry because of the homework")
        a3 = Activity(3, [3, 3], Date(13, 11, 2021), Time(0, 0, 3, 0), "do something fun")
        fa_repo.store(a1)
        fa_repo.store(a2)
        fa_repo.store(a3)
        result = fa_repo.search_by_date_time_description("2020")
        self.assertEqual(result, [a1, a2])
        result = fa_repo.search_by_date_time_description("00:00")
        self.assertEqual(result, [a1, a2, a3])
        result = fa_repo.search_by_date_time_description("work")
        self.assertEqual(result, [a1, a2])
        # test is in list
        self.assertTrue(fa_repo.is_in_list(2))
        self.assertFalse(fa_repo.is_in_list(5))
        self.assertEqual(fa_repo.search_person_activities(Person(1, "n1", "012")), [a1])
        with open('txt_test_files/activity_file_repo_test.txt', "w") as f:
            f.truncate(0)
            ActivityDataAccess.write_to(f, Activity(77, [1], Date(12, 12, 2025), Time(12, 00, 13, 00), 'dd'))

    def test_binary_repo_activity(self):
        with open('binary_test_files/binary_activity_repo_test.pickle', 'wb') as f:
            f.truncate(0)
        ba_repo = BinaryActivityRepository('binary_test_files/binary_activity_repo_test.pickle')
        self.assertEqual(len(ba_repo), 0)
        activity = Activity(1, [1, 2, 3], Date(11, 11, 2020), Time(0, 0, 0, 1), "d1")
        ba_repo.store(activity)
        self.assertEqual(len(ba_repo), 1)
        with self.assertRaises(RepositoryException) as context:
            ba_repo.store(activity)
        self.assertTrue("activity already exists\n" in str(context.exception))
        # test searching
        self.assertEqual(ba_repo.search(1), activity)
        with self.assertRaises(RepositoryException) as context:
            ba_repo.search(17)
        self.assertTrue("activity doesn't exist\n" in str(context.exception))
        # test getting the list
        activities = ba_repo.get_activities()
        self.assertEqual(activities[0], activity)
        # test updating
        update_activity = Activity(1, [99], Date(1, 1, 2020), Time(2, 3, 2, 4), "Updated Description")
        ba_repo.update(update_activity)
        result = ba_repo.search(1)
        self.assertEqual(result, update_activity)
        with self.assertRaises(RepositoryException) as context:
            ba_repo.update(Activity(4, [324], Date(2, 2, 2020), Time(1, 1, 1, 2), "des"))
        self.assertTrue("activity doesn't exist\n" in str(context.exception))
        # test deletion
        ba_repo.delete(1)
        self.assertEqual(len(ba_repo), 0)
        with self.assertRaises(RepositoryException) as context:
            ba_repo.delete(4)
        self.assertTrue("activity doesn't exist\n" in str(context.exception))
        # test searching by date, time, description
        a1 = Activity(1, [1, 2], Date(12, 11, 2020), Time(0, 0, 3, 0), "do homework")
        a2 = Activity(2, [2, 3], Date(13, 11, 2020), Time(0, 0, 2, 0), "cry because of the homework")
        a3 = Activity(3, [3, 3], Date(13, 11, 2021), Time(0, 0, 3, 0), "do something fun")
        ba_repo.store(a1)
        ba_repo.store(a2)
        ba_repo.store(a3)
        result = ba_repo.search_by_date_time_description("2020")
        self.assertEqual(result, [a1, a2])
        result = ba_repo.search_by_date_time_description("00:00")
        self.assertEqual(result, [a1, a2, a3])
        result = ba_repo.search_by_date_time_description("work")
        self.assertEqual(result, [a1, a2])
        # test is in list
        self.assertTrue(ba_repo.is_in_list(2))
        self.assertFalse(ba_repo.is_in_list(5))
        self.assertEqual(ba_repo.search_person_activities(Person(1, "n1", "012")), [a1])

    def test_json_repo_activity(self):
        ja_repo = JSONActivityRepository('json_test_files/activity_json_test.json')
        ja_repo.delete(1)
        with open('json_test_files/activity_json_test.json', 'w') as f:
            f.truncate(0)
        self.assertEqual(len(ja_repo), 0)
        activity = Activity(1, [1, 2, 3], Date(11, 11, 2020), Time(0, 0, 0, 1), "d1")
        ja_repo.store(activity)
        self.assertEqual(len(ja_repo), 1)
        with self.assertRaises(RepositoryException) as context:
            ja_repo.store(activity)
        self.assertTrue("activity already exists\n" in str(context.exception))
        # test searching
        self.assertEqual(ja_repo.search(1), activity)
        with self.assertRaises(RepositoryException) as context:
            ja_repo.search(17)
        self.assertTrue("activity doesn't exist\n" in str(context.exception))
        # test getting the list
        activities = ja_repo.get_activities()
        self.assertEqual(activities, [activity])
        # test updating
        update_activity = Activity(1, [99], Date(1, 1, 2020), Time(2, 3, 2, 4), "Updated Description")
        ja_repo.update(update_activity)
        result = ja_repo.search(1)
        self.assertEqual(result, update_activity)
        with self.assertRaises(RepositoryException) as context:
            ja_repo.update(Activity(4, [324], Date(2, 2, 2020), Time(1, 1, 1, 2), "des"))
        self.assertTrue("activity doesn't exist\n" in str(context.exception))
        # test deletion
        ja_repo.delete(1)
        self.assertEqual(len(ja_repo), 0)
        with self.assertRaises(RepositoryException) as context:
            ja_repo.delete(4)
        self.assertTrue("activity doesn't exist\n" in str(context.exception))
        # test searching by date, time, description
        a1 = Activity(1, [1, 2], Date(12, 11, 2020), Time(0, 0, 3, 0), "do homework")
        a2 = Activity(2, [2, 3], Date(13, 11, 2020), Time(0, 0, 2, 0), "cry because of the homework")
        a3 = Activity(3, [3, 3], Date(13, 11, 2021), Time(0, 0, 3, 0), "do something fun")
        ja_repo.store(a1)
        ja_repo.store(a2)
        ja_repo.store(a3)
        result = ja_repo.search_by_date_time_description("2020")
        self.assertEqual(result, [a1, a2])
        result = ja_repo.search_by_date_time_description("00:00")
        self.assertEqual(result, [a1, a2, a3])
        result = ja_repo.search_by_date_time_description("work")
        self.assertEqual(result, [a1, a2])
        # test is in list
        self.assertTrue(ja_repo.is_in_list(2))
        self.assertFalse(ja_repo.is_in_list(5))
        self.assertEqual(ja_repo.search_person_activities(Person(1, "n1", "012")), [a1])
        data = {"1": [[1, 2], [12, 11, 2020], [0, 0, 3, 0], "do homework"]}
        with open('json_test_files/activity_json_test.json', 'w') as f:
            json.dump(data, f)

    def test_service_person(self):
        p_repo = PersonRepository()
        p_validator = PersonValidator()
        p_service = PersonService(p_repo, p_validator)
        p_service.add_person(1, "name", "0123456789")
        self.assertEqual(p_service.get_all_people(), [Person(1, "name", "0123")])
        p_service.update_person(1, "Updated Name", "1122334455")
        self.assertEqual(p_service.get_all_people(), [Person(1, "Updated Name", "1122334455")])
        p_service.add_person(2, "Fara nume", "0123456789")
        self.assertEqual(p_service.search_people('am'), [Person(1, "Updated Name", "1122334455")])
        self.assertEqual(p_service.search_people('89'), [Person(2, "Fara nume", "0123456789")])
        self.assertTrue(p_service.is_person(2))
        self.assertFalse(p_service.is_person(3))
        people = p_service.sort_people()
        self.assertEqual(people[0], Person(2, "Fara nume", "0123456789"))
        self.assertEqual(people[1], Person(1, "Updated Name", "1122334455"))
        p_service.remove_person(1)
        p_service.remove_person(2)
        self.assertEqual(p_service.get_all_people(), [])
        self.assertEqual(p_service.search(200), None)

    def test_service_activity(self):
        p_repo = PersonRepository()
        a_repo = ActivityRepository()
        a_validator = ActivityValidator()
        a_service = ActivityService(a_repo, p_repo, a_validator)
        p_repo.store(Person(1, "n1", "1234567890"))
        p_repo.store(Person(2, "n1", "1234567890"))
        a_service.add_activity(1, [1, 2], Date(28, 12, 2025), Time(12, 00, 13, 00), "d1")
        with self.assertRaises(ValidatorException) as context:
            a_service.add_activity(1, [1, 7], Date(25, 12, 2025), Time(12, 00, 13, 00), "d1")
        self.assertTrue("people that don't exist can't take part in activities\n" in str(context.exception))
        self.assertEqual(
            a_service.get_activities_of_person_on_a_date(Person(1, "n1", "1234567890"), Date(28, 12, 2025)),
            [Activity(1, [1, 2], Date(28, 12, 2025), Time(12, 00, 13, 00), "d1")])
        time1 = Time(12, 00, 12, 30)
        time2 = Time(12, 15, 13, 30)
        time3 = Time(13, 30, 14, 30)
        self.assertTrue(a_service.is_same_time(time1, time2))
        self.assertFalse(a_service.is_same_time(time1, time3))
        self.assertFalse(a_service.person_already_has_activity(Person(1, "n1", "1234567890"), Date(21, 11, 2020),
                                                               Time(11, 00, 11, 59)))
        self.assertTrue(a_service.person_already_has_activity(Person(1, "n1", "1234567890"), Date(28, 12, 2025),
                                                              Time(11, 00, 12, 1)))
        with self.assertRaises(ValidatorException) as context:
            a_service.add_activity(1, [1], Date(28, 12, 2025), Time(11, 00, 12, 1), "d1")
        self.assertTrue("user cannot have more than one activity at any given time\n" in str(context.exception))
        self.assertEqual(a_service.get_all_activities(),
                         [Activity(1, [1, 2], Date(21, 11, 2020), Time(12, 00, 13, 00), "d1")])
        a_service.update_activity(1, [2], Date(12, 5, 2026), Time(12, 00, 13, 00), "d1")
        with self.assertRaises(ValidatorException) as context:
            a_service.update_activity(1, [5], Date(12, 5, 2026), Time(12, 00, 13, 00), "d1")
        self.assertTrue("people that don't exist can't take part in activities\n" in str(context.exception))
        a_service.remove_person_from_activity(2)
        p_repo.store(Person(2, "n1", "1234567890"))
        a_service.add_activity(1, [1, 2], Date(12, 5, 2026), Time(12, 00, 13, 00), "d1")
        a_service.remove_person_from_activity(1)
        self.assertTrue(a_service.is_activity(1))
        self.assertFalse(a_service.is_activity(2))
        self.assertEqual(a_service.search_activities("5.2026"),
                         [Activity(1, [2], Date(12, 5, 2026), Time(12, 00, 13, 00), "d1")])
        a_service.add_activity(2, [2], Date(12, 5, 2026), Time(5, 0, 6, 0), "dd")
        a_service.add_activity(3, [2], Date(12, 5, 2026), Time(1, 0, 2, 0), "dd")
        a_service.add_activity(4, [2], Date(12, 5, 2026), Time(3, 0, 4, 0), "dd")
        self.assertEqual(a_service.activities_for_date(Date(12, 5, 2026)),
                         [Activity(3, [2], Date(12, 5, 2026), Time(1, 0, 2, 0), "dd"),
                          Activity(4, [2], Date(12, 5, 2026), Time(3, 0, 4, 0), "dd"),
                          Activity(2, [2], Date(12, 5, 2026), Time(5, 0, 6, 0), "dd"),
                          Activity(1, [2], Date(12, 5, 2026), Time(12, 00, 13, 00), "d1")])
        a_service.add_activity(5, [2], Date(13, 5, 2026), Time(5, 0, 6, 0), "dd")
        a_service.add_activity(6, [2], Date(14, 5, 2026), Time(0, 0, 1, 1), "dd")
        a_service.add_activity(7, [2], Date(14, 5, 2026), Time(2, 0, 3, 0), "dd")
        a_service.add_activity(8, [2], Date(14, 5, 2026), Time(4, 0, 5, 0), "dd")
        a_service.add_activity(9, [2], Date(14, 5, 2026), Time(6, 0, 7, 0), "dd")
        a_service.add_activity(10, [2], Date(14, 5, 2026), Time(8, 0, 9, 0), "dd")
        a_service.add_activity(11, [2], Date(10, 5, 2026), Time(10, 0, 11, 0), "dd")
        a_service.add_activity(12, [2], Date(18, 5, 2026), Time(0, 0, 0, 5), "dd")
        expected = ["On the date 18.05.2026, the activities take 5 minutes.\n",
                    "On the date 10.05.2026, the activities take 1 hour.\n",
                    "On the date 13.05.2026, the activities take 1 hour.\n",
                    "On the date 12.05.2026, the activities take 4 hours.\n",
                    "On the date 14.05.2026, the activities take 5 hours and 1 minute.\n"]
        activities = a_service.busiest_days()
        for i in range(len(activities)):
            self.assertEqual(str(activities[i]), str(expected[i]))
        expected = [Activity(11, [2], Date(10, 5, 2026), Time(10, 0, 11, 0), "dd"),
                    Activity(3, [2], Date(12, 5, 2026), Time(1, 0, 2, 0), "dd"),
                    Activity(4, [2], Date(12, 5, 2026), Time(3, 0, 4, 0), "dd"),
                    Activity(2, [2], Date(12, 5, 2026), Time(5, 0, 6, 0), "dd"),
                    Activity(1, [2], Date(12, 5, 2026), Time(12, 00, 13, 00), "d1"),
                    Activity(5, [2], Date(13, 5, 2026), Time(5, 0, 6, 0), "dd"),
                    Activity(6, [2], Date(14, 5, 2026), Time(0, 0, 1, 1), "dd"),
                    Activity(7, [2], Date(14, 5, 2026), Time(2, 0, 3, 0), "dd"),
                    Activity(8, [2], Date(14, 5, 2026), Time(4, 0, 5, 0), "dd"),
                    Activity(9, [2], Date(14, 5, 2026), Time(6, 0, 7, 0), "dd"),
                    Activity(10, [2], Date(14, 5, 2026), Time(8, 0, 9, 0), "dd"),
                    Activity(12, [2], Date(18, 5, 2026), Time(0, 0, 0, 5), "dd")]
        activities = a_service.activities_with_a_person(2)
        for i in range(len(activities)):
            self.assertEqual(str(activities[i]), str(expected[i]))
        with self.assertRaises(ValidatorException) as context:
            activities = a_service.activities_with_a_person(20)
        self.assertTrue("Person that doesn't exist does not have activities.\n" in str(context.exception))
        self.assertEqual(a_service.search(200), None)
        # test sorting
        result = a_service.sort_activities()
        index = 12
        for a in result:
            self.assertEqual(a.activity_id, index)
            index -= 1

    # def test_person_generator(self):
    #     p_repo = PersonRepository()
    #     p_valid = PersonValidator()
    #     p_service = PersonService(p_repo, p_valid)
    #     undo_redo_repo = UndoRedoRepo()
    #     undo_redo_service = UndoRedoService(undo_redo_repo)
    #     p_gen = PersonGenerator(p_service, undo_redo_service)
    #     for i in range(10):
    #         p_gen.generate_people()
    #     self.assertEqual(len(p_repo), 100)
    #
    # def test_activity_generator(self):
    #     p_repo = PersonRepository()
    #     p_valid = PersonValidator()
    #     p_service = PersonService(p_repo, p_valid)
    #     a_repo = ActivityRepository()
    #     a_valid = ActivityValidator()
    #     undo_redo_repo = UndoRedoRepo()
    #     undo_redo_service = UndoRedoService(undo_redo_repo)
    #     p_gen = PersonGenerator(p_service, undo_redo_service)
    #     a_service = ActivityService(a_repo, p_repo, a_valid)
    #     a_gen = ActivityGenerator(a_service, p_service, undo_redo_service)
    #     # p_gen.generate_people()
    #     p_service.add_person(1, "Name", "1122334455")
    #     p_service.add_person(2, "Name", "1122334455")
    #     p_service.add_person(3, "Name", "1122334455")
    #     for i in range(10):
    #         a_gen.generate_activities()
    #     self.assertFalse(a_gen.is_same_time(Time(12, 00, 13, 00), Time(14, 00, 15, 00)))
    #     self.assertTrue(a_gen.is_same_time(Time(12, 00, 13, 00), Time(12, 30, 14, 00)))
    #     today = date.today().strftime("%d.%m.%Y")
    #     cd, cm, cy = today.split('.')
    #     now = datetime.now().strftime("%H:%M")
    #     ch = now.split(':')[0]
    #     ch = int(ch)
    #     today = Date(int(cd), int(cm), int(cy))
    #     for i in range(10):
    #         a_gen.generate_time(today)
    #     people_ids = [a_repo.get_activities()[0].person_id[0]]
    #     a_date = a_repo.get_activities()[0].date
    #     time = a_repo.get_activities()[0].time
    #     self.assertFalse(a_gen.good_people(people_ids, a_date, time))

    def test_undo_activity(self):
        a_repo = ActivityRepository()
        p_repo = PersonRepository()
        a_valid = ActivityValidator()
        a_service = ActivityService(a_repo, p_repo, a_valid)
        undo_redo_repo = UndoRedoRepo()
        undo_redo_service = UndoRedoService(undo_redo_repo)
        p_repo.store(Person(1, "Name", '1212121212'))
        a_service.add_activity(1, [1], Date(1, 1, 2030), Time(12, 0, 13, 0), 'desc')

        undo_activity = undo_redo_service.create_operation(a_service, UndoHandler.ADD_ACTIVITY, 1, [1],
                                                           Date(1, 1, 2030), Time(12, 0, 13, 0), 'desc')
        undo_redo_service.push(undo_activity)

        a_service.add_activity(2, [1], Date(1, 1, 2031), Time(12, 0, 13, 0), 'desc')
        undo_activity = undo_redo_service.create_operation(a_service, UndoHandler.ADD_ACTIVITY, 2, [1],
                                                           Date(1, 1, 2031), Time(12, 0, 13, 0), 'desc')
        undo_redo_service.push(undo_activity)
        # act 1,2
        a_service.remove_activity(1)
        # act 2
        undo_activity = undo_redo_service.create_operation(a_service, UndoHandler.DELETE_ACTIVITY, 1, [1],
                                                           Date(1, 1, 2030), Time(12, 0, 13, 0), 'desc')
        undo_redo_service.push(undo_activity)
        activities = a_service.get_all_activities()
        self.assertEqual(len(activities), 1)
        self.assertEqual(activities[0], Activity(2, [1], Date(1, 1, 2031), Time(12, 0, 13, 0), 'desc'))
        undo_redo_service.undo()
        # act 1,2
        activities = a_service.get_all_activities()
        self.assertEqual(len(activities), 2)
        self.assertEqual(activities[0], Activity(2, [1], Date(1, 1, 2031), Time(12, 0, 13, 0), 'desc'))
        self.assertEqual(activities[1], Activity(1, [1], Date(1, 1, 2030), Time(12, 0, 13, 0), 'desc'))
        undo_redo_service.redo()
        # act 2
        activities = a_service.get_all_activities()
        self.assertEqual(len(activities), 1)
        self.assertEqual(activities[0], Activity(2, [1], Date(1, 1, 2031), Time(12, 0, 13, 0), 'desc'))
        a_service.update_activity(2, [1], Date(22, 12, 2022), Time(5, 0, 7, 0), 'updated')
        self.assertEqual(a_service.search(2).description, 'updated')
        # act 2 updated
        undo_activity = undo_redo_service.create_operation(a_service, UndoHandler.UPDATE_ACTIVITY,
                                                           2, [1], Date(1, 1, 2031), Time(12, 0, 13, 0), 'desc', [1],
                                                           Date(22, 12, 2022), Time(5, 0, 7, 0), 'updated')
        undo_redo_service.push(undo_activity)
        undo_redo_service.undo()
        self.assertEqual(a_service.search(2).description, 'desc')
        # act 2

        activities = a_service.get_all_activities()
        self.assertEqual(activities[0], Activity(2, [1], Date(1, 1, 2031), Time(12, 0, 13, 0), 'desc'))
        undo_redo_service.redo()

        # act 2 updated
        self.assertEqual(a_service.search(2).description, 'updated')
        a_service.add_activity(3, [1], Date(24, 11, 2050), Time(12, 0, 13, 0), 'desc3')
        # act 2 updated, 3
        undo_activity = undo_redo_service.create_operation(a_service, UndoHandler.ADD_ACTIVITY, 3, [1],
                                                           Date(24, 11, 2050), Time(12, 0, 13, 0), 'desc3')
        undo_redo_service.push(undo_activity)
        with self.assertRaises(UndoException) as context:
            undo_redo_service.redo()
        self.assertTrue("No more redos!\n" in str(context.exception))
        undo_redo_service.undo()
        # act 2 updated
        self.assertEqual(a_service.search(2).description, 'updated')
        undo_redo_service.redo()
        # here we have activities with ids 2 updated,3
        undo_redo_service.undo()
        # here we have activities with ids 2 updated (undid the adding of 3)
        undo_redo_service.undo()
        # here we have act 2 (undid update)
        undo_redo_service.undo()
        # here we have acts 2 and 1 (undid removal of 1)
        undo_redo_service.undo()
        # here we have act 1 (undid adding of 2)
        undo_redo_service.undo()
        # here we have no acts (undid adding of 1)
        self.assertTrue(len(a_service.get_all_activities()) == 0)
        with self.assertRaises(UndoException) as context:
            undo_redo_service.undo()
        self.assertTrue("No more undos!\n" in str(context.exception))

    def test_undo_person(self):
        p_repo = PersonRepository()
        p_valid = PersonValidator()
        p_service = PersonService(p_repo, p_valid)
        undo_redo_repo = UndoRedoRepo()
        undo_redo_service = UndoRedoService(undo_redo_repo)
        p_service.add_person(1, 'N1', '1231231234')
        undo_op = undo_redo_service.create_operation(p_service, UndoHandler.ADD_PERSON, 1, 'N1', '1231231234')
        undo_redo_service.push(undo_op)
        p_service.add_person(2, 'N2', '7897897890')
        undo_op = undo_redo_service.create_operation(p_service, UndoHandler.ADD_PERSON, 2, 'N2', '7897897890')
        undo_redo_service.push(undo_op)
        undo_redo_service.undo()
        self.assertEqual(len(p_service.get_all_people()), 1)
        undo_redo_service.redo()
        self.assertEqual(len(p_service.get_all_people()), 2)

        p_service.update_person(2, 'updatedName', '1112223334')
        undo_op = undo_redo_service.create_operation(p_service, UndoHandler.UPDATE_PERSON, 2, 'N2', '7897897890',
                                                     'updatedName', '1112223334')
        undo_redo_service.push(undo_op)

        self.assertEqual(p_service.search(2).name, 'updatedName')
        undo_redo_service.undo()
        self.assertEqual(p_service.search(2).name, 'N2')
        undo_redo_service.redo()
        self.assertEqual(p_service.search(2).name, 'updatedName')
        with self.assertRaises(UndoException) as context:
            undo_redo_service.redo()
        self.assertTrue("No more redos!\n" in str(context.exception))
        # people 1,2updated
        undo_redo_service.undo()
        # people 1, 2
        self.assertEqual(len(p_service.get_all_people()), 2)
        undo_redo_service.undo()
        # people 1
        self.assertEqual(len(p_service.get_all_people()), 1)
        undo_redo_service.undo()
        # no people
        self.assertEqual(len(p_service.get_all_people()), 0)
        with self.assertRaises(UndoException) as context:
            undo_redo_service.undo()
        self.assertTrue("No more undos!\n" in str(context.exception))

        # complex stuff
        a_repo = ActivityRepository()
        a_valid = ActivityValidator()
        a_service = ActivityService(a_repo, p_repo, a_valid)
        undo_redo_service.redo()  # now we have person 1
        undo_redo_service.redo()  # now we have person 1,2
        a_service.add_activity(1, [1], Date(12, 12, 2060), Time(0, 0, 1, 0), 'desc1')
        undo_activity = undo_redo_service.create_operation(a_service, UndoHandler.ADD_ACTIVITY, 1, [1],
                                                           Date(12, 12, 2060), Time(0, 0, 1, 0), 'desc1')
        undo_redo_service.push(undo_activity)
        a_service.add_activity(2, [1, 2], Date(15, 5, 2065), Time(2, 0, 3, 0), 'desc2')
        undo_activity = undo_redo_service.create_operation(a_service, UndoHandler.ADD_ACTIVITY, 2, [1, 2],
                                                           Date(15, 5, 2065), Time(2, 0, 3, 0), 'desc2')
        undo_redo_service.push(undo_activity)
        a_service.remove_person_from_activity(1)
        activity_list = [Activity(1, [1], Date(12, 12, 2060), Time(0, 0, 1, 0), 'desc1'),
                         Activity(2, [1, 2], Date(15, 5, 2065), Time(2, 0, 3, 0), 'desc2')]
        complex_undo_activity = undo_redo_service.create_complex_operation(p_service, a_service,
                                                                           UndoComplexHandler.DELETE_PERSON_COMPLEX,
                                                                           Person(1, 'N1', '1231231234'), activity_list)
        undo_redo_service.push(complex_undo_activity)

        people = p_service.get_all_people()
        self.assertEqual(len(people), 1)
        self.assertEqual(people[0].name, 'N2')
        self.assertEqual(len(a_service.get_all_activities()), 1)
        self.assertEqual(a_service.get_all_activities()[0].description, 'desc2')

        undo_redo_service.undo()
        people = p_service.get_all_people()
        self.assertEqual(len(people), 2)
        self.assertEqual(people[1].name, 'N1')
        self.assertEqual(len(a_service.get_all_activities()), 2)
        self.assertEqual(a_service.get_all_activities()[0].person_id, [2, 1])
        self.assertEqual(a_service.get_all_activities()[1].person_id, [1])

        undo_redo_service.redo()
        people = p_service.get_all_people()
        self.assertEqual(len(people), 1)
        self.assertEqual(people[0].name, 'N2')
        self.assertEqual(len(a_service.get_all_activities()), 1)
        self.assertEqual(a_service.get_all_activities()[0].person_id, [2])
