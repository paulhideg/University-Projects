from errors.exceptions import ValidationError


class ValidatorStudent(object):
    """
        The validator class for student
    """

    def validate(self, student):
        errors = ""
        if student.get_student_id() < 0:
            errors += "invalid student id\n"
        if student.get_name() == "":
            errors += "invalid name\n"
        if len(errors) > 0:
            raise ValidationError(errors)


class ValidatorDiscipline(object):
    """
        The validator class for discipline
    """

    def validate(self, discipline):
        errors = ""
        if discipline.get_discipline_id() < 0:
            errors += "invalid discipline id\n"
        if discipline.get_name() == "":
            errors += "invalid name\n"
        if len(errors) > 0:
            raise ValidationError(errors)


class ValidatorGrade(object):
    """
        The validator class for grade
    """

    def validate(self, grade, grade_value):
        errors = ""
        if grade.get_student_id() < 0:
            errors += "invalid student id\n"
        if grade.get_discipline_id() < 0:
            errors += "invalid discipline id\n"
        if grade_value < 1 or grade_value > 10:
            errors += "invalid grade\n"
        if len(errors) > 0:
            raise ValidationError(errors)
