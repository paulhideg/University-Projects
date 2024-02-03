from errors.exceptions import ValidatorException


class PersonValidator:

    def validate(self, person):
        error = ""
        if person.person_id < 1:
            error += "invalid person id!\n"
        if person.name == "":
            error += "invalid person name!\n"
        if person.phone_number == "" or len(person.phone_number) != 10 or not person.phone_number.isnumeric():
            error += "invalid person phone number!\n"
        if len(error) > 0:
            raise ValidatorException(error)
