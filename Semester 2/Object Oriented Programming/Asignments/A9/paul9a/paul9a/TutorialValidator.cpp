#include "TutorialValidator.h"

using namespace std;

ValidationException::ValidationException(std::string _message) : message{ _message }
{
}

std::string ValidationException::getMessage() const
{
	return this->message;
}


ValidationExceptionInherited::ValidationExceptionInherited(std::string _message) : message{ _message }
{
}

const char* ValidationExceptionInherited::what() const noexcept
{
	return message.c_str();
}


void TutorialValidator::validate(const Tutorial& s)
{
	string errors;
	if (s.GetTitle().size() < 2)
		errors += string("The tutorial title cannot be less than 2 characters!\n");
	if (s.GetPresenter().size() < 2)
		errors += string("The tutorial presenter cannot be less than 2 characters!\n");
	if (s.GetLikes() < 0)
		errors += string("The tutorial can not have a negative number of likes");
	if (errors.size() > 0)
		throw ValidationException(errors);
}
