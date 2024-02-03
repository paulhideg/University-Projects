from domain.student import Student
from domain.discipline import Discipline
from domain.grade import Grade
from errors.exceptions import RepositoryError
import random
import statistics
from operator import itemgetter


class RepoStudents(object):
    def __init__(self):
        self._students = []

    def __len__(self):
        """
        Returns the length of the students repo
        """
        return len(self._students)

    def random_students(self):
        """
        Generates 10 random students
        """
        names = ["Sergio", "Aydin", "Rylee", "Rory", "James", "Rex", "Matthias", "Lawrence", "Kyler", "Isaiah", "Roland", "Mohamed", "Romeo", "Leroy", "Davis",
                 "Raven", "Melissa", "Theresa", "Carla", "Mariah", "Tiana", "Cara", "Mia", "Kenna", "Mallory", "Jessica", "Lillian", "Donna", "Rebecca", "Iulia"]
        random.shuffle(names)
        for i in range(1, 11):
            s = Student(i, names[i])
            self._students.append(s)

    def add_student(self, student):
        """
        Adds a student to the repo, if there isn't already a student with the same id
        """
        for _student in self._students:
            if _student.get_student_id() == student.get_student_id():
                raise RepositoryError("student id already registered")
        self._students.append(student)

    def remove_student(self, student_id):
        """
        removes a student by his id, if it is in the repo
        """
        ok = True
        for _student in self._students:
            if _student.get_student_id() == student_id:
                self._students.remove(_student)
                ok = False
        if ok:
            raise RepositoryError("inexistent student id")

    def search_by_id(self, student_id):
        """
        searches a student by id
        """
        ok = True
        for _student in self._students:
            if _student.get_student_id() == student_id:
                return _student
        if ok:
            raise RepositoryError("inexistent student id")

    def update_student(self, student_id, name):
        """
        updates a student based on his id
        """
        ok = True
        for _student in self._students:
            if _student.get_student_id() == student_id:
                _student.set_name(name)
                ok = False
        if ok:
            raise RepositoryError("inexistent student id")

    def get_all_students(self):
        """
        returns the list of repo students
        """
        return self._students[:]

    def search_students(self, value):
        """
        searches a student based on a string/substring
        """
        result = []
        for _student in self._students:
            if value in str(_student.get_student_id()) or value in str(_student.get_name()).lower():
                result.append(_student)
        if len(result) == 0:
            result.append("No students fit the criteria")
        else:
            result.insert(0, str(len(result)) + " student(s) found:")
            result.insert(0, "")
        return result


class RepoDisciplines(object):
    def __init__(self):
        self._disciplines = []

    def random_disciplines(self):
        """
        Generates 10 random disciplines
        """
        disciplines = ["Astronomy", "Biology", "Chemistry", "Physics", "Mathematics", "Computer Science", "Communications", "Economics", "History", "Psychology",
                       "Sociology", "Arts", "Music", "Philosophy", "Theatre", "Business", "Law", "Engineering", "Agriculture", "Journalism",
                       "Education", "Health", "Anatomy", "Optics", "Geography", "Sports", "Algebra", "Artificial Intelligence", "Cryptography", "Robotics"]
        random.shuffle(disciplines)
        for i in range(1, 11):
            s = Discipline(i, disciplines[i])
            self._disciplines.append(s)

    def __len__(self):
        """
        Returns the length of the disciplines repo
        """
        return len(self._disciplines)

    def add_discipline(self, discipline):
        """
        Adds a discipline to the repo, if there isn't already a discipline with the same id
        """
        for _discipline in self._disciplines:
            if _discipline.get_discipline_id() == discipline.get_discipline_id():
                raise RepositoryError("discipline id already registered")
        self._disciplines.append(discipline)

    def remove_discipline(self, discipline_id):
        """
        removes a discipline by his id, if it is in the repo
        """
        ok = True
        for _discipline in self._disciplines:
            if _discipline.get_discipline_id() == discipline_id:
                self._disciplines.remove(_discipline)
                ok = False
        if ok:
            raise RepositoryError("inexistent discipline id")

    def search_by_id(self, discipline_id):
        """
        searches a discipline by id
        """
        ok = True
        for _discipline in self._disciplines:
            if _discipline.get_discipline_id() == discipline_id:
                return _discipline
        if ok:
            raise RepositoryError("inexistent discipline id")

    def update_discipline(self, discipline_id, name):
        """
        updates a discipline based on his id
        """
        ok = True
        for _discipline in self._disciplines:
            if _discipline.get_discipline_id() == discipline_id:
                _discipline.set_name(name)
                ok = False
        if ok:
            raise RepositoryError("inexistent id")

    def get_all_disciplines(self):
        """
        returns the list of repo disciplines
        """
        return self._disciplines[:]

    def search_disciplines(self, value):
        """
        searches a discipline based on a string/substring
        """
        result = []
        for _discipline in self._disciplines:
            if value in str(_discipline.get_discipline_id()) or value in str(_discipline.get_name()).lower():
                result.append(_discipline)
        if len(result) == 0:
            result.append("No disciplines fit the criteria")
        else:
            result.insert(0, str(len(result)) + " discipline(s) found:")
            result.insert(0, "")
        return result


