#include "Array.h"
#include "domain.h"
#include "exceptions.h"
#include "repository.h"
#include "service.h"
#include "validation.h"
#include <cassert>
#include <sstream>
#pragma once

class Testing {

private:
    static void test_array();
    static void test_domain();
    static void test_repo();
    static void test_service();
    static void test_validation();

public:
    Testing() = default;
    static void run_tests();
    ~Testing();
};