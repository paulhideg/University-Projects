#include "adminservice.h"
#include "TutorialValidator.h"
#include <assert.h>
#include <sstream>

AdminServices::AdminServices(Repository& repo) :
	repository{ repo }
{
}

void AdminServices::AddTutorial(std::string title, std::string presenter, std::string duration, size_t likes, std::string link)
{
	try {
		Tutorial newTutorial = Tutorial(title, presenter, duration, likes, link);
		TutorialValidator::validate(newTutorial);

		bool found = false;
		for (size_t i = 0; i < this->repository.GetSize() && !found; ++i)
			if (this->repository.GetArray()[i] == newTutorial) found = true;

		if (found) throw std::exception("A tutorial with the given title already exists!");
		this->repository.AddElement(newTutorial);
	}
	catch (ValidationException& e)
	{
		std::cout << e.getMessage() << "\n";
	}
}

void AdminServices::RemoveTutorial(std::string title)
{
	size_t position = this->repository.FindElementByTitle(title);

	if (position >= this->repository.GetSize()) throw std::exception("Tutorial not found!");
	this->repository.RemoveElement(position);
}

void AdminServices::UpdateTutorialTitle(std::string oldTitle, std::string newTitle)
{
	if (!Validator::ValidTutorialTitle(newTitle)) throw std::exception("Invalid tutorial title!");
	size_t position = this->repository.FindElementByTitle(oldTitle);

	if (position >= this->repository.GetSize()) throw std::exception("Tutorial not found!");
	this->repository.UpdateElementTitle(position, newTitle);
}

void AdminServices::UpdateTutorialPresenter(std::string title, std::string newPresenter)
{
	if (!Validator::ValidTutorialPresenter(newPresenter)) throw std::exception("Invalid tutorial presenter!");
	size_t position = this->repository.FindElementByTitle(title);

	if (position >= this->repository.GetSize()) throw std::exception("Tutorial not found!");
	this->repository.UpdateElementPresenter(position, newPresenter);
}

void AdminServices::UpdateTutorialDuration(std::string title, std::string newDuration)
{
	if (!Validator::ValidTutorialDuration(newDuration)) throw std::exception("Invalid tutorial duration!");
	size_t position = this->repository.FindElementByTitle(title);

	if (position >= this->repository.GetSize()) throw std::exception("Tutorial not found!");
	this->repository.UpdateElementDuration(position, newDuration);
}

void AdminServices::UpdateTutorialLikes(std::string title, size_t newLikes)
{
	if (!Validator::ValidTutorialLikes(newLikes)) throw std::exception("Invalid tutorial likes!");
	size_t position = this->repository.FindElementByTitle(title);

	if (position >= this->repository.GetSize()) throw std::exception("Tutorial not found!");
	this->repository.UpdateElementLikes(position, newLikes);
}

void AdminServices::UpdateTutorialLink(std::string title, std::string newLink)
{
	if (!Validator::ValidTutorialLink(newLink)) throw std::exception("Invalid tutorial link!");
	size_t position = this->repository.FindElementByTitle(title);

	if (position >= this->repository.GetSize()) throw std::exception("Tutorial not found!");
	this->repository.UpdateElementLink(position, newLink);
}

Repository AdminServices::GetRepo() const
{
	return this->repository;
}

