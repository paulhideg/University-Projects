#pragma once
#include <vector>
#include "domain.h"

class TutorialList
{
public:
	TutorialList();
	void AddTutorial(const Tutorial& tutorial);
	int DeleteTutorial(const Tutorial& tutorial);
	int GetSize(const Tutorial& tutorial);

	const std::vector<Tutorial>& GetList() const;
private:
	std::vector<Tutorial> tutorialList;
};

class TutorialListWriter
{
public:
	virtual void WriteToFile(const TutorialList& tutorialList) = 0;

	const std::string& GetFileName() const;
	void SetFileName(const std::string& newFile);
protected:
	std::string fileName;
};

class CSVTutorialListWriter : public TutorialListWriter
{
public:
	CSVTutorialListWriter(const std::string& fileName);
	void WriteToFile(const TutorialList& adoptionList);
};

class HTMLTutorialListWriter : public TutorialListWriter
{
public:
	HTMLTutorialListWriter(const std::string& fileName);
	void WriteToFile(const TutorialList& adoptionList);
};



