#include "window.h"
#include "ui_Window.h"
#include "QMessageBox"
#include <sstream>
#include <vector>


Window::Window(Service& service,User* user, QWidget *parent) :
        service(service),user(user), QWidget(parent), ui(new Ui::Window) {

    ui->setupUi(this);
    this->window()->setWindowTitle(QString::fromStdString(user->getName()));
    this->populateList();
    this->service.addObserver(this);
    this->update();
    this->connectSignalsAndSlots();

}

Window::~Window() {
    delete ui;
}

void Window::update() {
    populateList();
}

void Window::populateList() {
    this->ui->questionListWidget->clear();
    for(auto& issue: this->service.getAllQuestionsSortedId())
    {
        this->ui->questionListWidget->addItem(QString::fromStdString(issue.toString()));
    }
}

void Window::connectSignalsAndSlots() {
    QObject::connect(this->ui->addPushButton, &QPushButton::clicked, this, &Window::addIssue);
}

void Window::addIssue() {
    std::string id = this->ui->addLineEdit->text().toStdString();
    try
    {
        if(id.empty())
            throw "The id is empty!";
        else if(this->user->getName() == "presenter")
        {
            std::vector<std::string> texts{ "WhatsYourName", "FavoriteMusic", "FavoriteColor", "HowTallAreYou", "AreYouCool", "HowAreYouu", "DoYouLikeToTravel" };
            std::vector<std::string> answers{ "Paul", "HipHop", "Blue", "189centimeters", "Yes", "ImGood", "OfCourse" };
            std::vector<std::string> scores{ "5", "3", "7", "8", "2", "9", "4" };
            int random = rand() % texts.size();
            std::string text = texts[random];
            std::string answer = answers[random];
            std::string score = scores[random];
            this->service.addQuestionService(id, text, answer, score);
            this->populateList();
        }
        else
        {
            throw "Only the presenter cand add an issue!";
        }

    }
    catch(const char *msg) {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(msg);
        error->setWindowTitle("Invalid input!");
        error->exec();
    }
}