void AdminServices::InitializeRepo()
{
	//AddMovie("City Lights", "comedy", 1931, 820249, "https://www.youtube.com/watch?v=7vl7F8S4cpQ");
	//AddMovie("Rear Window", "thriller", 1954, 578456, "https://www.youtube.com/watch?v=6kCcZCMYw38");
	//AddMovie("Casablanca", "drama", 1942, 785565, "https://www.youtube.com/watch?v=BkL9l7qovsE");
	//AddMovie("The Godfather", "crime", 1972, 654269, "https://www.youtube.com/watch?v=sY1S34973zA");
	//AddMovie("The Lord of the Rings", "action", 2003, 74685564, "https://www.youtube.com/watch?v=r5X-hFf6Bwo");
	//AddMovie("The Dark Knight", "action", 2008, 98426458, "https://www.youtube.com/watch?v=EXeTwQWrcwY");
	//AddMovie("Inception", "action", 2010, 4567515, "https://www.youtube.com/watch?v=YoHD9XEInc0"); 
	//AddMovie("Venom", "action", 2018, 98551555, "https://www.youtube.com/watch?v=u9Mv98Gr5pY");
	//AddMovie("Rush Hour", "comedy", 1998, 82221525, "https://www.youtube.com/watch?v=JMiFsFQcFLE");
	//AddMovie("It", "thrailler", 2017, 6584455, "https://www.youtube.com/watch?v=7no56Zw1e20");
}
//void AdminServicesTests::TestAll()
//{
//	TestConstructors();
//	TestAdd();
//	TestRemove();
//	TestUpdate();
//}
//
//void AdminServicesTests::TestConstructors()
//{
//	Repository repo(20);
//	AdminServices s2(repo);
//	assert(s2.repository.GetSize() == 0);
//
//	assert(s2.GetRepo() == repo);
//}
//
//void AdminServicesTests::TestAdd()
//{
//	Repository repo(20);
//
//	AdminServices s2(repo);
//	s2.AddMovie("It", "comedy", 2010, 10, "youtube.com");
//
//	assert(s2.repository[0].GetTitle() == "It");
//	assert(s2.repository[0].GetGenre() == "comedy");
//	assert(s2.repository[0].GetYear() == 2010);
//	assert(s2.repository[0].GetLikes() == 10);
//	assert(s2.repository[0].GetTrailer() == "youtube.com");
//
//	s2.AddMovie("Movie", "drama", 2000, 190, "youtube.com");
//
//	assert(s2.repository[1].GetTitle() == "Movie");
//	assert(s2.repository[1].GetGenre() == "drama");
//	assert(s2.repository[1].GetYear() == 2000);
//	assert(s2.repository[1].GetLikes() == 190);
//	assert(s2.repository[1].GetTrailer() == "youtube.com");
//}
//
//void AdminServicesTests::TestRemove()
//{
//	Repository repo(20);
//
//	AdminServices s2(repo);
//	
//
//	s2.AddMovie("It", "comedy", 2010, 10, "youtube.com");
//	s2.AddMovie("Movie", "drama", 2000, 190, "youtube.com");
//
//	s2.RemoveMovie("It");
//
//	assert(s2.repository[0].GetTitle() == "Movie");
//	assert(s2.repository[0].GetGenre() == "drama");
//	assert(s2.repository[0].GetYear() == 2000);
//	assert(s2.repository[0].GetLikes() == 190);
//	assert(s2.repository[0].GetTrailer() == "youtube.com");
//}
//
//void AdminServicesTests::TestUpdate()
//{
//	Repository repo(20);
//
//	AdminServices s2(repo);
//	s2.AddMovie("It", "comedy", 2010, 10, "youtube.com");
//
//	assert(s2.repository[0].GetTitle() == "It");
//	assert(s2.repository[0].GetGenre() == "comedy");
//	assert(s2.repository[0].GetYear() == 2010);
//	assert(s2.repository[0].GetLikes() == 10);
//	assert(s2.repository[0].GetTrailer() == "youtube.com");
//
//	s2.UpdateMovieYear("It", 2000);
//	assert(s2.repository[0].GetYear() == 2000);
//	s2.UpdateMovieLikes("It", 2000);
//	assert(s2.repository[0].GetLikes() == 2000);
//	s2.UpdateMovieTitle("It", "Ted");
//	assert(s2.repository[0].GetTitle() == "Ted");
//	s2.UpdateMovieGenre("Ted", "action");
//	assert(s2.repository[0].GetGenre() == "action");
//	s2.UpdateMovieTrailer("Ted", "Movies.ro");
//	assert(s2.repository[0].GetTrailer() == "Movies.ro");
//}