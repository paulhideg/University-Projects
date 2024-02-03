#pragma once
#include <string>
#include <cstring>
#include "exceptions.h"

class Tutorial_Validation {

private:

    /// Title Validation
    /// \param title Title
    static void validate_title(const std::string& title);

    /// Presenter validator
    /// \param presenter Presenter
    static void validate_presenter(const std::string& presenter);

    /// Duration validator
    /// \param duration Duration
    static void validate_duration(const std::string& duration);

public:

    /// Link validator (ID)
    /// \param link Link
    static void validate_link(std::string link);

    /// Tutorial Validator (Whole tutorial)
    /// \param link Link
    /// \param title Title
    /// \param presenter Presenter
    /// \param duration Duration
    static void validate_tutorial(std::string link, const std::string& title, const std::string& presenter, const std::string& duration);

};
