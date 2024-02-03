from domain.entities.person import Person
from errors.exceptions import ValidatorException
from domain.useful_stuff.date import Date
from domain.useful_stuff.time import Time
from datetime import datetime, date


class ActivityValidator:
    @staticmethod
    def leap(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False

    def validate(self, activity):
        errors = ""
        if activity.activity_id < 1:
            errors += "invalid activity id!\n"
        if not activity.person_id:
            errors += "invalid activity person id!\n"
        else:
            for i in activity.person_id:
                if i < 1:
                    errors += "invalid activity person id!\n"
                    break
        if not (isinstance(activity.date.day, int) or isinstance(activity.date.month, int) or isinstance(
                activity.date.year, int)):
            errors += "invalid activity date: must be numbers\n"
        else:
            if not (0 < activity.date.day <= 31 and 0 < activity.date.month <= 12) or (
                    activity.date.month in [4, 6, 9, 11] and activity.date.day > 30) or (
                    activity.date.month == 2 and activity.date.day > 29) or (
                    not ActivityValidator.leap(
                        activity.date.year) and activity.date.month == 2 and activity.date.day > 28):
                errors += "invalid activity date!\n"
            else:
                today = date.today().strftime("%d.%m.%Y")
                cd, cm, cy = today.split('.')
                today = Date(int(cd), int(cm), int(cy))
                if activity.date < today:
                    errors += "activity can't be in the past"
                elif activity.date == today:
                    now = datetime.now().strftime("%H:%M")
                    ch, cm = now.split(':')
                    ch = int(ch)
                    cm = int(cm)
                    if activity.time.start_h < ch or (
                            activity.time.start_h == ch and (activity.time.start_m < cm or cm == 0)):
                        errors += "activity can't be in the past"

        if not (isinstance(activity.time.start_h, int) or isinstance(activity.time.start_m, int) or isinstance(
                activity.time.end_h, int) or isinstance(activity.time.end_m, int)):
            errors += "invalid activity time: must be numbers\n"
        else:
            if not (
                    0 <= activity.time.start_h < 24 and 0 <= activity.time.end_h < 24 and 0 <= activity.time.start_m < 60
                    and 0 <= activity.time.end_m < 60):
                errors += "invalid activity time. hours must be between 0 and 23 and minutes between 0 and 59\n"
            elif (activity.time.start_h > activity.time.end_h) or (
                    activity.time.start_h == activity.time.end_h and activity.time.start_m >= activity.time.end_m):
                errors += "invalid activity time: activity must start before its end\n"
        if activity.description == "":
            errors += "invalid activity description!\n"
        if len(errors) > 0:
            raise ValidatorException(errors)


class DateValidator:
    @staticmethod
    def validate(given_date):
        errors = ''
        if not (0 < given_date.day <= 31 and 0 < given_date.month <= 12) or (
                given_date.month in [4, 6, 9, 11] and given_date.day > 30) or (
                given_date.month == 2 and given_date.day > 29) or (
                not ActivityValidator.leap(given_date.year) and given_date.month == 2 and given_date.day > 28):
            errors += "invalid date!\n"
        else:
            today = date.today().strftime("%d.%m.%Y")
            cd, cm, cy = today.split('.')
            today = Date(int(cd), int(cm), int(cy))
            if given_date < today:
                errors += "Date can't be in the past.\n"
        if len(errors) > 0:
            raise ValidatorException(errors)
