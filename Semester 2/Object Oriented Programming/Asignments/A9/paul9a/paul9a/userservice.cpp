#include "userservice.h"
#include <assert.h>
#include <sstream>

UserServices::UserServices(Repository& repo) :
	repo{ repo },
	tutoriallist{ repo.GetArray() },
	watchlist{ std::vector<Tutorial>(1) }, index{ 0 },
	writer{ nullptr },
	writeMode{ "" },
	tutorials{ TutorialList() }
{
}

UserServices::~UserServices()
{
	delete writer;
}

void UserServices::WriteData()
{
	writer->WriteToFile(tutorials);
}

void UserServices::InitializeTutorialList()
{
	if (tutoriallist == repo.GetArray())
		return;

	tutoriallist = repo.GetArray();
	index = 0;
}

void UserServices::AddToWatchList(const Tutorial& tutorial)
{
	//bool found = false;
	//for (int i = 0; i < watchlist.size(); i++)
	//	if (watchlist[i] == movie)
	//		found = true;
	//if (found == true)
	//	throw std::exception("Movie alreday in watch list");
	//else
	//	watchlist.push_back(movie);
	//NextMovie();

	tutorials.AddTutorial(tutorial);
	NextTutorial();
}

std::vector<Tutorial> UserServices::SeeWatchList() const
{
	return watchlist;
}

void UserServices::FilterByPresenter(std::string presenter)
{
	for (int i = 0; i < tutoriallist.size(); i++)
		if (tutoriallist[i].GetPresenter() != presenter)
		{
			tutoriallist.erase(tutoriallist.begin() + i);
			i--;
		}
	index = 0;
}

bool UserServices::IsPresenter(std::string presenter)
{
	return repo.FindElementByPresenter(presenter);
}

void UserServices::NextTutorial()
{
	if (index == tutoriallist.size() - 1)
	{
		index = 0;
		return;
	}
	index++;
}

void UserServices::RateWatchedTutorial(std::string title)
{
	size_t i = repo.FindElementByTitle(title);
	size_t currentLikes = repo.GetArray()[i].GetLikes() + 1;
	if (i >= 0)
	{
		bool found1 = false;
		for (size_t j = 0; j < tutoriallist.size() && !found1; j++)
			if (tutoriallist[j].GetTitle() == title)
			{
				found1 = true;
				repo.UpdateElementLikes(j, currentLikes);
				tutoriallist[j].SetLikes(currentLikes);
			}
	}
	else
		throw std::exception("No tutorial with such title");

}

void UserServices::WatchTutorial(std::string title, bool rate)
{
	//bool found = false;
	//for (int i = 0; i < watchlist.size(); i++)
	//	if (watchlist[i].GetTitle() == title)
	//	{
	//		watchlist.erase(watchlist.begin()+i);
	//		found = true;
	//		break;
	//	}
	//if (!found)
	//	throw std::exception("No such movie in your watch list");
	//if (rate)
	//		RateWatchedMovie(title);
	bool found = false;
	Tutorial m;
	for (int i = 0; i < tutoriallist.size(); i++)
		if (tutoriallist[i].GetTitle() == title)
		{
			m = tutoriallist[i];
			found = true;
			break;
		}
	found = false;
	found = tutorials.DeleteTutorial(m);
	if (!found)
		throw std::exception("No such tutorial in your watch list");
	if (rate)
		RateWatchedTutorial(title);
}

Tutorial UserServices::GetCurrentTutorial() const
{
	return tutoriallist[index];
}

const std::string& UserServices::GetFileName() const
{
	return writer->GetFileName();
}

const std::string& UserServices::GetWriteMode() const
{
	return writeMode;
}

void UserServices::SetWriteMode(const std::string& newMode)
{
	if (newMode == "CSV")
	{
		writeMode = newMode;
		writer = new CSVTutorialListWriter("watch_list.csv");
	}
	else if (newMode == "HTML")
	{
		writeMode = newMode;
		writer = new HTMLTutorialListWriter("watch_list.html");
	}
	else
	{
		throw std::exception("Unhandled mode!");
	}
}

void UserServicesTests::TestAll()
{
	//TestConstructor();
	//TestSkippingAndAddingToWatchList();
	//TestFilteringAndReinitialization();
	//TestRateMovieandDeteleFromWatchList(); 
	//TestGetters();
}

