from business.services.activity_service import ActivityService
from business.services.person_service import PersonService
from business.services.undoredo_service import UndoRedoService
from generators.activity_generator import ActivityGenerator
from generators.person_generator import PersonGenerator
from infrastructure.binary_repositories.binary_activity_repo import BinaryActivityRepository
from infrastructure.binary_repositories.binary_person_repo import BinaryPersonRepository
from infrastructure.file_repositories.file_activity_repo import FileActivityRepository
from infrastructure.file_repositories.file_person_repo import FilePersonRepository
from infrastructure.json_repositories.json_activity_repo import JSONActivityRepository
from infrastructure.json_repositories.json_person_repo import JSONPersonRepository
from infrastructure.repositories.activity_repo import ActivityRepository
from infrastructure.repositories.person_repo import PersonRepository
from infrastructure.repositories.undoredo_repo import UndoRedoRepo
from settings.properties import Settings
from ui.console import Console
from ui.gui import ActivityGUI
from validation.activity_validator import ActivityValidator
from validation.person_validator import PersonValidator


class AppCoordination:
    def start(self):
        start_choice = Settings('settings/settings.properties')

        # p_repo = start_choice.get_person_repo()
        # p_validator = PersonValidator()
        # p_service = PersonService(p_repo, p_validator)
        # a_repo = start_choice.get_activity_repo()
        # a_validator = ActivityValidator()
        # a_service = ActivityService(a_repo, p_repo, a_validator)
        # undo_redo_repo = UndoRedoRepo()
        # undo_redo_service = UndoRedoService(undo_redo_repo)
        # ui = start_choice.get_ui(p_service, a_service, undo_redo_service)
        # ui.run()

        p_repo = PersonRepository()
        p_validator = PersonValidator()
        a_repo = ActivityRepository()
        a_validator = ActivityValidator()
        undo_redo_repo = UndoRedoRepo()
        undo_redo_service = UndoRedoService(undo_redo_repo)

        # if start_choice.repository == 'files':
        #     p_repo = FilePersonRepository(start_choice.person_file)
        #     a_repo = FileActivityRepository(start_choice.activity_file)
        # elif start_choice.repository == 'binaryfiles':
        #     p_repo = BinaryPersonRepository(start_choice.person_file)
        #     a_repo = BinaryActivityRepository(start_choice.activity_file)
        # elif start_choice.repository == 'jsonfiles':
        #     p_repo = JSONPersonRepository(start_choice.person_file)
        #     a_repo = JSONActivityRepository(start_choice.activity_file)

        p_repo = PersonRepository()
        if start_choice.repository == "files":
            p_repo = FilePersonRepository(start_choice.person_file)
        elif start_choice.repository == "binaryfiles":
            p_repo = BinaryPersonRepository(start_choice.person_file)
        elif start_choice.repository == "jsonfiles":
            p_repo = JSONPersonRepository(start_choice.person_file)

        a_repo = ActivityRepository()
        if start_choice.repository == "files":
            a_repo = FileActivityRepository(start_choice.activity_file)
        elif start_choice.repository == "binaryfiles":
            a_repo = BinaryActivityRepository(start_choice.activity_file)
        elif start_choice.repository == "jsonfiles":
            a_repo = JSONActivityRepository(start_choice.activity_file)

        p_service = PersonService(p_repo, p_validator)
        a_service = ActivityService(a_repo, p_repo, a_validator)

        if start_choice.repository not in ['files', 'binaryfiles', 'jsonfiles']:
            p_gen = PersonGenerator(p_service, undo_redo_service)
            p_gen.generate_people()
            a_gen = ActivityGenerator(a_service, p_service, undo_redo_service)
            a_gen.generate_activities()

        ui = Console(p_service, a_service, undo_redo_service)
        if start_choice.ui == "GUI":
            ui = ActivityGUI(p_service, a_service, undo_redo_service)

        ui.run()
