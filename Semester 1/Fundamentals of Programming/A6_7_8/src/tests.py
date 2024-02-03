import unittest
from domain.student import Student
from domain.discipline import Discipline
from domain.grade import Grade
from repositories.repositories import RepoStudents, RepoDisciplines, RepoGrades, RepoUndo
from services.student_service import ServiceStudents
from services.discipline_service import ServiceDisciplines
from services.grade_service import ServiceGrades
from validations.validator import ValidatorStudent, ValidatorDiscipline, ValidatorGrade
from errors.exceptions import ValidationError, RepositoryError


class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        """
        Runs before every test method
        """
        pass

    def tearDown(self) -> None:
        """
        Runs after every test method
        """
        pass

    def test_run_student_creation_tests(self):
        student_id = 5
        name = "Jake"
        student = Student(student_id, name)
        assert(student.get_student_id() == student_id)
        assert(student.get_name() == name)
        assert(str(student) == "Student with id 5 and name: Jake")

        name2 = "Mike"
        student.set_name(name2)
        self.assertEqual(student.get_student_id(), student_id)
        self.assertEqual(student.get_name(), name2)

    def test_run_student_validation_tests(self):
        student_id = 5
        name = "Jake"
        student = Student(student_id, name)
        valid = ValidatorStudent()
        valid.validate(student)

        invalid_student_id = -2
        invalid_name = ""
        student_invalid_id = Student(invalid_student_id, name)
        valid = ValidatorStudent()
        try:
            valid.validate(student_invalid_id)

        except ValidationError as ve:
            assert(str(ve) == "invalid student id\n")

        student_invalid = Student(invalid_student_id, invalid_name)
        try:
            valid.validate(student_invalid)

        except ValidationError as ve:
            assert(str(ve) == "invalid student id\ninvalid name\n")

    def test_run_student_repo_add_tests(self):
        student_id = 21
        name = "Jake"
        student = Student(student_id, name)
        repo = RepoStudents()
        assert(len(repo) == 0)
        # or
        assert(repo.__len__() == 0)
        repo.add_student(student)
        assert(len(repo) == 1)
        found_student = repo.search_by_id(student_id)
        assert(found_student == student)
        assert(found_student.get_student_id() == student.get_student_id())
        assert(found_student.get_name() == student.get_name())

        inexistent_id = 23
        try:
            found_student = repo.search_by_id(inexistent_id)

        except RepositoryError as re:
            assert(str(re) == "inexistent student id")

        other_name = "Mike"
        student_same_id = Student(student_id, other_name)
        try:
            found_student = repo.add_student(student_same_id)

        except RepositoryError as re:
            assert(str(re) == "student id already registered")

    def test_run_student_repo_random_students_tests(self):
        repo = RepoStudents()
        repo.random_students()
        assert(len(repo.get_all_students()) == 20)

    def test_run_student_repo_remove_tests(self):
        student_id = 1
        name = "Jake"
        student = Student(student_id, name)
        repo = RepoStudents()
        repo.add_student(student)
        repo.remove_student(student_id)

        # invalid remove
        inexistent_student_id = 2000
        try:
            repo.remove_student(inexistent_student_id)

        except RepositoryError as re:
            assert(str(re) == "inexistent student id")

    def test_run_student_repo_update_tests(self):
        student_id = 1
        name = "Jake"
        student = Student(student_id, name)
        repo = RepoStudents()
        repo.add_student(student)
        updated_name = "Nate"
        repo.update_student(1, updated_name)

        # inexistent id update
        inexistent_student_id = 500
        try:
            repo.update_student(inexistent_student_id, updated_name)

        except RepositoryError as re:
            assert(str(re) == "inexistent student id")

    def test_run_student_repo_search_tests(self):
        student_id = 1
        name = "Jake"
        student = Student(student_id, name)
        repo = RepoStudents()
        repo.add_student(student)
        student_id = 10
        name = "Blake"
        student2 = Student(student_id, name)
        repo.add_student(student2)
        student_id = 21
        name = "Nate"
        student3 = Student(student_id, name)
        repo.add_student(student3)
        student_id = 3
        name = "Josh"
        student4 = Student(student_id, name)
        repo.add_student(student4)
        student_id = 4
        name = "Chris"
        student5 = Student(student_id, name)
        repo.add_student(student5)
        # search for "ake"
        search_result = repo.search_students("ake")
        # there are also added 2 messages at the beginningof the list
        assert(len(search_result) == 4)
        assert(search_result[0] == '')
        assert(search_result[1] == str(2) + " student(s) found:")
        assert(search_result[2] == student)
        assert(search_result[3] == student2)

        # search for "y"
        # returns no students
        search_result = repo.search_students("y")
        assert(len(search_result) == 1)
        assert(search_result[0] == "No students fit the criteria")

    def test_run_student_service_add_tests(self):
        student_id = 21
        name = "Jake"
        repo = RepoStudents()
        valid = ValidatorStudent()
        repo_undo = RepoUndo()
        srv = ServiceStudents(valid, repo, repo_undo)
        assert(srv.nr_of_students() == 0)
        srv.add_student(student_id, name)
        assert(srv.nr_of_students() == 1)

        other_name = "Mike"
        try:
            srv.add_student(student_id, other_name)

        except RepositoryError as re:
            assert(str(re) == "student id already registered")

        invalid_student_id = -2
        invalid_name = ""
        try:
            srv.add_student(invalid_student_id, invalid_name)

        except ValidationError as ve:
            assert(str(ve) == "invalid student id\ninvalid name\n")

    def test_run_student_service_update_tests(self):
        student_id = 21
        name = "Jake"
        repo = RepoStudents()
        valid = ValidatorStudent()
        srv = ServiceStudents(valid, repo)
        assert(srv.nr_of_students() == 0)
        srv.add_student(student_id, name)
        updated_name = "Mike"
        srv.update_student(student_id, updated_name)

    def test_run_student_service_get_all_tests(self):
        student_id = 21
        name = "Jake"
        repo = RepoStudents()
        valid = ValidatorStudent()
        srv = ServiceStudents(valid, repo)
        assert(srv.nr_of_students() == 0)
        srv.add_student(student_id, name)
        assert(len(repo) == 1)
        student_id = 20
        name = "Karl"
        srv.add_student(student_id, name)
        assert(len(repo) == 2)
        students = srv.get_all_students()
        assert(len(students) == 2)

    def test_run_student_service_search_tests(self):
        student_id = 21
        name = "Jake"
        repo = RepoStudents()
        valid = ValidatorStudent()
        srv = ServiceStudents(valid, repo)
        assert(srv.nr_of_students() == 0)
        srv.add_student(student_id, name)
        assert(srv.nr_of_students() == 1)
        student_id = 20
        name = "Caleb"
        srv.add_student(student_id, name)
        search_result = srv.search_students("j")
        # also adds 2 items in the beginning of the list if it finds a student
        assert(len(search_result) == 3)