class RepoGrades(object):
    def __init__(self):
        self._grades = []

    def random_grades(self):
        """
        generates 3 grades  per student with a random number of disciplines (3 grades *  3-5 disciplines * 10 students)
        """
        for i in range(1, 11):
            for j in range(random.randint(1, 2), 11, random.randint(2, 3)):
                grade = Grade(i, j, random.randint(4, 10))
                for k in range(1, 3):
                    grade.set_grade_value(random.randint(4, 10))
                self._grades.append(grade)

    def __len__(self):
        """
        returns the length of repo grades
        """
        return len(self._grades)

    def add_grade(self, grade, grade_value):
        """
        adds a grade to the repo grades
        """
        ok = True
        for _grade in self._grades:
            if _grade.get_student_id() == grade.get_student_id() and _grade.get_discipline_id() == grade.get_discipline_id():
                _grade.set_grade_value(grade_value)
                ok = False
        if ok:
            self._grades.append(grade)

    def remove_grade(self, student, discipline, grade, grade_value):
        """
        removes a grade from the list of grades
        """
        ok = True
        for _grade in self._grades:
            if _grade.get_student_id() == grade.get_student_id() and _grade.get_discipline_id() == grade.get_discipline_id():
                _grade.get_grade_value().remove(grade_value)
                if(len(_grade.get_grade_value()) == 0):
                    self._grades.remove(_grade)
                break

    def get_all_grades(self):
        """
        returns a list of all grades registered in the repo
        """
        return self._grades[:]

    def remove_grades_student(self, student_id):
        """
        removes all grades that have a given student's id
        """
        for i in range((len(self._grades))-1, -1, -1):
            grade = self._grades[i]
            if grade.get_student_id() == student_id:
                del self._grades[i]

    def remove_grades_discipline(self, discipline_id):
        """
        removes all grades that have a given discipline's id
        """
        for i in range((len(self._grades))-1, -1, -1):
            _grade = self._grades[i]
            if _grade.get_discipline_id() == discipline_id:
                del self._grades[i]

    def get_grades_by_student_id(self, student_id):
        """
        returns a list of grades objects that match the student id
        """
        list_of_grades = []
        for _grade in self._grades:
            if _grade.get_student_id() == student_id:
                item = []
                item.append(_grade)
                item.append(_grade.get_grade_value())
                list_of_grades.append(item)
        return list_of_grades

    def get_grades_by_discipline_id(self, discipline_id):
        """
        returns a list of grades objects that match the discipline id
        """
        list_of_grades = []
        for _grade in self._grades:
            if _grade.get_discipline_id() == discipline_id:
                item = []
                item.append(_grade)
                item.append(_grade.get_grade_value())
                list_of_grades.append(item)
        return list_of_grades

    """
    STATS
    """

    def students_failing(self):
        """
        returns a list of students that are failing
        """
        students_failing = []
        for _grade in self._grades:
            if round(statistics.mean(_grade.get_grade_value()), 2) < 5.00:
                if _grade.get_student_id() not in students_failing:
                    students_failing.append(_grade.get_student_id())
        return students_failing

    def students_top(self):
        """
        returns a sorted list of all students by their aggregated average
        """
        students_top = []
        id_s = []
        for _grade in self._grades:
            if _grade.get_student_id() not in id_s:
                id_s.append(_grade.get_student_id())
        for id in id_s:
            student_averages = []
            for _grade in self._grades:
                if _grade.get_student_id() == id:
                    student_averages.append(
                        round(statistics.mean(_grade.get_grade_value()), 2))
            student_aggregated_average = round(
                statistics.mean(student_averages), 2)
            students_top.append([id, student_aggregated_average])
        students_top = sorted(students_top, key=itemgetter(1), reverse=True)
        return students_top

    def disciplines_highest(self):
        """
        returns a sorted list of disciplines sorted by their average grade
        """
        disciplines_highest = []
        id_s = []
        for _grade in self._grades:
            if _grade.get_discipline_id() not in id_s:
                id_s.append(_grade.get_discipline_id())
        for id in id_s:
            discipline_averages = []
            for _grade in self._grades:
                if _grade.get_discipline_id() == id:
                    discipline_averages.append(
                        round(statistics.mean(_grade.get_grade_value()), 2))
            discipline_aggregated_average = round(
                statistics.mean(discipline_averages), 2)
            disciplines_highest.append([id, discipline_aggregated_average])
        disciplines_highest = sorted(
            disciplines_highest, key=itemgetter(1), reverse=True)
        return disciplines_highest


class RepoUndo(object):
    def __init__(self):
        self._stack = [] 
        self._stack_index = -1

    def push(self, undo_op):
        self._stack = self._stack[:self._stack_index + 1]
        self._stack.append(undo_op)
        self._stack_index += 1

    def pop(self):
        self._stack_index -= 1

    def pull(self):
        self._stack_index += 1

    def peek(self):
        return self._stack[self._stack_index]

    def size(self):
        return self._stack_index + 1

    def full(self):
        return self._stack_index == len(self._stack) - 1
