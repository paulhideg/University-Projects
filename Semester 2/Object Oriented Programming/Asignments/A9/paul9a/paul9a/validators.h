#pragma once
#include "domain.h"

class Validator
{
public:
	static bool ValidTutorialAttributes(std::string title, std::string presenter, std::string duration, size_t likes, std::string link);
	static bool ValidTutorialTitle(std::string title);
	static bool ValidTutorialPresenter(std::string presenter);
	static bool ValidTutorialDuration(std::string duration);
	static bool ValidTutorialLikes(size_t likes);
	static bool ValidTutorialLink(std::string link);
};