class TestsDiscipline(unittest.TestCase):

    def setUp(self) -> None:
        """
        Runs before every test method
        """
        self._repo = RepoDisciplines

    def tearDown(self) -> None:
        """
        Runs after every test method
        """
        pass

    def test_run_discipline_creation_tests(self):
        discipline_id = 1
        name = "Math"
        discipline = Discipline(discipline_id, name)
        assert(discipline.get_discipline_id() == discipline_id)
        assert(discipline.get_name() == name)
        assert(str(discipline) == "Discipline with id 1 and name: Math")

        name_changed = "FP"
        discipline.set_name(name_changed)
        assert(discipline.get_name() == name_changed)

        discipline_id2 = 2
        name2 = "Physics"
        discipline2 = Discipline(discipline_id2, name2)
        assert(discipline2.get_discipline_id() == discipline_id2)
        assert(discipline2.get_name() == name2)

    def test_run_discipline_validation_tests(self):
        discipline_id = 1
        name = "Math"
        discipline = Discipline(discipline_id, name)
        valid = ValidatorDiscipline()
        valid.validate(discipline)

        invalid_discipline_id = -3
        invalid_name = ""
        discipline_invalid_id = Discipline(invalid_discipline_id, name)
        try:
            valid.validate(discipline_invalid_id)

        except ValidationError as ve:
            assert(str(ve) == "invalid discipline id\n")

        discipline_invalid = Discipline(invalid_discipline_id, invalid_name)
        try:
            valid.validate(discipline_invalid)

        except ValidationError as ve:
            assert(str(ve) == "invalid discipline id\ninvalid name\n")

    def test_run_discipline_add_repo_tests(self):
        discipline_id = 21
        name = "Maths"
        discipline = Discipline(discipline_id, name)
        repo = RepoDisciplines()
        assert(len(repo) == 0)
        # or
        assert(repo.__len__() == 0)
        repo.add_discipline(discipline)
        assert(len(repo) == 1)
        found_discipline = repo.search_by_id(discipline_id)
        assert(found_discipline == discipline)
        assert(found_discipline.get_discipline_id()
               == discipline.get_discipline_id())
        assert(found_discipline.get_name() == discipline.get_name())

        inexistent_id = 22
        try:
            found_discipline = repo.search_by_id(inexistent_id)

        except RepositoryError as re:
            assert(str(re) == "inexistent discipline id")

        other_name = "English"
        discipline_same_id = Discipline(discipline_id, other_name)
        try:
            found_discipline = repo.add_discipline(discipline_same_id)

        except RepositoryError as re:
            assert(str(re) == "discipline id already registered")

    def test_run_discipline_repo_random_disciplines_tests(self):
        repo = RepoDisciplines()
        repo.random_disciplines()
        assert(len(repo.get_all_disciplines()) == 20)

    def test_run_discipline_repo_remove_tests(self):
        discipline_id = 1
        name = "Maths"
        discipline = Discipline(discipline_id, name)
        repo = RepoDisciplines()
        repo.add_discipline(discipline)
        repo.remove_discipline(discipline_id)

        # invalid remove
        inexistent_discipline_id = 2000
        try:
            repo.remove_discipline(inexistent_discipline_id)

        except RepositoryError as re:
            assert(str(re) == "inexistent discipline id")

    def test_run_discipline_repo_update_tests(self):
        discipline_id = 1
        name = "Maths"
        discipline = Discipline(discipline_id, name)
        repo = RepoDisciplines()
        repo.add_discipline(discipline)
        updated_name = "FP"
        repo.update_discipline(1, updated_name)

        # inexistent id update
        inexistent_discipline_id = 1000
        try:
            repo.update_discipline(inexistent_discipline_id, updated_name)

        except RepositoryError as re:
            assert(str(re) == "inexistent id")

    def test_run_discipline_repo_search_tests(self):
        discipline_id = 1
        name = "Maths"
        discipline = Discipline(discipline_id, name)
        repo = RepoDisciplines()
        repo.add_discipline(discipline)
        discipline_id = 21
        name = "Romanian"
        discipline2 = Discipline(discipline_id, name)
        repo.add_discipline(discipline2)
        discipline_id = 10
        name = "ASC"
        discipline3 = Discipline(discipline_id, name)
        repo.add_discipline(discipline3)
        discipline_id = 2
        name = "Logic"
        discipline4 = Discipline(discipline_id, name)
        repo.add_discipline(discipline4)
        discipline_id = 5
        name = "Algebra"
        discipline5 = Discipline(discipline_id, name)
        repo.add_discipline(discipline5)
        # search for "o"
        search_result = repo.search_disciplines("o")
        # there are also added 2 messages at the beginningof the list
        assert(len(search_result) == 4)
        assert(search_result[0] == '')
        assert(search_result[1] == str(2) + " discipline(s) found:")
        assert(search_result[2] == discipline2)
        assert(search_result[3] == discipline4)

        # search for "y"
        # returns no disciplines
        search_result = repo.search_disciplines("y")
        assert(len(search_result) == 1)
        assert(search_result[0] == "No disciplines fit the criteria")

    def test_run_discipline_add_service_tests(self):
        discipline_id = 21
        name = "Math"
        repo = RepoDisciplines()
        valid = ValidatorDiscipline()
        srv = ServiceDisciplines(valid, repo)
        assert(srv.nr_of_disciplines() == 0)
        srv.add_discipline(discipline_id, name)
        assert(srv.nr_of_disciplines() == 1)

        other_name = "Sports"
        try:
            srv.add_discipline(discipline_id, other_name)

        except RepositoryError as re:
            assert(str(re) == "discipline id already registered")

        invalid_discipline_id = -2
        invalid_name = ""
        try:
            srv.add_discipline(invalid_discipline_id, invalid_name)

        except ValidationError as ve:
            assert(str(ve) == "invalid discipline id\ninvalid name\n")

    def test_run_discipline_service_update_tests(self):
        discipline_id = 21
        name = "Math"
        repo = RepoDisciplines()
        valid = ValidatorDiscipline()
        srv = ServiceDisciplines(valid, repo)
        assert(srv.nr_of_disciplines() == 0)
        srv.add_discipline(discipline_id, name)
        assert(srv.nr_of_disciplines() == 1)
        new_name = "FP"
        srv.update_discipline(discipline_id, new_name)

    def test_run_discipline_service_get_all_tests(self):
        discipline_id = 21
        name = "Math"
        repo = RepoDisciplines()
        valid = ValidatorDiscipline()
        srv = ServiceDisciplines(valid, repo)
        assert(srv.nr_of_disciplines() == 0)
        srv.add_discipline(discipline_id, name)
        assert(srv.nr_of_disciplines() == 1)
        discipline_id = 20
        name = "Biology"
        srv.add_discipline(discipline_id, name)
        assert(len(repo) == 2)
        disciplines = srv.get_all_disciplines()
        assert(len(disciplines) == 2)

    def test_run_discipline_service_search_tests(self):
        discipline_id = 21
        name = "Math"
        repo = RepoDisciplines()
        valid = ValidatorDiscipline()
        srv = ServiceDisciplines(valid, repo)
        assert(srv.nr_of_disciplines() == 0)
        srv.add_discipline(discipline_id, name)
        assert(srv.nr_of_disciplines() == 1)
        discipline_id = 20
        name = "Biology"
        srv.add_discipline(discipline_id, name)
        assert(len(repo) == 2)
        search_result = srv.search_disciplines("m")
        # also adds 2 items in the beginning of the list if it finds a discipline
        assert(len(search_result) == 3)


