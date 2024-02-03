#pragma once
#include "domain.h"
#include <vector>
#include <string>
#include <iostream>

class Repository
{
public:
	/// <summary>
	/// Default constructor for the repository class
	/// </summary>
	Repository();

	/// <summary>
	/// Destructor for the repository
	/// </summary>
	~Repository();

	/// <summary>
	/// Adds a new tutorial to the repository
	/// </summary>
	/// <param name="newTutorial">The new tutorial to be added</param>
	virtual void AddElement(const Tutorial& newTutorial);

	/// <summary>
	/// Removes an element from the repo by position
	/// </summary>
	/// <param name="position">The position of the element to be removed</param>
	virtual void RemoveElement(size_t position);

	/// <summary>
	/// Finds a tutorial in the repo by its title
	/// </summary>
	/// <param name="title">The name of the tutorial</param>
	/// <returns>The position of the tutorial</returns>
	virtual size_t FindElementByTitle(std::string title) const;

	/// <summary>
	/// Finds a tutorial in the repo by its presenter
	/// </summary>
	/// <param name="title">The presenter of the tutorial</param>
	/// <returns>The position of the tutorial</returns>
	virtual bool FindElementByPresenter(std::string presenter) const;

	/// <summary>
	/// Updates the title of a tutorial
	/// </summary>
	/// <param name="position">The position of the tutorial</param>
	/// <param name="newTitle">The new title of the tutorial</param>
	virtual void UpdateElementTitle(size_t position, std::string newTitle);

	/// <summary>
	/// Updates the presenter of a tutorial
	/// </summary>
	/// <param name="position">The position of the tutorial</param>
	/// <param name="newPresenter">The new presenter of the tutorial</param>
	virtual void UpdateElementPresenter(size_t position, std::string newPresenter);

	/// <summary>
	/// Updates the duration of a tutorial
	/// </summary>
	/// <param name="position">The position of the tutorial</param>
	/// <param name="newDuration">The new duration of the tutorial</param>
	virtual void UpdateElementDuration(size_t position, std::string newDuration);

	/// <summary>
	/// Updates the number of likes of a tutorial
	/// </summary>
	/// <param name="position">The position of the tutorial</param>
	/// <param name="newLikes">The new likes of the tutorial</param>
	virtual void UpdateElementLikes(size_t position, size_t newLikes);

	/// <summary>
	/// Updates the link of a tutorial
	/// </summary>
	/// <param name="position"></param>
	/// <param name="newLink"></param>
	virtual void UpdateElementLink(size_t position, std::string newLink);

	size_t GetSize() const;
	std::vector<Tutorial> GetArray() const;
	friend std::ostream& operator<<(std::ostream& os, const Repository& repo);
	friend class RepositoryTests;
private:
	std::vector<Tutorial> elementsArray;
};

class RepositoryTests
{
public:
	//static void TestAll();
	//static void TestConstructorsAndAssignment();
	//static void TestAdd();
	//static void TestRemoveSubscript();
	//static void TestUpdate();
	//static void TestFind();
	//static void TestPrint();
};