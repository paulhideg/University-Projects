#pragma once
#include "repository.h"
#include "Observer.h"

class Service : public Subject {
private:
    Repository& repository;
public:
    Service(Repository& repository1);

    ~Service() = default;

    std::vector<Question> getAllQuestionsService();

    std::vector<User*> getAllUsersService();

    std::vector<Question> getAllQuestionsSortedId();

    std::vector<Question> getAllQuestionsSortedSc();

    void addQuestionService(const std::string& id, const std::string& text, const std::string& answer, const std::string& score);

    //void updateIssueService(const std::string& description, const std::string& newDescription, const std::string& newStatus, const std::string& newReporter, const std::string& newSolver);
};