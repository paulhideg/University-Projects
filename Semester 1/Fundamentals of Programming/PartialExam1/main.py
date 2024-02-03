from ui import UI
from service import Service
from repo import Repo

if __name__ == '__main__':
    repo = Repo()
    service = Service(repo)
    ui = UI(service)
    ui.run()
