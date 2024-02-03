#pragma once
#include <string>
#include <sstream>
#include "exceptions.h"


class Tutorial {

private:

    std::string title;
    std::string presenter;
    std::string duration;
    unsigned int likes_number{};
    std::string link;

public:

    Tutorial();
    ~Tutorial();
    Tutorial(std::string& link, std::string& title, std::string& presenter, std::string& duration, unsigned int likes_number);

    /// Link getter
    /// \return The object's link
    std::string get_link();

    /// Title getter
    /// \return The object's title
    std::string get_title();

    /// Presenter getter
    /// \return The object's presenter
    std::string get_presenter();

    /// Duration getter
    /// \return The object's duration
    std::string get_duration();

    /// Number likes getter
    /// \return The object's number of likes
    unsigned int get_likes_number() const;

    /// Title setter
    /// \param new_title
    void set_title(std::string& new_title);

    /// Presenter setter
    /// \param new_presenter
    void set_presenter(std::string& new_presenter);

    ///  Duration setter
    /// \param new_duration
    void set_duration(std::string& new_duration);

    /// Number of likes setter
    /// \param new_likes_number
    void set_likes_number(unsigned int new_likes_number);

    /// Pretty print
    /// \param outputStream The output pretty printed
    /// \param event_to_print Event object
    /// \return The pretty printed string
    friend std::ostream& operator<<(std::ostream& outputStream, const Tutorial& tutorial_to_print);
};