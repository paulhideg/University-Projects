#include <iostream>
#include <cstdlib>
#include "domain.h"
#include "exceptions.h"
#include "Array.h"
#pragma once


class Tutorial_Repo {

private:
    Array <Tutorial> dynamic_array;

    /// Event finder by link
    /// \param link Unique identifier
    /// \return The 's index if it's found, -1 otherwise
    int find(const std::string& link);

public:

    /// Event Tutorial constructor
    /// \param dynamic_array Inherited from Array class
    explicit Tutorial_Repo(const Array <Tutorial>& dynamic_array) : dynamic_array{ dynamic_array } {};

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
    Tutorial* get_all_tutorials();
};