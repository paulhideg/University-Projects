from dataclasses import dataclass
from enum import Enum


def add_person_handler(person_service, person_id, person_name, phone_number):
    person_service.remove_person(person_id)


def delete_person_handler(person_service, person_id, person_name, phone_number):
    person_service.add_person(person_id, person_name, phone_number)


def update_person_handler(person_service, person_id, old_person_name, old_phone_number, new_person_name,
                          new_phone_number):
    person_service.update_person(person_id, old_person_name, old_phone_number)


def update_person_rev_handler(person_service, person_id, old_person_name, old_phone_number, new_person_name,
                              new_phone_number):
    person_service.update_person(person_id, new_person_name, new_phone_number)


def add_activity_handler(activity_service, activity_id, activity_people, date, time, description):
    activity_service.remove_activity(activity_id)


def delete_activity_handler(activity_service, activity_id, activity_people, date, time, description):
    activity_service.add_activity(activity_id, activity_people, date, time, description)


def update_activity_handler(activity_service, activity_id, old_activity_people, old_date, old_time, old_description,
                            new_activity_people, new_date, new_time, new_description):
    activity_service.update_activity(activity_id, old_activity_people, old_date, old_time, old_description)


def update_activity_rev_handler(activity_service, activity_id, old_activity_people, old_date, old_time, old_description,
                                new_activity_people, new_date, new_time, new_description):
    activity_service.update_activity(activity_id, new_activity_people, new_date, new_time, new_description)


class UndoHandler(Enum):
    ADD_PERSON = add_person_handler
    DELETE_PERSON = delete_person_handler
    UPDATE_PERSON = update_person_handler
    UPDATE_PERSON_REV = update_person_rev_handler
    ADD_ACTIVITY = add_activity_handler
    DELETE_ACTIVITY = delete_activity_handler
    UPDATE_ACTIVITY = update_activity_handler
    UPDATE_ACTIVITY_REV = update_activity_rev_handler

    @staticmethod
    def get_opposite_handler(handler):
        if handler == UndoHandler.ADD_PERSON:
            return UndoHandler.DELETE_PERSON
        elif handler == UndoHandler.UPDATE_PERSON:
            return UndoHandler.UPDATE_PERSON_REV
        elif handler == UndoHandler.ADD_ACTIVITY:
            return UndoHandler.DELETE_ACTIVITY
        elif handler == UndoHandler.DELETE_ACTIVITY:
            return UndoHandler.ADD_ACTIVITY
        elif handler == UndoHandler.UPDATE_ACTIVITY:
            return UndoHandler.UPDATE_ACTIVITY_REV


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


def delete_person_complex_handler(person_service, activity_service, person, activity_list):
    person_service.add_person(person.person_id, person.name, person.phone_number)
    for activity in activity_list:
        if activity_service.is_activity(activity.activity_id):
            people_ids = activity.person_id[:]
            people_ids.remove(person.person_id)
            people_ids.append(person.person_id)
            activity_service.update_activity(activity.activity_id, people_ids, activity.date, activity.time,
                                             activity.description)
        else:
            activity_service.add_activity(activity.activity_id, [person.person_id], activity.date, activity.time,
                                          activity.description)


def add_person_complex_handler(person_service, activity_service, person, activity_list):
    for activity in activity_list:
        if len(activity.person_id) > 1:
            people_ids = activity.person_id[:]
            people_ids.remove(person.person_id)
            activity_service.update_activity(activity.activity_id, people_ids, activity.date, activity.time,
                                             activity.description)
        else:
            activity_service.remove_activity(activity.activity_id)
    person_service.remove_person(person.person_id)


class UndoComplexHandler(Enum):
    DELETE_PERSON_COMPLEX = delete_person_complex_handler
    ADD_PERSON_COMPLEX = add_person_complex_handler

    @staticmethod
    def get_opposite_handler():
        return UndoComplexHandler.ADD_PERSON_COMPLEX


@dataclass
class UndoRedoComplexOperation:
    target_object1: object
    target_object2: object
    handler: object
    obj1: object
    obj2: object

    def perform_operation(self):
        self.handler(self.target_object1, self.target_object2, self.obj1, self.obj2)

    def perform_reverse_operation(self):
        opposite_handler = UndoComplexHandler.get_opposite_handler()
        opposite_handler(self.target_object1, self.target_object2, self.obj1, self.obj2)