class TestsGrade(unittest.TestCase):
    def setUp(self) -> None:
        """
        Runs before every test method
        """
        self.__service_grades = ServiceGrades(ValidatorGrade(), ValidatorStudent(
        ), ValidatorDiscipline(), RepoGrades(), RepoStudents(), RepoDisciplines())

    def tearDown(self) -> None:
        """
        Runs after every test method
        """
        pass

    def test_run_grade_creation_value(self):
        discipline_id = 1
        student_id = 5
        grade_value = 2
        grade = Grade(student_id, discipline_id, grade_value)
        assert(grade.get_discipline_id() == discipline_id)
        assert(grade.get_student_id() == student_id)
        assert(grade.get_grade_value() == [grade_value])
        assert(str(grade) == str("Student id: " + str(student_id) + "   Discipline id: " +
               str(discipline_id) + "   Has grade(s): " + str([grade_value])))

        grade_value2 = 4
        grade.set_grade_value(grade_value2)
        assert(grade.get_discipline_id() == discipline_id)
        assert(grade.get_student_id() == student_id)
        assert(grade.get_grade_value() == [grade_value, grade_value2])

    def test_run_grade_validation_tests(self):
        student_id = 5
        discipline_id = 1
        grade_value = 2
        grade = Grade(discipline_id, student_id, grade_value)
        valid = ValidatorGrade()
        valid.validate(grade, grade_value)

        invalid_student_id = -2
        invalid_discipline_id = -3
        invalid_grade_value = 0
        grade_invalid = Grade(invalid_student_id,
                              invalid_discipline_id, invalid_grade_value)
        try:
            valid.validate(grade_invalid, invalid_grade_value)

        except ValidationError as ve:
            assert(
                str(ve) == "invalid student id\ninvalid discipline id\ninvalid grade\n")

    def test_run_grade_repo_add_tests(self):
        student_id = 12
        student_name = "Jake"
        discipline_id = 21
        discipline_name = "Maths"
        grade_value = 5
        student = Student(student_id, student_name)
        discipline = Discipline(discipline_id, discipline_name)
        grade = Grade(student, discipline, grade_value)
        repo = RepoGrades()
        assert(len(repo) == 0)
        # or
        assert(repo.__len__() == 0)
        repo.add_grade(student, discipline, grade, grade_value)
        assert(len(repo) == 1)

        another_grade_value = 10
        grade_same_id_s = Grade(student_id, discipline_id, another_grade_value)
        repo.add_grade(student, discipline, grade, another_grade_value)
        assert(len(repo) == 1)

    def test_run_grade_repo_random_grades_tests(self):
        repo = RepoGrades()
        repo.random_grades()
        assert(len(repo.get_all_grades()) == 400)

    def test_run_grade_repo_remove_tests(self):
        student_id = 1
        student_name = "Jake"
        discipline_id = 4
        discipline_name = "Maths"
        grade_value = 5
        student = Student(student_id, student_name)
        discipline = Discipline(discipline_id, discipline_name)
        grade = Grade(student, discipline, grade_value)
        repo = RepoGrades()
        repo.add_grade(student, discipline, grade, grade_value)
        assert(len(repo) == 1)
        student_id = 3
        student_name = "Mike"
        discipline_id = 2
        discipline_name = "FP"
        grade_value2 = 6
        student2 = Student(student_id, student_name)
        discipline2 = Discipline(discipline_id, discipline_name)
        grade2 = Grade(student2, discipline2, grade_value2)
        repo.add_grade(student2, discipline2, grade2, grade_value2)
        assert(len(repo) == 2)

        # remove by student id
        repo.remove_grades_student(1)
        assert(len(repo) == 2)
        repo.remove_grades_discipline(2)
        assert(len(repo) == 2)

    def test_run_grade_repo_students_failing_tests(self):
        student_id = 1
        student_name = "Jake"
        discipline_id = 4
        discipline_name = "Maths"
        grade_value = 4
        student = Student(student_id, student_name)
        discipline = Discipline(discipline_id, discipline_name)
        grade = Grade(student, discipline, grade_value)
        repo = RepoGrades()
        repo.add_grade(student, discipline, grade, grade_value)
        assert(len(repo) == 1)
        failing_students = repo.students_failing()
        assert(len(failing_students) == 1)

    def test_run_grade_repo_top_students_tests(self):
        student_id = 1
        student_name = "Jake"
        discipline_id = 4
        discipline_name = "Maths"
        grade_value = 4
        student = Student(student_id, student_name)
        discipline = Discipline(discipline_id, discipline_name)
        grade = Grade(student, discipline, grade_value)
        repo = RepoGrades()
        repo.add_grade(student, discipline, grade, grade_value)
        student_id = 2
        student_name = "Matt"
        discipline_id = 4
        discipline_name = "Maths"
        grade_value = 10
        student = Student(student_id, student_name)
        discipline = Discipline(discipline_id, discipline_name)
        grade2 = Grade(student, discipline, grade_value)
        repo.add_grade(student, discipline, grade2, grade_value)
        assert(len(repo) == 2)
        top_students = repo.students_top()
        assert(len(top_students) == 2)

    def test_run_grade_repo_highest_disciplines_tests(self):
        student_id = 1
        student_name = "Jake"
        discipline_id = 3
        discipline_name = "FP"
        grade_value = 4
        student = Student(student_id, student_name)
        discipline = Discipline(discipline_id, discipline_name)
        grade = Grade(student, discipline, grade_value)
        repo = RepoGrades()
        repo.add_grade(student, discipline, grade, grade_value)
        student_id = 2
        student_name = "Matt"
        discipline_id = 5
        discipline_name = "Maths"
        grade_value = 10
        student = Student(student_id, student_name)
        discipline = Discipline(discipline_id, discipline_name)
        grade2 = Grade(student, discipline, grade_value)
        repo.add_grade(student, discipline, grade2, grade_value)
        assert(len(repo) == 2)
        highest_disciplines = repo.disciplines_highest()
        assert(len(highest_disciplines) == 2)

    def test_run_grade_service_init_tests(self):
        valid_student = ValidatorStudent()
        valid_discipline = ValidatorDiscipline()
        valid_grade = ValidatorGrade()
        repo_students = RepoStudents()
        repo_disciplines = RepoDisciplines()
        repo_grades = RepoGrades()
        ServiceGrades(
            valid_grade, valid_student, valid_discipline, repo_grades, repo_students, repo_disciplines)

    def test_run_grade_service_random_grades_tests(self):
        valid_student = ValidatorStudent()
        valid_discipline = ValidatorDiscipline()
        valid_grade = ValidatorGrade()
        repo_students = RepoStudents()
        repo_disciplines = RepoDisciplines()
        repo_grades = RepoGrades()
        servicesGrade = ServiceGrades(
            valid_grade, valid_student, valid_discipline, repo_grades, repo_students, repo_disciplines)
        student_id = 1
        student_name = "Jake"
        student = Student(student_id, student_name)
        repo_students.add_student(student)
        discipline_id = 1
        discipline_name = "Maths"
        discipline = Discipline(discipline_id, discipline_name)
        repo_disciplines.add_discipline(discipline)
        grade_value = 5
        servicesGrade.add_grade(student_id, discipline_id, grade_value)
        assert(len(repo_grades) == 1)

    def test_run_grade_service_remove_student_tests(self):
        valid_student = ValidatorStudent()
        valid_discipline = ValidatorDiscipline()
        valid_grade = ValidatorGrade()
        repo_students = RepoStudents()
        repo_disciplines = RepoDisciplines()
        repo_grades = RepoGrades()
        servicesGrade = ServiceGrades(
            valid_grade, valid_student, valid_discipline, repo_grades, repo_students, repo_disciplines)
        student_id = 1
        student_name = "Jake"
        student = Student(student_id, student_name)
        repo_students.add_student(student)
        assert(len(repo_students) == 1)
        discipline_id = 1
        discipline_name = "Maths"
        discipline = Discipline(discipline_id, discipline_name)
        repo_disciplines.add_discipline(discipline)
        assert(len(repo_disciplines) == 1)
        grade_value = 5
        servicesGrade.add_grade(student_id, discipline_id, grade_value)
        assert(len(repo_grades) == 1)
        servicesGrade.remove_student(student_id)
        assert(len(repo_grades) == 0)
        assert(len(repo_students) == 0)
        assert(len(repo_disciplines) == 1)

    def test_run_grade_service_remove_discipline_tests(self):
        valid_student = ValidatorStudent()
        valid_discipline = ValidatorDiscipline()
        valid_grade = ValidatorGrade()
        repo_students = RepoStudents()
        repo_disciplines = RepoDisciplines()
        repo_grades = RepoGrades()
        servicesGrade = ServiceGrades(
            valid_grade, valid_student, valid_discipline, repo_grades, repo_students, repo_disciplines)
        student_id = 1
        student_name = "Jake"
        student = Student(student_id, student_name)
        repo_students.add_student(student)
        assert(len(repo_students) == 1)
        discipline_id = 1
        discipline_name = "Maths"
        discipline = Discipline(discipline_id, discipline_name)
        repo_disciplines.add_discipline(discipline)
        assert(len(repo_disciplines) == 1)
        grade_value = 5
        servicesGrade.add_grade(student_id, discipline_id, grade_value)
        assert(len(repo_grades) == 1)
        servicesGrade.remove_discipline(discipline_id)
        assert(len(repo_grades) == 0)
        assert(len(repo_students) == 1)
        assert(len(repo_disciplines) == 0)

    def test_run_grade_service_students_failing_tests(self):
        valid_student = ValidatorStudent()
        valid_discipline = ValidatorDiscipline()
        valid_grade = ValidatorGrade()
        repo_students = RepoStudents()
        repo_disciplines = RepoDisciplines()
        repo_grades = RepoGrades()
        servicesGrade = ServiceGrades(
            valid_grade, valid_student, valid_discipline, repo_grades, repo_students, repo_disciplines)
        student_id = 1
        student_name = "Jake"
        student = Student(student_id, student_name)
        repo_students.add_student(student)
        assert(len(repo_students) == 1)
        discipline_id = 1
        discipline_name = "Maths"
        discipline = Discipline(discipline_id, discipline_name)
        repo_disciplines.add_discipline(discipline)
        assert(len(repo_disciplines) == 1)
        grade_value = 5
        servicesGrade.add_grade(student_id, discipline_id, grade_value)

        student_id = 2
        student_name = "Carl"
        student2 = Student(student_id, student_name)
        repo_students.add_student(student2)
        assert(len(repo_students) == 2)
        discipline_id = 2
        discipline_name = "Business"
        discipline2 = Discipline(discipline_id, discipline_name)
        repo_disciplines.add_discipline(discipline2)
        assert(len(repo_disciplines) == 2)
        grade_value = 4
        servicesGrade.add_grade(student_id, discipline_id, grade_value)

        students_failing = servicesGrade.students_failing()
        assert(len(students_failing) == 1)

    def test_run_grade_service_top_students_tests(self):
        valid_student = ValidatorStudent()
        valid_discipline = ValidatorDiscipline()
        valid_grade = ValidatorGrade()
        repo_students = RepoStudents()
        repo_disciplines = RepoDisciplines()
        repo_grades = RepoGrades()
        servicesGrade = ServiceGrades(
            valid_grade, valid_student, valid_discipline, repo_grades, repo_students, repo_disciplines)
        student_id = 1
        student_name = "Jake"
        student = Student(student_id, student_name)
        repo_students.add_student(student)
        assert(len(repo_students) == 1)
        discipline_id = 1
        discipline_name = "Maths"
        discipline = Discipline(discipline_id, discipline_name)
        repo_disciplines.add_discipline(discipline)
        assert(len(repo_disciplines) == 1)
        grade_value = 5
        servicesGrade.add_grade(student_id, discipline_id, grade_value)

        student_id = 2
        student_name = "Carl"
        student2 = Student(student_id, student_name)
        repo_students.add_student(student2)
        assert(len(repo_students) == 2)
        discipline_id = 2
        discipline_name = "Business"
        discipline2 = Discipline(discipline_id, discipline_name)
        repo_disciplines.add_discipline(discipline2)
        assert(len(repo_disciplines) == 2)
        grade_value = 4
        servicesGrade.add_grade(student_id, discipline_id, grade_value)

        students_top = servicesGrade.students_top()
        assert(len(students_top) == 2)

    def test_run_grade_service_highest_disciplines_tests(self):
        valid_student = ValidatorStudent()
        valid_discipline = ValidatorDiscipline()
        valid_grade = ValidatorGrade()
        repo_students = RepoStudents()
        repo_disciplines = RepoDisciplines()
        repo_grades = RepoGrades()
        servicesGrade = ServiceGrades(
            valid_grade, valid_student, valid_discipline, repo_grades, repo_students, repo_disciplines)
        student_id = 1
        student_name = "Jake"
        student = Student(student_id, student_name)
        repo_students.add_student(student)
        assert(len(repo_students) == 1)
        discipline_id = 1
        discipline_name = "Maths"
        discipline = Discipline(discipline_id, discipline_name)
        repo_disciplines.add_discipline(discipline)
        assert(len(repo_disciplines) == 1)
        grade_value = 5
        servicesGrade.add_grade(student_id, discipline_id, grade_value)

        student_id = 2
        student_name = "Carl"
        student2 = Student(student_id, student_name)
        repo_students.add_student(student2)
        assert(len(repo_students) == 2)
        discipline_id = 2
        discipline_name = "Business"
        discipline2 = Discipline(discipline_id, discipline_name)
        repo_disciplines.add_discipline(discipline2)
        assert(len(repo_disciplines) == 2)
        grade_value = 4
        servicesGrade.add_grade(student_id, discipline_id, grade_value)

        disciplines_highest = servicesGrade.disciplines_highest()
        assert(len(disciplines_highest) == 2)

    def test_run_grade_service_nr_of_grades_tests(self):
        valid_student = ValidatorStudent()
        valid_discipline = ValidatorDiscipline()
        valid_grade = ValidatorGrade()
        repo_students = RepoStudents()
        repo_disciplines = RepoDisciplines()
        repo_grades = RepoGrades()
        servicesGrade = ServiceGrades(
            valid_grade, valid_student, valid_discipline, repo_grades, repo_students, repo_disciplines)
        servicesGrade.random_students_disciplines_grades()
        all_grades = servicesGrade.nr_of_grades()
        assert(all_grades == 400)

    def test_run_grade_service_get_all_tests(self):
        valid_student = ValidatorStudent()
        valid_discipline = ValidatorDiscipline()
        valid_grade = ValidatorGrade()
        repo_students = RepoStudents()
        repo_disciplines = RepoDisciplines()
        repo_grades = RepoGrades()
        servicesGrade = ServiceGrades(
            valid_grade, valid_student, valid_discipline, repo_grades, repo_students, repo_disciplines)
        servicesGrade.random_students_disciplines_grades()
        all_grades = servicesGrade.get_all_grades()
        assert(len(all_grades) == 400)


if __name__ == "__main__":
    unittest.main()