//void UserServicesTests::TestConstructor()
//{
//	Repository repo(20);
//	repo.AddElement(Movie("City Lights", "comedy", 1931, 820249, "https://www.youtube.com/watch?v=7vl7F8S4cpQ"));
//	repo.AddElement(Movie("Rear Window", "thriller", 1954, 578456, "https://www.youtube.com/watch?v=6kCcZCMYw38"));
//	repo.AddElement(Movie("Casablanca", "drama", 1942, 785565, "https://google.com"));
//	repo.AddElement(Movie("The Godfather", "crime", 1972, 654269, "https://google.com"));
//	repo.AddElement(Movie("The Lord of the Rings", "action", 2003, 74685564, "https://google.com"));
//	repo.AddElement(Movie("The Dark Knight", "action", 2008, 98426458, "photo.ro"));
//	repo.AddElement(Movie("Inception", "action", 2010, 4567515, "https://Movies.com/photos/1"));
//	repo.AddElement(Movie("Venom", "action", 2018, 98551555, "https://Movies.com/photos/2"));
//	repo.AddElement(Movie("Rush Hour", "comedy", 1998, 82221525, "https://Movies.com/photos/3"));
//	repo.AddElement(Movie("It", "thrailler", 2017, 6584455, "https://Movies.com/photos/4"));
//	UserServices s1(repo);
//	assert(s1.movielist == repo.GetArray());
//	assert(s1.index == 0);
//	assert(s1.watchlist.GetSize() == 0);
//}
//
//void UserServicesTests::TestSkippingAndAddingToWatchList()
//{
//	Repository repo(20);
//	repo.AddElement(Movie("Rush Hour", "comdey", 1998, 82221525, "https://Movies.com/photos/3"));
//	repo.AddElement(Movie("It", "thrailler", 2017, 6584455, "https://Movies.com/photos/4"));
//	UserServices s1(repo);
//
//	s1.AddToWatchList(s1.repo[s1.index]);
//	assert(s1.watchlist.GetSize() == 1);
//	assert(s1.watchlist[0] == s1.repo[0]);
//	assert(s1.index == 1);
//
//	s1.NextMovie();
//	assert(s1.index == 0);
//}
//
//void UserServicesTests::TestFilteringAndReinitialization()
//{
//	Repository repo(20);
//	repo.AddElement(Movie("City Lights", "comedy", 1931, 820249, "https://www.youtube.com/watch?v=7vl7F8S4cpQ"));
//	repo.AddElement(Movie("Rear Window", "thriller", 1954, 578456, "https://www.youtube.com/watch?v=6kCcZCMYw38"));
//	repo.AddElement(Movie("Casablanca", "drama", 1942, 785565, "https://google.com"));
//	repo.AddElement(Movie("The Godfather", "crime", 1972, 654269, "https://google.com"));
//	repo.AddElement(Movie("The Lord of the Rings", "action", 2003, 74685564, "https://google.com"));
//	repo.AddElement(Movie("The Dark Knight", "action", 2008, 98426458, "photo.ro"));
//	repo.AddElement(Movie("Inception", "action", 2010, 4567515, "https://Movies.com/photos/1"));
//	repo.AddElement(Movie("Venom", "action", 2018, 98551555, "https://Movies.com/photos/2"));
//	repo.AddElement(Movie("Rush Hour", "comedy", 1998, 82221525, "https://Movies.com/photos/3"));
//	repo.AddElement(Movie("It", "thrailler", 2017, 6584455, "https://Movies.com/photos/4"));
//	UserServices s1(repo);
//
//	s1.FilterByGenre("comedy");
//	assert(s1.movielist.GetSize() == 2);
//	assert(s1.movielist[0] == Movie("City Lights", "comedy", 1931, 820249, "https://www.youtube.com/watch?v=7vl7F8S4cpQ"));
//	assert(s1.movielist[1] == Movie("Rush Hour", "comedy", 1998, 82221525, "https://Movies.com/photos/3"));
//	bool found = s1.IsGenre("comedy");
//	assert(found == true);
//
//	s1.InitializeMovieList();
//	assert(s1.movielist.GetSize() == 10);
//	assert(s1.index == 0);
//
//	s1.FilterByGenre("action");
//	assert(s1.movielist.GetSize() == 4);
//
//	s1.InitializeMovieList();
//	assert(s1.movielist.GetSize() == 10);
//	assert(s1.index == 0);
//
//	s1.InitializeMovieList();
//	assert(s1.movielist.GetSize() == 10);
//	assert(s1.index == 0);
//}
//
//void UserServicesTests::TestRateMovieandDeteleFromWatchList()
//{
//	Repository repo(20);
//	repo.AddElement(Movie("Rush Hour", "comdey", 1998, 82221525, "https://Movies.com/photos/3"));
//	repo.AddElement(Movie("It", "thrailler", 2017, 6584455, "https://Movies.com/photos/4"));
//	UserServices s1(repo);
//
//	s1.AddToWatchList(s1.repo[1]);
//	s1.AddToWatchList(s1.repo[0]);
//	assert(s1.watchlist.GetSize()==2);
//
//	s1.WatchMovie("It", true);
//	assert(s1.watchlist.GetSize() == 1);
//	
//	assert(s1.repo[1].GetLikes() == 6584456);
//	try
//	{
//		s1.AddToWatchList(s1.repo[0]);
//		s1.WatchMovie("It", true);
//	}
//	catch (std::exception& ex)
//	{
//		//assert(true);
//	}
//
//}
//
//void UserServicesTests::TestGetters()
//{
//	Repository repo(20);
//	repo.AddElement(Movie("Rush Hour", "comdey", 1998, 82221525, "https://Movies.com/photos/3"));
//	repo.AddElement(Movie("It", "thrailler", 2017, 6584455, "https://Movies.com/photos/4"));
//	UserServices s1(repo);
//
//	s1.AddToWatchList(s1.repo[s1.index]);
//
//	s1.NextMovie();
//
//	assert(s1.SeeWatchList() == s1.watchlist);
//	assert(s1.GetCurrentMovie() == Movie("Rush Hour", "comdey", 1998, 82221525, "https://Movies.com/photos/3"));
//	try
//	{
//		s1.AddToWatchList(s1.repo[s1.index]);
//		//assert(false);
//	}
//	catch (std::exception& ex)
//	{
//		assert(true);
//	}
//}
