#pragma once
#include "Repository.h"

class FileRepository :
    public Repository
{
public:
    FileRepository(const std::string& path, bool initialize = false);

    void AddElement(const Tutorial& newTutorial) override;
    void RemoveElement(size_t position) override;

    void UpdateElementTitle(size_t position, std::string newTitle) override;
    void UpdateElementPresenter(size_t position, std::string newPresenter) override;
    void UpdateElementDuration(size_t position, std::string newDuration) override;
    void UpdateElementLikes(size_t position, size_t newLikes) override;
    void UpdateElementLink(size_t position, std::string newLink) override;

    bool IsInitializable() const;
protected:
    std::string filePath;
    bool initialize;
private:
    void ReadData();
    void WriteData();
};
