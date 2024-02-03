#include "Ui.h"

void UserInterface::ui_add() {

    char link[61], title[41], presenter[41], duration[41], likes_number[41];
    unsigned int new_likes_number;

    std::cout << "Link:\n";
    std::cin.getline(link, 61);
    if (link[0] == '\0')
        throw UserError("Invalid link\n");

    std::cout << "Title:\n";
    std::cin.getline(title, 41);
    if (title[0] == '\0')
        throw UserError("Invalid title\n");

    std::cout << "Presenter:\n";
    std::cin.getline(presenter, 41);
    if (presenter[0] == '\0')
        throw UserError("Invalid presenter\n");

    std::cout << "Duration (mm:ss) :\n";
    std::cin.getline(duration, 41);
    if (duration[0] == '\0')
        throw UserError("Invalid duration\n");

    std::cout << "Number of likes:\n";
    std::cin.getline(likes_number, 41);
    if (likes_number[0] == '\0')
        throw UserError("Invalid number of likes\n");
    new_likes_number = std::stoi(likes_number);

    this->tutorial_service.add_tutorial(link, title, presenter, duration, new_likes_number);
}

void UserInterface::ui_delete() {

    char link[41];
    std::cout << "Link:\n";
    std::cin.getline(link, 41);
    if (link[0] == '\0')
        throw UserError("Invalid link\n");
    this->tutorial_service.remove_tutorial(link);
}

void UserInterface::ui_update() {

    char link[61], title[41], presenter[41], duration[41], likes_number[41];
    unsigned int new_likes_number;

    std::cout << "Link:\n";
    std::cin.getline(link, 61);
    if (link[0] == '\0')
        throw UserError("Invalid link\n");

    std::cout << "New title:\n";
    std::cin.getline(title, 41);
    if (title[0] == '\0')
        throw UserError("Invalid title\n");

    std::cout << "New presenter:\n";
    std::cin.getline(presenter, 41);
    if (presenter[0] == '\0')
        throw UserError("Invalid presenter\n");

    std::cout << "New duration (mm:ss) :\n";
    std::cin.getline(duration, 41);
    if (duration[0] == '\0')
        throw UserError("Invalid duration\n");

    std::cout << "New number of likes:\n";
    std::cin.getline(likes_number, 41);
    if (likes_number[0] == '\0')
        throw UserError("Invalid number of likes\n");
    new_likes_number = std::stoi(likes_number);

    this->tutorial_service.update_tutorial(link, title, presenter, duration, new_likes_number);
    std::cout << "Tutorial upddated successfully\n";
}

void UserInterface::ui_list() {

    std::vector <Tutorial >tutorials = this->tutorial_service.list_tutorials();
    for (int i = 0; i <= this->tutorial_service.get_number_tutorials() - 1; i++)
        std::cout << tutorials[i];
}

