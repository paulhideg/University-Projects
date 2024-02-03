#pragma once
#include "repository.h"
#include "TutorialList.h"
#include <vector>

class UserServices
{
private:
	Repository& repo;
	std::vector<Tutorial> tutoriallist;
	TutorialList tutorials;
	TutorialListWriter* writer;
	std::vector<Tutorial> watchlist;
	size_t index;
	std::string writeMode;
public:
	/// <summary>
	/// The constrcutor for the user service class
	/// </summary>
	/// <param name="repo"></param>
	UserServices(Repository& repo);

	/// <summary>
	/// Initializez the current tutorial list to the list in repo and sets the index to 0
	/// </summary>
	void InitializeTutorialList();

	/// <summary>
	/// adds a tutorial to watch list
	/// </summary>
	/// <param name="movie">the tutorial to be added</param>
	void AddToWatchList(const Tutorial& tutorial);

	/// <summary>
	/// filters the tutorials in repo by presenter
	/// </summary>
	/// <param name="presenter">the presenter of the tutorial</param>
	void FilterByPresenter(std::string presenter);

	/// <summary>
	/// verifies if the presenter introduced by the user is valid
	/// </summary>
	/// <param name="presenter">the presenter introduced by the user</param>
	/// <returns>True if it exists in repo, false otherwise</returns>
	bool IsPresenter(std::string presenter);

	/// <summary>
	/// moves the index to the next tutorial in the list
	/// </summary>
	void NextTutorial();

	/// <summary>
	/// likes a tutorial watched by the user
	/// </summary>
	/// <param name="title">the title of the tutorial to be liked</param>
	void RateWatchedTutorial(std::string title);

	/// <summary>
	/// it deletes the tutorial from watch list and gives the user the posibility to like that tutorial
	/// </summary>
	/// <param name="title">the title of the tutorial</param>
	/// <param name="rate">yes/no like</param>
	void WatchTutorial(std::string title, bool rate);

	~UserServices();
	void WriteData();

	/// Getters
	Tutorial GetCurrentTutorial() const;
	std::vector<Tutorial> SeeWatchList() const;
	const std::string& GetFileName() const;
	const std::string& GetWriteMode() const;

	void SetWriteMode(const std::string& newMode);

	friend class UserServicesTests;
};

class UserServicesTests
{
public:
	static void TestAll();
	static void TestConstructor();
	static void TestSkippingAndAddingToWatchList();
	static void TestFilteringAndReinitialization();
	static void TestRateMovieandDeteleFromWatchList();
	static void TestGetters();
};