#include "FileRepository.h"
#include <fstream>


FileRepository::FileRepository(const std::string& path, bool initialize) :
	Repository{ Repository() },
	filePath{ path },
	initialize{ initialize }
{
	ReadData();
}

void FileRepository::ReadData()
{
	std::ifstream inputFile;
	inputFile.open(filePath, std::ios::in);

	Tutorial next;
	while (inputFile >> next)
	{
		Repository::AddElement(next);
	}
	inputFile.close();
}

void FileRepository::WriteData()
{
	std::ofstream outputFile;
	outputFile.open(filePath, std::ios::out);

	for (const Tutorial& d : Repository::GetArray())
		outputFile << d;

	outputFile.close();
}

void FileRepository::AddElement(const Tutorial& newTutorial)
{
	Repository::AddElement(newTutorial);
	WriteData();
}

void FileRepository::RemoveElement(size_t position)
{
	Repository::RemoveElement(position);
	WriteData();
}

void FileRepository::UpdateElementTitle(size_t position, std::string newTitle)
{
	Repository::UpdateElementTitle(position, newTitle);
	WriteData();
}

void FileRepository::UpdateElementPresenter(size_t position, std::string newPresenter)
{
	Repository::UpdateElementPresenter(position, newPresenter);
	WriteData();
}

void FileRepository::UpdateElementDuration(size_t position, std::string newDuration)
{
	Repository::UpdateElementDuration(position, newDuration);
	WriteData();
}

void FileRepository::UpdateElementLikes(size_t position, size_t newLikes)
{
	Repository::UpdateElementLikes(position, newLikes);
	WriteData();
}


void FileRepository::UpdateElementLink(size_t position, std::string newLink)
{
	Repository::UpdateElementLink(position, newLink);
	WriteData();
}

bool FileRepository::IsInitializable() const
{
	return initialize;
}