void UserInterface::ui_user_show_tutorials() {

    char command[41], presenter[41];

    while (true)
    {
        try {
            std::cout << "Please enter a presenter:\n";
            std::cin.getline(presenter, 41);

            if (presenter[0] == '\0')
                throw UserError("Invalid presenter\n");
            break;
        }
        catch (UserError& valid_error) {
            std::cout << valid_error.get_message() << std::endl;
        }
        catch (const std::invalid_argument& ia) {
            std::cout << "Invalid presenter" << std::endl;
        }
    }

    if (this->tutorial_service.get_number_tutorials_for_presenter(presenter) == this->user_tutorial_service.get_number_tutorials_for_presenter(presenter))
    {
        std::cout << "All tutorials from this presenter are already in your list of events\n";
        return;
    }

    std::cout << "Did you like this tutorial?:\n";
    std::cout << "If so, you can add it to your watchlist:\n\n";
    std::cout << "'add' - Add event to your list\n";
    std::cout << "If not, feel free to ignore this event:\n";
    std::cout << "'next' - Ignore this event\n\n";
    std::cout << "'exit' - Exit this menu\n\n";

    int i;
    bool valid1, valid2;

    std::vector <Tutorial> tutorials = this->tutorial_service.list_tutorials();
    for (i = 0; i <= this->tutorial_service.get_number_tutorials() - 1; i++)
    {

        valid2 = true;
        if (tutorials[i].get_presenter() != presenter)
            valid2 = false;

        valid1 = true;
        std::vector <Tutorial> user_tutorials = this->user_tutorial_service.list_tutorials();

        if (valid2)
        {
            for (int j = 0; j <= this->user_tutorial_service.get_number_tutorials() - 1; j++)
                if (tutorials[i].get_link() == user_tutorials[j].get_link())
                {
                    valid1 = false;
                    break;
                }
        }

        if (valid1 && valid2)
        {
            std::cout << tutorials[i];
            system(std::string("start " + tutorials[i].get_link()).c_str());
            while (true)
            {
                std::cout << "Please enter your option:\n";
                std::cin.getline(command, 41);
                if (!strcmp(command, "add"))
                {
                    this->user_tutorial_service.add_tutorial(tutorials[i].get_link(),
                        tutorials[i].get_title(),
                        tutorials[i].get_presenter(),
                        tutorials[i].get_duration(),
                        tutorials[i].get_likes_number());
                    command[0] = '\0';
                    if (this->tutorial_service.get_number_tutorials_for_presenter(presenter) == this->user_tutorial_service.get_number_tutorials_for_presenter(presenter))
                    {
                        std::cout << "All tutorials available from this presenter are already in your list of tutorials\n";
                        return;
                    }
                    break;
                }
                else if (!strcmp(command, "next"))
                {
                    command[0] = '\0';
                    break;
                }
                else if (!strcmp(command, "exit"))
                    return;
                else
                {
                    std::cout << "Invalid command\n";
                    command[0] = '\0';
                }
            }
        }
        if (i == this->tutorial_service.get_number_tutorials() - 1)
            i = 0;
    }
    std::cout << "All tutorials available from this presenter are already in your list of tutorials\n";
}

void UserInterface::ui_user_my_tutorials() {

    char command[41];

    if (this->user_tutorial_service.get_number_tutorials() == 0)
    {
        std::cout << "You have no tutorial in your watch list\n";
        return;
    }

    std::vector <Tutorial> user_tutorials = this->user_tutorial_service.list_tutorials();
    for (int i = 0; i <= this->user_tutorial_service.get_number_tutorials() - 1; i++)
        std::cout << user_tutorials[i];

    while (true)
    {
        try {
            std::cout << "\nPlease enter your option:\n\n";
            std::cout << "'delete' - Remove a tutorial\n\n";
            std::cout << "'exit' - Exit this menu\n";
            std::cin.getline(command, 41);
            if (!strcmp(command, "delete"))
            {
                char link[61];
                char command2[41];
                std::cout << "Link:\n";
                std::cin.getline(link, 61);
                
                int i = 0;
                std::vector <Tutorial> tutorials = this->tutorial_service.list_tutorials();
                for (i = 0; i <= this->tutorial_service.get_number_tutorials() - 1; i++)
                    if (tutorials[i].get_link() == link)
                        std::cout << "\nDid you like this tutorial?:\n";
                        std::cout << "'yes' / 'no'\n";
                        std::cin.getline(command2, 41);
                        if (!strcmp(command2, "yes"))
                        {
                            //TODO increasing like number not working
                            //tutorials[i].set_likes_number(tutorials[i].get_likes_number() + 1);

                            /*std::string title, presenter, duration;
                            unsigned int new_likes_number;
                            title = tutorials[i].get_link();
                            presenter = tutorials[i].get_presenter();
                            duration = tutorials[i].get_duration();
                            new_likes_number = tutorials[i].get_likes_number() + 1;
                            this->tutorial_service.update_tutorial(link,title,presenter,duration,new_likes_number);*/
                            
                            std::cout << "Tutorial successfully liked!\n";
                            std::cout << "Tutorial successfully removed from your watchlist!\n";
                        }
                        else if (!strcmp(command2, "no"))
                        {
                            std::cout << "Tutorial successfully removed from your watchlist!\n";
                        }
                        else
                        {
                            std::cout << "Invalid choice\n";
                            std::cout << "Tutorial successfully removed from your watchlist!\n";
                        }
                this->user_tutorial_service.remove_tutorial(link);

                break;
            }
            else if (!strcmp(command, "exit"))
                return;
            else
            {
                std::cout << "Invalid command\n";
                command[0] = '\0';
            }
        }
        catch (RepoError& repo_error) {
            std::cout << repo_error.get_message() << std::endl;
        }
        catch (ValidError& valid_error) {
            std::cout << valid_error.get_message() << std::endl;
        }
        catch (UserError& user_error) {
            std::cout << user_error.get_message() << std::endl;
        }
    }
}

