#include "tests.h"

Testing::~Testing() = default;

void Testing::test_array() {


    Array <Tutorial> test_dynamic_array(2);
    Array <Tutorial> test_dynamic_array2(2);

    std::string link = "www.ro.com";
    std::string title = "title";
    std::string presenter = "desc";
    std::string duration = "59:59";
    Tutorial test_tutorial(link, title, presenter, duration, 45);
    test_dynamic_array.append_array(test_tutorial);

    test_tutorial + test_dynamic_array2;
    assert(test_dynamic_array2.get_size() == 1);

    Array <Tutorial> test_dynamic_array1(test_dynamic_array);
    assert(test_dynamic_array1.get_size() == 1);
}


void Testing::test_domain() {

    Tutorial default_tuorial{};

    std::string link = "www.1.com";
    std::string title = "title";
    std::string presenter = "pres";
    std::string duration = "59:59";
    Tutorial test_tutorial(link, title, presenter, duration, 45);

    assert(test_tutorial.get_link() == link);
    assert(test_tutorial.get_title() == title);
    assert(test_tutorial.get_presenter() == presenter);
    assert(test_tutorial.get_duration() == duration);
    assert(test_tutorial.get_likes_number() == 45);

    std::string link1 = "www.2.com";
    std::string title1 = "title";
    std::string presenter1 = "pres";
    std::string duration1 = "12:12";
    Tutorial test_tutorial1(link1, title1, presenter1, duration1, 90);

    std::string new_title = "new title";
    test_tutorial.set_title(new_title);
    assert(test_tutorial.get_title() == new_title);

    std::string new_presenter= "new presenter";
    test_tutorial.set_presenter(new_presenter);
    assert(test_tutorial.get_presenter() == new_presenter);

    std::string new_duration = "new duration";
    test_tutorial.set_duration(new_duration);
    assert(test_tutorial.get_duration() == new_duration);

    test_tutorial.set_likes_number(80);
    assert(test_tutorial.get_likes_number() == 80);

    std::stringstream string_tutorial;
    string_tutorial << test_tutorial;
    assert(string_tutorial.str() == "www.1.com | new title | new presenter | new duration | 80\n");
}

void Testing::test_repo() {

    Array<Tutorial> test_dynamic_array(1);
    Tutorial_Repo test_tutorial_repo(test_dynamic_array);
    Tutorial default_tutorial{};

    std::string link = "www.1.com";
    std::string title = "title";
    std::string presenter = "pres";
    std::string duration = "12:12";
    Tutorial test_tutorial(link, title, presenter, duration, 45);

    test_tutorial_repo.add(test_tutorial);
    assert(test_tutorial_repo.get_tutorial_number() == 1);

    try {
        test_tutorial_repo.add(test_tutorial);
    }
    catch (RepoError& re) {
        assert(true);
    }

    std::string link1 = "www.2.com";
    Tutorial test_tutorial1(link1, title, presenter, duration, 80);

    try {
        test_tutorial_repo.update(test_tutorial1);
    }
    catch (RepoError& re) {
        assert(true);
    }

    test_tutorial_repo.update(test_tutorial);

    std::string link2 = "www.3.com";
    Tutorial test_tutorial2(link2, title, presenter, duration, 60);
    test_tutorial_repo.add(test_tutorial2);

    try {
        test_tutorial_repo.remove(test_tutorial1.get_link());
    }
    catch (RepoError& re) {
        assert(true);
    }

    test_tutorial_repo.remove(test_tutorial.get_link());
    assert(test_tutorial_repo.get_tutorial_number() == 1);

    //assert(test_tutorial_repo.get_tutorial
}

void Testing::test_service() {

    Array<Tutorial> test_dynamic_array(1);
    Tutorial_Repo test_tutorial_repo(test_dynamic_array);
    Tutorial_Validation test_tutorial_validation;
    Tutorial_Service test_tutorial_service(test_tutorial_repo, test_tutorial_validation);

    std::string link = "www.1.com";
    std::string title = "title";
    std::string presenter = "pres";
    std::string duration = "12:12";

    test_tutorial_service.add_tutorial(link, title, presenter, duration, 10);
    assert(test_tutorial_service.get_number_tutorials() == 1);

    test_tutorial_service.update_tutorial(link, title, presenter, duration, 50);
    assert(test_tutorial_service.list_tutorials()[0].get_likes_number() == 50);

    assert(test_tutorial_service.get_number_tutorials_for_presenter(presenter) == 1);

    test_tutorial_service.remove_tutorial(link);
    assert(test_tutorial_service.get_number_tutorials() == 0);

    test_tutorial_service.populate_array();
    assert(test_tutorial_service.get_number_tutorials() == 10);

    std::string test_presenter = "not_a_presenter";
    assert(test_tutorial_service.get_number_tutorials_for_presenter(test_presenter) == 0);

}

void Testing::test_validation() {

    std::string link;
    try {
        Tutorial_Validation::validate_link(link);
    }
    catch (ValidError& ve) {
        assert(true);
    }

    std::string link1 = "121";
    try {
        Tutorial_Validation::validate_link(link1);
    }
    catch (ValidError& ve) {
        assert(true);
    }
    std::string link2 = "ww2.olm.moc";
    try {
        Tutorial_Validation::validate_link(link2);
    }
    catch (ValidError& ve) {
        assert(true);
    }

    std::string link3;
    std::string title;
    std::string presenter;
    std::string duration;
    try {
        Tutorial_Validation::validate_tutorial(link3, title, presenter, duration);
    }
    catch (ValidError& ve) {
        assert(true);
    }

    std::string duration0 = "123";
    try {
        Tutorial_Validation::validate_tutorial(link3, title, presenter, duration0);
    }
    catch (ValidError& ve) {
        assert(true);
    }

    std::string duration1 = "11 11";
    try {
        Tutorial_Validation::validate_tutorial(link3, title, presenter, duration1);
    }
    catch (ValidError& ve) {
        assert(true);
    }

    std::string duration2 = "00:00";
    try {
        Tutorial_Validation::validate_tutorial(link3, title, presenter, duration2);
    }
    catch (ValidError& ve) {
        assert(true);
    }

    std::string duration3 = "11:99";
    try {
        Tutorial_Validation::validate_tutorial(link3, title, presenter, duration3);
    }
    catch (ValidError& ve) {
        assert(true);
    }

    std::string duration4 = "1a:05";
    try {
        Tutorial_Validation::validate_tutorial(link3, title, presenter, duration4);
    }
    catch (ValidError& ve) {
        assert(true);
    }
}

void Testing::run_tests() {

    test_array();
    test_domain();
    test_repo();
    test_service();
    test_validation();
}
