#include "domain.h"

Tutorial::Tutorial() = default;

Tutorial::Tutorial(std::string & link, std::string & title, std::string & presenter, std::string & duration, unsigned int likes_number)
{
    this->link = link;
    this->title = title;
    this->presenter = presenter;
    this->duration = duration;
    this->likes_number = likes_number;
}

Tutorial::~Tutorial() = default;

std::string Tutorial::get_title() {
    return title;
}

std::string Tutorial::get_presenter() {
    return presenter;
}

std::string Tutorial::get_duration() {
    return duration;
}

std::string Tutorial::get_link() {
    return link;
}

unsigned int Tutorial::get_likes_number() const {
    return likes_number;
}

void Tutorial::set_title(std::string & new_title) {
    this->title = new_title;
}

void Tutorial::set_presenter(std::string & new_presenter) {
    this->presenter = new_presenter;
}

void Tutorial::set_duration(std::string & new_duration) {
    this->duration = new_duration;
}

void Tutorial::set_likes_number(unsigned int new_likes_number) {
    this->likes_number = new_likes_number;
}

std::ostream& operator<<(std::ostream & output, const Tutorial & tutorial_to_print) {

    output << tutorial_to_print.link << " | " << tutorial_to_print.title << " | " << tutorial_to_print.presenter << " | " << tutorial_to_print.duration << " | " << tutorial_to_print.likes_number << "\n";
    return output;
}