void UserInterface::print_admin_menu() {

    std::cout << "\nHere is a list of your options (Admin Mode):\n\n";
    std::cout << "'add': Add a tutorial\n";
    std::cout << "'delete': Delete a tutorial\n";
    std::cout << "'update': Update an tutorial\n";
    std::cout << "'list': List all tutorials\n";
    std::cout << "'exit': Exit admin mode\n";
}

void UserInterface::print_user_menu() {

    std::cout << "\nHere is a list of your options (User Mode):\n\n";
    std::cout << "'show tutorials': Lists all available tutorials for a presenter of your choosing\n";
    std::cout << "'my tutorials': Lists all tutorials you're interested in\n";
    std::cout << "'exit' - Exit user mode\n";
}

void UserInterface::run()
{
    char command[41], user_command[41], admin_command[41];
    this->tutorial_service.populate_array();
    std::cout << "Welcome to the Tutorials Planner!\n";
    std::cout << "Please enter a option: \n\n";
    std::cout << "'admin' - To enter admin mode\n";
    std::cout << "'user' - To enter user mode\n";
    std::cout << "'exit' - Exit planner\n";
    while (true)
    {
        std::cout << "\nPlease enter a mode (Admin or User):\n";
        std::cin.getline(command, 41);
        if (!strcmp(command, "user"))
        {
            while (true)
            {
                this->print_user_menu();
                std::cout << "Please enter your option:\n";
                std::cin.getline(user_command, 41);
                try {
                    if (!strcmp(user_command, "show tutorials"))
                    {
                        this->ui_user_show_tutorials();
                        user_command[0] = '\0';
                    }
                    else if (!strcmp(user_command, "my tutorials"))
                    {
                        this->ui_user_my_tutorials();
                        user_command[0] = '\0';
                    }
                    else if (!strcmp(user_command, "exit"))
                    {
                        user_command[0] = '\0';
                        break;
                    }
                    else
                    {
                        std::cout << "Invalid command\n";
                        user_command[0] = '\0';
                    }
                }
                catch (RepoError& repo_error) {
                    std::cout << repo_error.get_message() << std::endl;
                }
                catch (ValidError& valid_error) {
                    std::cout << valid_error.get_message() << std::endl;
                }
                catch (UserError& user_error) {
                    std::cout << user_error.get_message() << std::endl;
                }
            }
        }
        else if (!strcmp(command, "admin"))
        {
            this->print_admin_menu();
            while (true) {
                std::cout << "Please enter your option:\n";
                std::cin.getline(admin_command, 41);
                try {
                    if (!strcmp(admin_command, "add")) {
                        this->ui_add();
                        admin_command[0] = '\0';
                    }
                    else if (!strcmp(admin_command, "delete")) {
                        this->ui_delete();
                        admin_command[0] = '\0';
                    }
                    else if (!strcmp(admin_command, "update")) {
                        this->ui_update();
                        admin_command[0] = '\0';
                    }
                    else if (!strcmp(admin_command, "list")) {
                        this->ui_list();
                        std::cout << std::endl;
                        admin_command[0] = '\0';
                    }
                    else if (!strcmp(admin_command, "exit"))
                        break;
                    else
                        std::cout << "Invalid command!\n";
                }
                catch (RepoError& repo_error) {
                    std::cout << repo_error.get_message() << std::endl;
                }
                catch (ValidError& valid_error) {
                    std::cout << valid_error.get_message() << std::endl;
                }
                catch (UserError& user_error) {
                    std::cout << user_error.get_message() << std::endl;
                }
                catch (const std::invalid_argument& ia) {
                    std::cout << "Invalid number of people" << std::endl;
                }
            }
            command[0] = '\0';
        }
        else if (!strcmp(command, "exit"))
            return;
        else
        {
            std::cout << "Invalid mode!\n";
            command[0] = '\0';
        }
    }
}
