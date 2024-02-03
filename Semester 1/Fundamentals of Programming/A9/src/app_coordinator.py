from ui.ui import UI
from ui.gui import StudentsGUI
from services.student_service import ServiceStudents
from services.discipline_service import ServiceDisciplines
from services.grade_service import ServiceGrades
from services.undo_redo_service import ServiceUndoRedo
from validations.validator import ValidatorStudent, ValidatorDiscipline, ValidatorGrade
from repositories.repositories import RepoStudents, RepoDisciplines, RepoGrades, RepoUndo
from repositories.file_repositories import FileRepoStudents, FileRepoDisciplines, FileRepoGrades
from repositories.binary_repositories import BinaryRepoStudents, BinaryRepoDisciplines, BinaryRepoGrades
# from repositories.json_repositories import
from settings.properties import Settings


class AppCoordination:
    def start(self):
        start_choice = Settings('settings/settings.properties')

        valid_student = ValidatorStudent()
        valid_discipline = ValidatorDiscipline()
        valid_grade = ValidatorGrade()

        repo_students = RepoStudents()
        repo_disciplines = RepoDisciplines()
        repo_grades = RepoGrades()
        repo_undo = RepoUndo()

        servicesUndoRedo = ServiceUndoRedo(repo_undo)

        if start_choice.repository == "files":
            repo_students = FileRepoStudents(start_choice.students_file)
            repo_disciplines = FileRepoDisciplines(
                start_choice.disciplines_file)
            repo_grades = FileRepoGrades(start_choice.grades_file)
        elif start_choice.repository == "binaryfiles":
            repo_students = BinaryRepoStudents(start_choice.students_file)
            repo_disciplines = BinaryRepoDisciplines(
                start_choice.disciplines_file)
            repo_grades = BinaryRepoGrades(start_choice.grades_file)

        servicesStudent = ServiceStudents(
            valid_student, repo_students, repo_undo)
        servicesDiscipline = ServiceDisciplines(
            valid_discipline, repo_disciplines, repo_undo)
        servicesGrade = ServiceGrades(
            valid_grade, valid_student, valid_discipline, repo_grades, repo_students, repo_disciplines, repo_undo)

        if start_choice.repository not in ["files", "binaryfiles"]:
            servicesGrade.random_students_disciplines_grades()

        ui = UI(servicesStudent, servicesDiscipline,
                servicesGrade, servicesUndoRedo)
        if start_choice.ui == "GUI":
            ui = StudentsGUI(servicesStudent, servicesDiscipline,
                             servicesGrade, servicesUndoRedo)

        ui.run()
