#pragma once
#include "adminservice.h"
#include "userservice.h"

class Console
{
public:
	Console(AdminServices& adminServices, UserServices& userservices);

	void Start();
	void SelectMode();
	void SelectWriteMode();
	void MainLoopUser();
	void MainLoopAdministrator();

	void AddTutorial();
	void RemoveTutorial();
	void UpdateTutorial();
	void UpdateTutorialTitle(std::string oldTitle, std::string newTitle);
	void UpdateTutorialPresenter(std::string title, std::string newPresenter);
	void UpdateTutorialDuration(std::string title, std::string newDuration);
	void UpdateTutorialLikes(std::string title, size_t newLikes);
	void UpdateTutorialLink(std::string title, std::string newLink);
	void PrintAllTutorials();

	void WatchListNoFilter();
	void WatchListFilter();
	void PrintWatchList();
	void AddTutorialToWatchList();
	void DoNotAddTutorialToWatchList();
	void FilterByPresenter();
	void UserInitializeTutorialList();
	void UserWatchTutorial();

	void PrintAdminMenu();
	void PrintUserMenu();
private:
	AdminServices adminServices;
	UserServices userServices;
};
