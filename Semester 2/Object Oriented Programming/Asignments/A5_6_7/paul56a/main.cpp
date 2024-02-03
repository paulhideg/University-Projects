#include "Ui.h"
#include "tests.h"

/// Main function, run the tests and creating the repo's
/// return 0
int main()
{
    Testing::run_tests();

    Array <Tutorial> dynamic_array(1);
    Tutorial_Repo tutorial_repo(dynamic_array);
    Tutorial_Validation tutorial_validator;
    Tutorial_Service tutorial_service(tutorial_repo, tutorial_validator);

    Array <Tutorial> user_dynamic_array(1);
    Tutorial_Repo user_tutorial_repo(user_dynamic_array);
    Tutorial_Service user_service_repo(user_tutorial_repo, tutorial_validator);

    UserInterface ui(tutorial_service, user_service_repo);
    ui.run();

    return 0;
}