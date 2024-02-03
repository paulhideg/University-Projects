#include <iostream>
#include <string>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <cstdlib>
#include <windows.h>
#include <shellapi.h>
#include "validation.h"
#include "service.h"
#include "exceptions.h"
#pragma once


class UserInterface {

private:

    Tutorial_Service tutorial_service;
    Tutorial_Service user_tutorial_service;

    void ui_add();
    void ui_delete();
    void ui_update();
    void ui_list();
    static void print_admin_menu();

    void ui_user_show_tutorials();
    void ui_user_my_tutorials();
    static void print_user_menu();

public:

    explicit UserInterface(Tutorial_Service  tutorial_service, 
                           Tutorial_Service  user_tutorial_service) : 
                           tutorial_service(std::move(tutorial_service)), 
                           user_tutorial_service(std::move(user_tutorial_service)) {};
    void run();

};
