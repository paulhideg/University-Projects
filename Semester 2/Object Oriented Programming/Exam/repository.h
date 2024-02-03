#pragma once
#include <vector>
#include "domain.h"

class Repository {
private:
    std::vector<Question> questions;
    std::string userFile;
    std::vector<User*> users;
    std::string questionFile;

public:
    Repository(std::vector<Question>& questions, std::vector<User*>& users, std::string& questionFile, std::string& userFile);

    std::vector<Question> getAllQuestionsRepo();

    std::vector<User*> getAllUsersRepo();

    std::string getQuestionsFileRepo();

    std::string getUserFileRepo();

    void tokenizeUser(std::string readString);

    void loadFromFileUser();

    void tokenizeQuestion(std::string readString);

    void loadFromFileQuestion();

    void initialiseRepo();

    int findById(const std::string& id);

    void addQuestionRepo(Question& question);

    void updateQuestionRepo(int index, Question& newQuestion);

    void writeQuestionsToFile();

    void writeToFileRepo();

    ~Repository() = default;
};
