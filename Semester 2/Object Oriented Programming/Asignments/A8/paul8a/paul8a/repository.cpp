#include "repository.h"


int Tutorial_Repo::find(const std::string& link) {

    std::vector<Tutorial> the_tutorials = this->dynamic_array;
    for (auto& tutorial: dynamic_array)
        if (tutorial.get_link() == link)
            return &tutorial - &dynamic_array[0];
    return -1;
}

void Tutorial_Repo::add(Tutorial tutorial)
{
    if (find(tutorial.get_link()) != -1)
        throw RepoError("Tutorial already exists");
    this->dynamic_array.push_back(tutorial);
    ///this->dynamic_array + tutorial;
    ///this->dynamic_array = tutorial + this->dynamic_array;
}

void Tutorial_Repo::remove(const std::string& link) {

    int index = find(link);
    if (index == -1)
        throw RepoError("Tutorial doesn't exist");
    this->dynamic_array.erase(this->dynamic_array.begin() + index);
}

void Tutorial_Repo::update(Tutorial tutorial) {

    int index = find(tutorial.get_link());
    if (index == -1)
        throw RepoError("Tutorial doesn't exist");
    this->dynamic_array[index] = tutorial;
}

std::vector<Tutorial> Tutorial_Repo::get_all_tutorials() {

    return this->dynamic_array;
}

int Tutorial_Repo::get_tutorial_number() {
    return this->dynamic_array.size();
}


