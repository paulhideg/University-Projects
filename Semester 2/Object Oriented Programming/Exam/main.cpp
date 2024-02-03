#include <iostream>
#include "QApplication"
#include "domain.h"
#include "repository.h"
#include "service.h"
#include "window.h"
#include "QWidget"

int main(int argc, char* argv[]) {
    QApplication a(argc, argv);
    std::vector<Question> vectorQuestions;
    std::string questionFile = R"(C:\Users\paulh\OneDrive\Desktop\OOP_practical\OOP_exam\OOP_exam\questions.txt)";
    std::vector<User*> vectorUsers;
    std::string userFile = R"(C:\Users\paulh\OneDrive\Desktop\OOP_practical\OOP_exam\OOP_exam\users.txt)";
    Repository repository{ vectorQuestions, vectorUsers, questionFile, userFile };
    repository.initialiseRepo();
    Service service{ repository };
    std::vector<Window*> windows;
    for (auto user : service.getAllUsersService())

    {
        auto window = new Window(service, user);
        windows.push_back(window);
    }

    for (auto wnd : windows)
    {
        wnd->show();
    }

    a.exec();
    return 0;
}
