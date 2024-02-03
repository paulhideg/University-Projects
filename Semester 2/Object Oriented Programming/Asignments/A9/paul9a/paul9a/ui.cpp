#include "ui.h"
#include <iostream>

Console::Console(AdminServices& adminServices, UserServices& userservices) :
	adminServices{ adminServices }, userServices{ userservices }
{
	adminServices.InitializeRepo();
}

void Console::Start()
{
	SelectWriteMode();
	SelectMode();
}

void Console::SelectWriteMode()
{
	std::cout << "Please select how the data will be saved: \n";
	std::cout << "1. CSV\n";
	std::cout << "2. HTML\n";

	std::string mode;
	std::cin >> mode;

	if (mode.size() != 1)
	{
		std::cout << "Invalid mode!\n";
		exit(1);
	}

	switch (mode[0])
	{
	case '1':
	{
		userServices.SetWriteMode("CSV");
		return;
	}
	case '2':
	{
		userServices.SetWriteMode("HTML");
		return;
	}
	default:
	{
		std::cout << "Invalid mode!\n";
		exit(1);
	}
	}
}

void Console::SelectMode()
{
	bool done = false;

	while (!done)
	{
		std::cout << "Open application in:\n";
		std::cout << "1.Administrator mode\n";
		std::cout << "2.User mode\n";
		std::string mode;
		std::cin >> mode;
		if (mode.size() != 1)
		{
			std::cout << "Invalid command!\n";
			return;
		}

		switch (mode[0])
		{
		case '1':
		{
			MainLoopAdministrator();
			break;
		}
		case '2':
		{
			MainLoopUser();
			break;
		}
		default:
		{
			std::cout << "Invalid command!\n";
			done = true;
			break;
		}
		}
	}
}

void Console::MainLoopUser()
{
	std::string command;
	bool done = false;

	while (!done)
	{
		PrintUserMenu();
		std::cout << "Choose an option: ";
		std::cin >> command;
		if (command.size() != 1)
			std::cout << "Invalid command!\n";
		else
		{
			try
			{
				switch (command[0])
				{
				case '1':
				{
					WatchListNoFilter();
					break;
				}
				case '2':
				{
					WatchListFilter();
					break;
				}
				case '3':
				{
					PrintWatchList();
					break;
				}
				case '4':
				{
					UserWatchTutorial();
					break;
				}
				case '5':
				{
					done = true;
					break;
				}
				default:
				{
					std::cout << "Invalid command!\n";
					break;
				}
				}

			}
			catch (std::exception& e)
			{
				std::cout << e.what() << '\n';
			}
		}
	}
}

void Console::MainLoopAdministrator()
{
	std::string command;
	bool done = false;


	while (!done)
	{
		PrintAdminMenu();
		std::cout << "Command:\n";
		std::cin >> command;
		if (command.size() != 1)
			std::cout << "Invalid command!\n";

		else
		{
			try
			{
				switch (command[0])
				{
				case '1':
				{
					AddTutorial();
					break;
				}
				case '2':
				{
					RemoveTutorial();
					break;
				}
				case '3':
				{
					UpdateTutorial();
					break;
				}
				case '4':
				{
					PrintAllTutorials();
					break;
				}
				case '5':
				{
					done = true;
					break;
				}
				default:
				{
					std::cout << "Invalid command!\n";
					break;
				}
				}
			}
			catch (std::exception& e)
			{
				std::cout << e.what() << '\n';
			}

		}
	}
}

void Console::AddTutorial()
{
	std::string title, presenter, duration, link;
	size_t likes;
	std::cout << "Title: ";
	std::cin >> title;
	std::cout << "Presenter: ";
	std::cin >> presenter;
	std::cout << "Duration: ";
	std::cin >> duration;
	std::cout << "Number of likes: ";
	std::cin >> likes;
	std::cout << "Link: ";
	std::cin >> link;

	this->adminServices.AddTutorial(title, presenter, duration, likes, link);
}

void Console::RemoveTutorial()
{
	std::string title;
	std::cout << "Title of the tutorial you wish to remove: ";
	std::cin >> title;

	this->adminServices.RemoveTutorial(title);
}

void Console::UpdateTutorial()
{
	std::string title;
	std::cout << "Title of the tutorial you wish to update\n";
	std::cin >> title;
	std::cout << "What would you like to modify?\n"
		<< "1. title | 2. presenter | 3. duration | 4. likes | 5. link\n";

	std::string updateAttribute;
	std::cin >> updateAttribute;

	if (updateAttribute.size() != 1)
	{
		std::cout << "Invalid command!\n";
		return;
	}

	switch (updateAttribute[0])
	{
	case '1':
	{
		std::string newTitle;
		std::cout << "Please input the new title\n";
		std::cin >> newTitle;
		UpdateTutorialTitle(title, newTitle);
		break;
	}
	case '2':
	{
		std::string newPresenter;
		std::cout << "Please input the new presenter\n";
		std::cin >> newPresenter;
		UpdateTutorialPresenter(title, newPresenter);
		break;
	}
	case '3':
	{
		std::string newDuration;
		std::cout << "Please input the new duration\n";
		std::cin >> newDuration;
		UpdateTutorialDuration(title, newDuration);
		break;
	}
	case '4':
	{
		size_t newLikes;
		std::cout << "Please input the new number of likes\n";
		std::cin >> newLikes;
		UpdateTutorialLikes(title, newLikes);
		break;
	}
	case '5':
	{
		std::string newLink;
		std::cout << "Please input the new link\n";
		std::cin >> newLink;
		UpdateTutorialLink(title, newLink);
		break;
	}
	default:
	{
		std::cout << "Invalid attribute!\n";
		break;
	}
	}
}

