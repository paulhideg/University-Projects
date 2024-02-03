#include "repository.h"
#include <iostream>
#include <assert.h>
#include <sstream>
#include <vector>

Repository::Repository()
{
}

Repository::~Repository()
{
}

void Repository::AddElement(const Tutorial& newTutorial)
{
	this->elementsArray.push_back(newTutorial);
}

void Repository::RemoveElement(size_t position)
{
	this->elementsArray.erase(this->elementsArray.begin() + position);
}

size_t Repository::FindElementByTitle(std::string title) const
{
	auto it = std::find_if(this->elementsArray.begin(), this->elementsArray.end(),
		[title](Tutorial m) { return m.GetTitle() == title; });
	if (it != this->elementsArray.end())
	{
		//std::cout << "Element " << name << " found at position : ";
		//std::cout << it - this->elementsArray.begin() << " (counting from zero) \n";
		return it - this->elementsArray.begin();
	}
	else
		//std::cout << "Element not found.\n\n";
		return -1;

}

bool Repository::FindElementByPresenter(std::string presenter) const
{
	auto it = std::find_if(this->elementsArray.begin(), this->elementsArray.end(),
		[presenter](Tutorial m) { return m.GetPresenter() == presenter; });
	if (it != this->elementsArray.end())
		return true;
	else
		return false;
}

void Repository::UpdateElementTitle(size_t position, std::string newTitle)
{
	(this->elementsArray)[position].SetTitle(newTitle);
}

void Repository::UpdateElementPresenter(size_t position, std::string newPresenter)
{
	(this->elementsArray)[position].SetPresenter(newPresenter);
}

void Repository::UpdateElementDuration(size_t position, std::string newDuration)
{
	(this->elementsArray)[position].SetDuration(newDuration);
}

void Repository::UpdateElementLikes(size_t position, size_t newLikes)
{
	(this->elementsArray)[position].SetLikes(newLikes);
}

void Repository::UpdateElementLink(size_t position, std::string newLink)
{
	(this->elementsArray)[position].SetLink(newLink);
}

size_t Repository::GetSize() const
{
	return this->elementsArray.size();
}

std::vector<Tutorial> Repository::GetArray() const
{
	return this->elementsArray;
}

std::ostream& operator<<(std::ostream& os, const Repository& repo)
{
	for (auto it : repo.GetArray())
		os << it;
	return os;
}

//void RepositoryTests::TestAll()
//{
//	TestConstructorsAndAssignment();
//	TestAdd();
//	TestRemoveSubscript();
//	TestUpdate();
//	TestFind();
//	TestPrint();
//}
//
//void RepositoryTests::TestConstructorsAndAssignment()
//{
//	Repository repo1{};
//	assert(repo1.elementsArray.size() == 0);
//
//	Repository repo2{};
//	assert(repo2.elementsArray.size() == 0);
//	assert(repo2.GetSize() == 0);
//
//	repo2.AddElement(Movie("It", "comedy", 2010, 10, "youtube.com"));
//	repo1 = repo2;
//
//	assert(repo1.elementsArray == repo2.elementsArray);
//}
//
//void RepositoryTests::TestAdd()
//{
//	Repository repo2{};
//	Movie d1("It", "comedy", 2010, 10, "youtube.com");
//	Movie d2("It", "comedy", 2010, 10, "youtube.com");
//	Movie d3("It", "comedy", 2010, 10, "youtube.com");
//	Movie d4("It", "comedy", 2010, 10, "youtube.com");
//	repo2.AddElement(d1);
//	repo2.AddElement(d2);
//	repo2.AddElement(d3);
//	repo2.AddElement(d4);
//
//	assert(repo2[0] == d1);
//	assert(repo2[1] == d2);
//	assert(repo2[2] == d3);
//	assert(repo2[3] == d4);
//}
//
//void RepositoryTests::TestRemoveSubscript()
//{
//	Repository repo2(10);
//	Movie d1("It", "comedy", 2010, 10, "youtube.com");
//	Movie d2("It", "comedy", 2010, 10, "youtube.com");
//	Movie d3("It", "comedy", 2010, 10, "youtube.com");
//	Movie d4("It", "comedy", 2010, 10, "youtube.com");
//	repo2.AddElement(d1);
//	repo2.AddElement(d2);
//	repo2.AddElement(d3);
//	repo2.AddElement(d4);
//
//	repo2.RemoveElement(1);
//
//	assert(repo2[0] == d1);
//	assert(repo2[1] == d3);
//	assert(repo2[2] == d4);
//}
//
//void RepositoryTests::TestUpdate()
//{
//	Repository repo2(10);
//	Movie d1("It", "comedy", 2010, 10, "youtube.com");
//	repo2.AddElement(d1);
//
//	repo2.UpdateElementTitle(0, "oo");
//	assert(repo2[0].GetTitle() == "oo");
//
//	repo2.UpdateElementGenre(0, "drama");
//	assert(repo2[0].GetGenre() == "drama");
//
//	repo2.UpdateElementYear(0, 1500);
//	assert(repo2[0].GetYear() == 1500);
//
//	repo2.UpdateElementTrailer(0, "Movies.com");
//	assert(repo2[0].GetTrailer() == "Movies.com");
//}
//
//void RepositoryTests::TestFind()
//{
//	Repository repo2(10);
//	Movie d1("It", "comedy", 2010, 10, "youtube.com");
//	Movie d2("It", "comedy", 2010, 10, "youtube.com");
//	Movie d3("It2", "comedy", 2010, 10, "youtube.com");
//	Movie d4("It", "comedy", 2010, 10, "youtube.com");
//	repo2.AddElement(d1);
//	repo2.AddElement(d2);
//	repo2.AddElement(d3);
//	repo2.AddElement(d4);
//
//	size_t position = repo2.FindElementByTitle("It2");
//	bool found = repo2.FindElementByGenre("comedy");
//	assert(position == 2);
//	assert(found == true);
//}
//
//void RepositoryTests::TestPrint()
//{
//	Repository repo2(10);
//	Movie d1("It", "comedy", 2010, 10, "youtube.com");
//	repo2.AddElement(d1);
//	Movie d2("It1", "comedy", 2010, 10, "youtube.com");
//	repo2.AddElement(d2);
//
//	std::stringbuf buffer;
//	std::ostream os(&buffer);
//	os << repo2;
//	assert(buffer.str() == "Title: It | Genre: comedy | Year: 2010 | Likes: 10\n\tTrailer: youtube.com\nTitle: It1 | Genre: comedy | Year: 2010 | Likes: 10\n\tTrailer: youtube.com\n\n");
//}