#include "domain.h"

User::User(const std::string& name, const std::string& score) {
    this->name = name;
    this->score = score;
}

Question::Question(const std::string& id, const std::string& text, const std::string& answer, const std::string& score) {
    this->id = id;
    this->text = text;
    this->answer = answer;
    this->score = score;
}

std::string Question::toString() {
    return this->id + " " + this->text + " " + this->answer + " " + this->score;
}
