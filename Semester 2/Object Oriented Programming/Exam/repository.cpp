#include "repository.h"
#include <fstream>
#include <sstream>
#include <algorithm>

Repository::Repository(std::vector<Question>& questions, std::vector<User*>& users, std::string& questionFile,
    std::string& userFile) {
    this->questions = questions;
    this->users = users;
    this->questionFile = questionFile;
    this->userFile = userFile;
}

std::vector<Question> Repository::getAllQuestionsRepo() {
    return this->questions;
}

std::vector<User*> Repository::getAllUsersRepo() {
    return this->users;
}

std::string Repository::getQuestionsFileRepo() {
    return this->questionFile;
}

std::string Repository::getUserFileRepo() {
    return this->userFile;
}

void Repository::tokenizeUser(std::string readString)
{
    std::string items[10];
    int index = 0;
    std::stringstream ss(readString);
    std::string word;
    while (ss >> word)
    {
        items[index] = word;
        index++;
    }
    User* userToAdd = new User{ items[0], items[1] };
    this->users.push_back(userToAdd);
}

void Repository::loadFromFileUser() {
    if (!this->userFile.empty())
    {
        User userFromFile;
        std::ifstream fin(this->userFile);
        std::string readString;
        User readUser;
        while (std::getline(fin, readString))
        {
            fin.clear();
            this->tokenizeUser(readString);
        }
    }
}

void Repository::tokenizeQuestion(std::string readString)
{
    std::string items[10];
    int index = 0;
    std::stringstream ss(readString);
    std::string word;
    while (ss >> word)
    {
        items[index] = word;
        index++;
    }
    Question questionToAdd{ items[0], items[1], items[2], items[3] };
    this->questions.push_back(questionToAdd);
}

void Repository::loadFromFileQuestion() {
    if (!this->questionFile.empty())
    {
        Question questionFromFile;
        std::ifstream fin(this->questionFile);
        std::string readString;
        Question readQuestion;
        while (std::getline(fin, readString))
        {
            fin.clear();
            this->tokenizeQuestion(readString);
        }
    }
}

void Repository::initialiseRepo() {
    this->loadFromFileQuestion();
    this->loadFromFileUser();
}

int Repository::findById(const std::string& id) {
    int searchedIndex = -1;
    auto it = std::find_if(this->questions.begin(), this->questions.end(), [&id](Question& question) {return question.getId() == id; });
    if (it != this->questions.end())
        searchedIndex = it - this->questions.begin();
    return searchedIndex;
}

void Repository::addQuestionRepo(Question& question) {
    if (question.getId() == "" || question.getText()== "" || question.getAnswer() == "" || question.getScore() == "") {
        throw "Question is empty";
    }
    int existing = this->findById(question.getId());
    
    if (existing != -1)
    {
        throw "The Question is already in the list";
    }
    this->questions.push_back(question);
    this->writeQuestionsToFile();
}

void Repository::writeQuestionsToFile() {
    if (!this->questionFile.empty())
    {
        std::ofstream fout(this->questionFile);
        for (auto movie : this->questions)
        {
            fout << movie.toString() << "\n";
        }
        fout.close();
    }
}

void Repository::updateQuestionRepo(int index, Question& newQuestion) {
    if (index == -1)
    {
        throw "The Question does not exist";
    }
    this->questions[index] = newQuestion;
    this->writeQuestionsToFile();
}

void Repository::writeToFileRepo() {
    this->writeQuestionsToFile();
}






