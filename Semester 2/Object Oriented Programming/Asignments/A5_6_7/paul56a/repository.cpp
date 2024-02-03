#include "repository.h"


int Tutorial_Repo::find(const std::string& link) {

    for (int i = 0; i < this->dynamic_array.get_size(); i++)
        if (this->dynamic_array.elements[i].get_link() == link)
            return i;
    return -1;
}

void Tutorial_Repo::add(Tutorial tutorial)
{
    if (find(tutorial.get_link()) != -1)
        throw RepoError("Tutorial already exists");
    this->dynamic_array.append_array(tutorial);
    ///this->dynamic_array + tutorial;
    ///this->dynamic_array = tutorial + this->dynamic_array;
}

void Tutorial_Repo::remove(const std::string& link) {

    int index = find(link);
    if (index == -1)
        throw RepoError("Tutorial doesn't exist");
    this->dynamic_array.remove_array(index);
}

void Tutorial_Repo::update(Tutorial tutorial) {

    int index = find(tutorial.get_link());
    if (index == -1)
        throw RepoError("Tutorial doesn't exist");
    this->dynamic_array.update_array(index, tutorial);
}

Tutorial* Tutorial_Repo::get_all_tutorials() {

    return this->dynamic_array.get_all_elements();
}

int Tutorial_Repo::get_tutorial_number() {
    return this->dynamic_array.get_size();
}


