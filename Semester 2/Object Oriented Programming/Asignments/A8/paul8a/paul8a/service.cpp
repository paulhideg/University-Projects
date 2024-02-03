//
// Created by Alen on 16/03/2022.
//

#include "service.h"


void Tutorial_Service::add_tutorial(std::string link, std::string title, std::string presenter, std::string duration, unsigned int likes_number) {

    Tutorial tutorial(link, title, presenter, duration, likes_number);
    this->tutorial_validator.validate_tutorial(link, title, presenter, duration);
    this->tutorial_repo.add(tutorial);
}

void Tutorial_Service::remove_tutorial(const std::string& link) {

    this->tutorial_validator.validate_link(link);
    this->tutorial_repo.remove(link);
}

void Tutorial_Service::update_tutorial(std::string link, std::string title, std::string presenter, std::string duration, unsigned int likes_number) {

    Tutorial tutorial(link, title, presenter, duration, likes_number);
    this->tutorial_validator.validate_tutorial(link, title, presenter, duration);
    this->tutorial_repo.update(tutorial);
}

std::vector<Tutorial> Tutorial_Service::list_tutorials() {
    return this->tutorial_repo.get_all_tutorials();
}

int Tutorial_Service::get_number_tutorials() {
    return this->tutorial_repo.get_tutorial_number();
}

unsigned int Tutorial_Service::get_number_tutorials_for_presenter(std::string presenter) {

    unsigned int number_of_tutorials = 0;
    std::vector<Tutorial> tutorials = this->list_tutorials();
    for (auto& tutorial: tutorials)
        if (tutorial.get_presenter() ==  presenter)
            number_of_tutorials++;

    return number_of_tutorials;
}

void Tutorial_Service::populate_array() {

    std::string link[12] = { "www.pbinfo.com", "www.untold.com", "www.w3.com", "www.y8.com",
                            "www.schoolit.com","www.itis.com","www.code.com","www.codeacademy.com",
                            "www.duolingo.com","www.udemy.com", "www.youtube.com", "www.sololearn.com" };
    std::string title[12] = { "Basics", "Variables", "Functions","Headers",
                              "Conditions", "Loops", "Pointers","Classes",
                              "Structs","thiss","Dynamic Arrays", "Inheritance"
                                };
    std::string presenter[5] = { "Tom","Grace","Jack","Arthur","David" };
    std::string duration[12] = { "50:50", "23:00", "11:35", "20:45",
                                 "18:15","21:50", "13:13", "34:12",
                                 "34:51","28:59","09:12", "01:01"};
    unsigned int link_index, title_index, presenter_index, duration_index, likes;
    srand(time(nullptr));
    while (this->tutorial_repo.get_tutorial_number() != 10)
    {
        link_index = title_index = duration_index = rand() % 12;
        presenter_index = rand() % 5;
        likes = rand() % 1000;
        try {
            add_tutorial(link[link_index], title[title_index], presenter[presenter_index], duration[duration_index], likes);
        }
        catch (RepoError& repo_error) {}
    }
}
