from services import Services
from domain import Student


def test_add_student(serv=Services()):
    serv.students = []
    serv.add_student(Student(15, "Steve", 4))
    assert len(serv.students) == 1


test_add_student()
