#include "service.h"
#include "algorithm"

bool sortQuestionId(Question question1, Question question2)
{
    if (stoi(question1.getId()) < stoi(question2.getId()))
        return true;
    else
        return false;
}

bool sortQuestionScore(Question question1, Question question2)
{
    if (stoi(question1.getScore()) > stoi(question2.getScore()))
        return true;
    else
        return false;
}

Service::Service(Repository& repository1) :repository(repository1) {

}

std::vector<Question> Service::getAllQuestionsService() {
    return this->repository.getAllQuestionsRepo();
}

std::vector<User*> Service::getAllUsersService() {
    return this->repository.getAllUsersRepo();
}

std::vector<Question> Service::getAllQuestionsSortedId() {
    std::vector<Question> vector;
    vector = this->repository.getAllQuestionsRepo();
    std::sort(vector.begin(), vector.end(), sortQuestionId);
    return vector;
}

std::vector<Question> Service::getAllQuestionsSortedSc() {
    std::vector<Question> vector;
    vector = this->repository.getAllQuestionsRepo();
    std::sort(vector.begin(), vector.end(), sortQuestionScore);
    return vector;
}

void Service::addQuestionService(const std::string& id, const std::string& text, const std::string& answer, const std::string& score) {
    Question question = Question(id, text, answer, score);
    this->repository.addQuestionRepo(question);
    notify();
}




