#pragma once
#include <string>

class User {
private:
    std::string name;
    std::string score;
public:
    User() : name{ "" }, score{ "" }{}

    User(const std::string& name, const std::string& score);

    std::string getName() { return this->name; }

    std::string getScore() { return this->score; }

    ~User() = default;
};

class Question {
private:
    std::string id;
    std::string text;
    std::string answer;
    std::string score;
    
public:
    Question() : id{ ""}, text{""}, answer{""}, score{""}{}

    Question(const std::string& id, const std::string& text, const std::string& answer, const std::string& score);

    std::string getId() { return this->id; };

    std::string getText() { return this->text; };

    std::string getAnswer() { return this->answer; };

    std::string getScore() { return this->score; };

    std::string toString();

    ~Question() = default;
};