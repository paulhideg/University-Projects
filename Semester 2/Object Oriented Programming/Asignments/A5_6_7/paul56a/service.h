#pragma once
#include <utility>

#include "repository.h"
#include "validation.h"

class Tutorial_Service {

private:
    Tutorial_Repo tutorial_repo;
    Tutorial_Validation tutorial_validator;

public:

    /// Service constructor with inherited repo and validator
    /// \param tutorial_repo Repo of tutorials
    /// /// \param tutorial_validator Validator of the tutorial
    Tutorial_Service(Tutorial_Repo& tutorial_repo, Tutorial_Validation tutorial_validator) : tutorial_repo{ std::move(tutorial_repo) }, tutorial_validator{ tutorial_validator } {}

    /// Calls the repo and validator to add and validate the tutorial
    /// \param link Link
    /// \param title Title
    /// \param presenter Presenter
    /// \param duration Duration
    /// \param likes_number Number of likes
    void add_tutorial(std::string link, std::string title, std::string presenter, std::string duration, unsigned int likes_number);

    /// Removes the tutorial by link, by calling the repo
    /// \param link Unique identifier
    void remove_tutorial(const std::string& link);

    /// Updates a tutorial by calling the repo
    /// \param link Link
    /// \param title Title
    /// \param presenter Presenter
    /// \param duration Duration
    /// \param likes_number Number of likes
    void update_tutorial(std::string link, std::string title, std::string presenter, std::string duration, unsigned int likes_number);

    /// Populates the array with random valid tutorials
    void populate_array();

    /// Getter for number of tutorials for a given presenter
    /// \return Number of tutorials for a given presenter 
    unsigned int get_number_tutorials_for_presenter(std::string presenter);

    /// Getter for number of tutorials
    /// \return Number of tutorials
    int get_number_tutorials();

    /// Returns the list of tutorials
    /// \return List of tutorials
    Tutorial* list_tutorials();
};
