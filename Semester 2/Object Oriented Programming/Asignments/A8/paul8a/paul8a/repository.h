#include <iostream>
#include <cstdlib>
#include "domain.h"
#include "exceptions.h"
#include <vector>
#pragma once


class Tutorial_Repo {

private:
    std::vector <Tutorial> dynamic_array;

    /// Event finder by link
    /// \param link Unique identifier
    /// \return The 's index if it's found, -1 otherwise
    int find(const std::string& link);

public:

    /// Event Tutorial constructor
    /// \param dynamic_array Inherited from Array class
    Tutorial_Repo() = default;

    /// Adds a tutorial to the dynamic array
    /// \param tutorial Tutorial to be added
    void add(Tutorial event);

    /// Removes a tutorial from the dynamic array
    /// \param link Link from the Tutorial to be removed
    void remove(const std::string& link);

    /// Updates and tutorial from the dynamic array
    /// \param tutorial The new tutorial 
    void update(Tutorial event);

    /// Number of tutorials getter
    /// \return Number of tutorials
    int get_tutorial_number();

    /// All tutorials getter
    /// \return All tutorials 
    std::vector<Tutorial> get_all_tutorials();
};