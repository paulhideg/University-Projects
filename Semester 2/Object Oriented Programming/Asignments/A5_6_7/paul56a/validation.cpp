#include "validation.h"
#include <utility>
#include <ctime>
#include <ctype.h>


void Tutorial_Validation::validate_link(std::string link) {

    if (link.empty())
        throw ValidError("Invalid link");
    if (link.length() < 5)
        throw ValidError("Invalid link");
    if (!(link[0] == link[1] && link[1] == link[2] && link[2] == 'w' && link[3] == '.'))
        throw ValidError("Invalid link");
}

void Tutorial_Validation::validate_title(const std::string& title) {

    if (title.empty())
        throw ValidError("Invalid title");
}

void Tutorial_Validation::validate_presenter(const std::string& presenter) {

    if (presenter.empty())
        throw ValidError("Invalid presenter");
}

void Tutorial_Validation::validate_duration(const std::string& duration) {

    if (duration.empty())
        throw ValidError("Invalid duration");

    if (duration.length() != 5)
        throw ValidError("Invalid duration");

    std::string minutes, seconds;

    if (duration[2] != ':')
        throw ValidError("Invalid duration");

    if (duration[0] == '0' && duration[1] == '0')
    {
        if (duration[3] == '0' && duration[4] == '0')
            throw ValidError("Invalid duration");
    }

    if (duration[3] < '0' || duration[3] > '5')
        throw ValidError("Invalid time");

    if (!(std::isdigit(duration[0])) || !(std::isdigit(duration[1])) || !(std::isdigit(duration[3])) || !(std::isdigit(duration[4])))
        throw ValidError("Invalid duration");
}

void Tutorial_Validation::validate_tutorial(std::string link, const std::string& title, const std::string& presenter, const std::string& duration) {

    std::string err;

    try {
        validate_link(std::move(link));
    }
    catch (ValidError& ve) {
        err += ve.get_message();
        err += "\n";
    }

    try {
        validate_title(title);
    }
    catch (ValidError& ve) {
        err += ve.get_message();
        err += "\n";
    }

    try {
        validate_presenter(presenter);
    }
    catch (ValidError& ve) {
        err += ve.get_message();
        err += "\n";
    }

    try {
        validate_duration(duration);
    }
    catch (ValidError& ve) {
        err += ve.get_message();
    }

    if (!err.empty())
        throw ValidError(err);
}
