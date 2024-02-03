#include "domain.h"
#include <iostream>
#include <assert.h>
#include <sstream>

using namespace std;

Tutorial::Tutorial(std::string title, std::string presenter, std::string duration, size_t likes, std::string link) :
	title{ title }, presenter{ presenter }, duration{ duration }, likes{ likes }, link{ link }
{
}

Tutorial::Tutorial() : title{ "" }, presenter{ "" }, duration{ ""}, likes{0}, link{""}
{
}

Tutorial::~Tutorial()
{
}

std::string Tutorial::GetTitle() const
{
	return this->title;
}

std::string Tutorial::GetPresenter() const
{
	return this->presenter;
}

std::string Tutorial::GetDuration() const
{
	return this->duration;
}

size_t Tutorial::GetLikes() const
{
	return this->likes;
}

std::string Tutorial::GetLink() const
{
	return this->link;
}

void Tutorial::SetTitle(std::string title)
{
	this->title = title;
}

void Tutorial::SetPresenter(std::string presenter)
{
	this->presenter = presenter;
}

void Tutorial::SetDuration(std::string durationoftutorial)
{
	this->duration = durationoftutorial;
}

void Tutorial::SetLikes(size_t likes)
{
	this->likes = likes;
}

void Tutorial::SetLink(std::string link)
{
	this->link = link;
}

bool Tutorial::operator==(const Tutorial& other) const
{
	return this->title == other.title;
}

//std::ostream& operator<<(std::ostream& os, const Movie& movie)
//{
//	return os << "Title: " << movie.title << " | Genre: " << movie.genre << " | Year: " << movie.year << " | Likes: " << movie.likes << "\n\tTrailer: " << movie.trailer << "\n";
//}

std::ostream& operator<<(std::ostream& os, const Tutorial& tutorial)
{
	return os << tutorial.title << " " << tutorial.presenter << " " << tutorial.duration << " " << tutorial.likes << " " << tutorial.link<< '\n';
}

std::istream& operator>>(std::istream& is, Tutorial& tutorial)
{
	return is >> tutorial.title >> tutorial.presenter>> tutorial.duration>> tutorial.likes >> tutorial.link;
}

void TutorialTests::TestAllTutorial()
{
	TestConstructorsAndGettersTutorial();
	TestSettersTutorial();
	TestEqualityTutorial();
	TestExtractionOperator();
}

void TutorialTests::TestConstructorsAndGettersTutorial()
{
	/*Movie m1;
	assert(m1.GetTitle() == "");
	assert(m1.GetGenre() == "");
	assert(m1.GetTrailer() == "");
	assert(m1.GetYear() == 0);
	assert(m1.GetLikes() == 0);

	Movie m2("It", "comedy", 2010, 10, "youtube.com");
	assert(m2.GetTitle() == "It");
	assert(m2.GetGenre() == "comedy");
	assert(m2.GetTrailer() == "youtube.com");
	assert(m2.GetYear() == 2010);
	assert(m2.GetLikes() == 10);*/
}

void TutorialTests::TestSettersTutorial()
{
	/*Movie m;
	m.SetTitle("It");
	m.SetGenre("comedy");
	m.SetTrailer("youtube.com");
	m.SetYear(2010);
	m.SetLikes(10);

	assert(m.GetTitle() == "It");
	assert(m.GetGenre() == "comedy");
	assert(m.GetTrailer() == "youtube.com");
	assert(m.GetYear() == 2010);
	assert(m.GetLikes() == 10);*/
}

void TutorialTests::TestEqualityTutorial()
{
	/*Movie m;
	m.SetTitle("It");
	m.SetGenre("comedy");
	m.SetTrailer("youtube.com");
	m.SetYear(2010);
	m.SetLikes(10);

	Movie n("It", "comedy", 2010, 10, "youtube.com");

	assert(m == n);*/
}

void TutorialTests::TestExtractionOperator()
{
	/*Movie m;
	m.SetTitle("It");
	m.SetGenre("comedy");
	m.SetTrailer("youtube.com");
	m.SetYear(2010);
	m.SetLikes(10);
	std::stringbuf buffer;
	std::ostream os(&buffer);
	os << m;
	assert(buffer.str() == "Title: It | Genre: comedy | Year: 2010 | Likes: 10\n\tTrailer: youtube.com\n");*/
}