void Console::UpdateTutorialTitle(std::string oldTitle, std::string newTitle)
{
	this->adminServices.UpdateTutorialTitle(oldTitle, newTitle);
}

void Console::UpdateTutorialPresenter(std::string title, std::string newPresenter)
{
	this->adminServices.UpdateTutorialPresenter(title, newPresenter);
}

void Console::UpdateTutorialDuration(std::string title, std::string newDuration)
{
	this->adminServices.UpdateTutorialDuration(title, newDuration);
}

void Console::UpdateTutorialLikes(std::string title, size_t newLikes)
{
	this->adminServices.UpdateTutorialLikes(title, newLikes);
}

void Console::UpdateTutorialLink(std::string title, std::string newLink)
{
	this->adminServices.UpdateTutorialLink(title, newLink);
}

void Console::PrintAllTutorials()
{
	std::cout << adminServices.GetRepo();
}

void Console::WatchListNoFilter()
{
	std::cout << "\t1. Add to watch list\n";
	std::cout << "\t2. Next tutorial\n";
	std::cout << "\t3. Exit\n";

	bool exit = false;
	UserInitializeTutorialList();

	while (!exit)
	{
		std::cout << userServices.GetCurrentTutorial();
		std::cout << "\n\tCommand: ";
		int command = 0;
		while (command >= 4 || 0 >= command)
		{
			std::cin >> command;
			if (command >= 4 || 0 >= command)
				std::cout << "Invalid command\n";
		}
		if (command == 1)
			AddTutorialToWatchList();
		if (command == 2)
			DoNotAddTutorialToWatchList();
		if (command == 3)
			exit = true;
	}
}

void Console::WatchListFilter()
{
	std::cout << "\t1. Add to watch list\n";
	std::cout << "\t2. Next tutorial\n";
	std::cout << "\t3. Exit\n";


	bool exit = false;
	UserInitializeTutorialList();
	FilterByPresenter();

	while (!exit)
	{
		std::cout << userServices.GetCurrentTutorial();
		std::cout << "\n\tCommand: ";
		int command = 0;
		while (command >= 4 || 0 >= command)
		{
			std::cin >> command;
			if (command >= 4 || 0 >= command)
				std::cout << "Invalid command\n";
		}
		if (command == 1)
			AddTutorialToWatchList();
		if (command == 2)
			DoNotAddTutorialToWatchList();
		if (command == 3)
			exit = true;
	}
}

void Console::PrintWatchList()
{
	if (userServices.GetWriteMode() == "CSV")
	{
		userServices.WriteData();

		std::string command = "notepad " + userServices.GetFileName();

		system("D:");
		system("cd 1.School\\OOP\\a9hp\\paul9a\\tutorialdatabase");
		system(command.c_str());
	}
	else
	{
		userServices.WriteData();

		system("D:");
		system("cd 1.School\\OOP\\a9hp\\paul9a\\tutorialdatabase");
		system(userServices.GetFileName().c_str());
	}
}

void Console::AddTutorialToWatchList()
{
	userServices.AddToWatchList(userServices.GetCurrentTutorial());
}

void Console::DoNotAddTutorialToWatchList()
{
	userServices.NextTutorial();
}

void Console::FilterByPresenter()
{
	bool found = false;

	while (!found)
	{
		std::string presenter;
		std::cout << "Choose presenter: ";
		std::cin >> presenter;
		found = userServices.IsPresenter(presenter);
		if (!found)
			std::cout << "No tutorial with this presenter!\n";
		else
			userServices.FilterByPresenter(presenter);
	}
}

void Console::UserInitializeTutorialList()
{
	userServices.InitializeTutorialList();
}

void Console::UserWatchTutorial()
{
	std::cout << "Title of the tutorial you watched: ";
	std::string title;
	std::cin.ignore(1000, '\n');
	std::getline(std::cin, title);

	std::cout << "Do you want to like this tutorial? (yes/no)";
	std::string rate;
	std::cin >> rate;

	bool yes = false;
	if (rate == "yes" || rate == "y")
		yes = true;


	userServices.WatchTutorial(title, yes);
}

void Console::PrintAdminMenu()
{
	std::cout << "\n1.Add a new tutorial\n";
	std::cout << "2.Remove a tutorial by title\n";
	std::cout << "3.Update an existing tutorial\n";
	std::cout << "4.Print all available tutorials\n";
	std::cout << "5.Exit\n\n";
}

void Console::PrintUserMenu()
{
	std::cout << "\n1. See all tutorials\n";
	std::cout << "2. Filter by presenter\n";
	std::cout << "3. See watch list\n";
	std::cout << "4. Mark tutorial as watched and rate it\n";
	std::cout << "5. Exit\n\n";
}
