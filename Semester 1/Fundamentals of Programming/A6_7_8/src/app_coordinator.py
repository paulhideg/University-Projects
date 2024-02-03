from ui.ui import UI
from ui.gui import StudentsGUI
from services.student_service import ServiceStudents
from services.discipline_service import ServiceDisciplines
from services.grade_service import ServiceGrades
from services.undo_redo_service import ServiceUndoRedo
from validations.validator import ValidatorStudent, ValidatorDiscipline, ValidatorGrade
from repositories.repositories import RepoStudents, RepoDisciplines, RepoGrades, RepoUndo


class AppCoordination:
    def start(self):
        valid_student = ValidatorStudent()
        valid_discipline = ValidatorDiscipline()
        valid_grade = ValidatorGrade()

        repo_students = RepoStudents()
        repo_disciplines = RepoDisciplines()
        repo_grades = RepoGrades()
        repo_undo = RepoUndo()

        servicesStudent = ServiceStudents(
            valid_student, repo_students, repo_undo)
        servicesDiscipline = ServiceDisciplines(
            valid_discipline, repo_disciplines, repo_undo)
        servicesGrade = ServiceGrades(
            valid_grade, valid_student, valid_discipline, repo_grades, repo_students, repo_disciplines, repo_undo)
        servicesUndoRedo = ServiceUndoRedo(repo_undo)

        ui = UI(servicesStudent, servicesDiscipline,
                servicesGrade, servicesUndoRedo)
        gui = StudentsGUI(servicesStudent, servicesDiscipline,
                          servicesGrade, servicesUndoRedo)

        choice = input("Press 1 for console UI, 2 for GUI>>")
        if choice == '1':
            ui.run()
        elif choice == '2':
            gui.start()
        else:
            print("Bad command")
