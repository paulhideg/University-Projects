#pragma once
//#include "repository.h"
#include "FileRepository.h"
#include "validators.h"

class AdminServices
{
public:
	/// <summary>
	/// Constructor for the Services class
	/// </summary>
	/// <param name="repo">The repository on which the services class operates</param>
	AdminServices(Repository& repo);

	/// <summary>
	/// Adds a new tutorial to the repository
	/// Also performs data validation
	/// </summary>
	/// <param name="title">The title of tutorial</param>
	/// <param name="presenter">The presenter of the tutorial</param>
	/// <param name="duration">The duration of the tutorial</param>
	/// <param name="likes">The number of likes of the tutorial</param>
	/// <param name="link">The link of the tutorial</param>
	void AddTutorial(std::string title, std::string presenter, std::string duration, size_t likes, std::string link);

	/// <summary>
	/// Removes a tutorial from the repository
	/// </summary>
	/// <param name="title">The title of the tutorial which will be removed</param>
	void RemoveTutorial(std::string title);

	/// <summary>
	/// Updates the title of a tutorial from the repository
	/// Performs data validation for the new title
	/// </summary>
	/// <param name="oldTitle">The old title of the tutorial</param>
	/// <param name="newTitle">The new title of the tutorial</param>
	void UpdateTutorialTitle(std::string oldTitle, std::string newTitle);

	/// <summary>
	/// Updates the presenter of a tutorial from the repository
	/// Performs data validation for the new presenter
	/// </summary>
	/// <param name="title">The title of the tutorial</param>
	/// <param name="newPresenter">The new presenter of the tutorial</param>
	void UpdateTutorialPresenter(std::string title, std::string newPresenter);

	/// <summary>
	/// Updates the duration of a tutorial from the repository
	/// Performs data validation for the new duration
	/// </summary>
	/// <param name="title">The title of the tutorial</param>
	/// <param name="newDuration">The new duration of the tutorial</param>
	void UpdateTutorialDuration(std::string title, std::string newDuration);

	/// <summary>
	/// Updates the likes of a tutorial from the repository
	/// Performs data validation for the new likes
	/// </summary>
	/// <param name="title">The title of the tutorial</param>
	/// <param name="newLikes">The new likes of the tutorial</param>
	void UpdateTutorialLikes(std::string title, size_t newLikes);

	/// <summary>
	/// Updates the link of a tutorial from the repository
	/// Performs data validation for the new link
	/// </summary>
	/// <param name="title">The title of the tutorial</param>
	/// <param name="newLink">The new link of the tutorial</param>
	void UpdateTutorialLink(std::string title, std::string newLink);

	/// <summary>
	/// Prints the contents of the repository
	/// </summary>
	Repository GetRepo() const;

	/// <summary>
	/// Adds 10 entries to the repository
	/// </summary>
	void InitializeRepo();

	friend class AdminServicesTests;
private:
	Repository& repository;
};


class AdminServicesTests
{
public:
	static void TestAll();
	static void TestConstructors();
	static void TestAdd();
	static void TestRemove();
	static void TestUpdate();
};