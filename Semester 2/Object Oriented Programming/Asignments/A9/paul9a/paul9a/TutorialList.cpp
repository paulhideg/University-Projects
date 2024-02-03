#include "TutorialList.h"
#include "HTMLTable.h"
#include <fstream>

TutorialList::TutorialList() :
	tutorialList{ std::vector<Tutorial>() }
{
}

void TutorialList::AddTutorial(const Tutorial& tut)
{
	auto pos = std::find(tutorialList.begin(), tutorialList.end(), tut);

	if (pos != tutorialList.end()) throw std::exception("Tutorial already in tutorial list!");
	tutorialList.push_back(tut);
}

int TutorialList::DeleteTutorial(const Tutorial& tut)
{
	auto pos = std::find(tutorialList.begin(), tutorialList.end(), tut);
	if (pos >= tutorialList.end()) return false;
	else {
		tutorialList.erase(pos);
		return true;
	}
}

int TutorialList::GetSize(const Tutorial& tutorial)
{
	return tutorialList.size();
}

const std::vector<Tutorial>& TutorialList::GetList() const
{
	return tutorialList;
}

CSVTutorialListWriter::CSVTutorialListWriter(const std::string& fileName)
{
	SetFileName(fileName);
}

void CSVTutorialListWriter::WriteToFile(const TutorialList& tutorialList)
{
	std::ofstream outputFile;
	outputFile.open(fileName, std::ios_base::out);

	for (auto& m : tutorialList.GetList())
	{
		outputFile << m.GetTitle() << ',' << m.GetPresenter() << ',' << m.GetDuration() << ',' << m.GetLikes() << ',' << m.GetLink();
		outputFile << '\n';
	}

	outputFile.close();
}

HTMLTutorialListWriter::HTMLTutorialListWriter(const std::string& fileName)
{
	SetFileName(fileName);
}

void HTMLTutorialListWriter::WriteToFile(const TutorialList& tutorialList)
{
	std::ofstream outputFile;
	outputFile.open(fileName, std::ios_base::out);

	outputFile << "<!DOCTYPE html>";

	outputFile << "<html>";
	outputFile << "<head>";
	outputFile << "<title> Tutorial List </title>";
	outputFile << "</head>";

	outputFile << "<body>";

	HTMLTable table = HTMLTable();
	HTMLTable::Row topRow;
	topRow.AddToRow("Title");
	topRow.AddToRow("Presenter");
	topRow.AddToRow("Duration");
	topRow.AddToRow("Number of likes");
	topRow.AddToRow("Link");
	table.AddRow(topRow);
	for (auto& m : tutorialList.GetList())
	{
		HTMLTable::Row newRow;
		newRow.AddToRow(m.GetTitle());
		newRow.AddToRow(m.GetPresenter());
		newRow.AddToRow(m.GetDuration());
		newRow.AddToRow(std::to_string(m.GetLikes()));
		newRow.AddToRow(m.GetLink());
		table.AddRow(newRow);
	}

	outputFile << table;

	outputFile << "</body>";

	outputFile << "</html>";

	outputFile.close();
}

const std::string& TutorialListWriter::GetFileName() const
{
	return fileName;
}

void TutorialListWriter::SetFileName(const std::string& newFile)
{
	fileName = newFile;
}
