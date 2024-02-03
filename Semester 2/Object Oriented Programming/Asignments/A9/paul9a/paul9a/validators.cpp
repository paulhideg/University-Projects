#include "validators.h"
#include <regex>

bool Validator::ValidTutorialAttributes(std::string title, std::string presenter, std::string duration, size_t likes, std::string link)
{
	return ValidTutorialTitle(title) && ValidTutorialPresenter(presenter) && ValidTutorialDuration(duration) && ValidTutorialLikes(likes) && ValidTutorialLink(link);
}

bool Validator::ValidTutorialTitle(std::string title)
{
	return !title.empty();
}

bool Validator::ValidTutorialPresenter(std::string presenter)
{
	return !presenter.empty();
}

bool Validator::ValidTutorialDuration(std::string duration)
{
    if (duration.empty())
        return 0;

    if (duration.length() != 5)
        return 0;

    std::string minutes, seconds;

    if (duration[2] != ':')
        return 0;

    if (duration[0] == '0' && duration[1] == '0')
    {
        if (duration[3] == '0' && duration[4] == '0')
            return 0;
    }

    if (duration[3] < '0' || duration[3] > '5')
        return 0;

    if (!(std::isdigit(duration[0])) || !(std::isdigit(duration[1])) || !(std::isdigit(duration[3])) || !(std::isdigit(duration[4])))
        return 0;

    return 1;
}

bool Validator::ValidTutorialLikes(size_t likes)
{
	return likes >= 0;
}

bool Validator::ValidTutorialLink(std::string link)
{
	return !link.empty();
}
