"""
  User interface module
"""
from functions import *

# MODIFY MENU FUNCTIONS


def filter_menu_verify(undo_lst, x, lst):
    if len(x) == 2 and x[0] == "filter" and x[1] == "real":
        filter_real(undo_lst, lst)
    elif len(x) == 4 and x[0] == "filter" and x[1] == "modulo" and (x[2] == "<" or x[2] == "=" or x[2] == ">"):
        filter_modulo_verify(undo_lst, lst, x[2], x[3])
    else:
        print("Invalid input")


def sub_list_menu_verify(x, lst):
    if len(x) == 4 and x[0] == "sum" and x[2] == "to":
        summ(lst, x[1], x[3])
    elif len(x) == 4 and x[0] == "product" and x[2] == "to":
        productt(lst, x[1], x[3])
    else:
        print("Invalid input")


def display_menu_verify(x, lst):
    # verifies if the input coresponds to
    if len(x) == 1 and x[0] == "-1":
        return  # exit sequence
    elif len(x) == 1 and x[0] == "list":
        display_list(lst)
        # "list" function
    elif len(x) == 5 and x[0] == "list" and x[1] == "real" and x[3] == "to":
        list_real_verify(lst, x[2], x[4])
        # "list real" function
    elif len(x) == 4 and x[0] == "list" and x[1] == "modulo" and (x[2] == "<" or x[2] == "=" or x[2] == ">"):
        list_modulo_verify(lst, x[2], x[3])
        # "list modulo" function
    else:
        print("Invalid input")
# END OF DISPLAY MENU FUNCTIONS


def modify_menu_verify(undo_lst, x, lst):
    if len(x) == 2 and x[0] == "remove":
        modify_remove(undo_lst, lst, x[1])
        # remove function
    elif len(x) == 4 and x[0] == "remove" and x[2] == "to":
        modify_remove_multiple(undo_lst, lst, x[1], x[3])
        # remove x to y function
    elif len(x) == 4 and x[0] == "replace" and x[2] == "with":
        modify_replace(undo_lst, lst, x[1], x[3])
        # replace x with y function
    else:
        print("INVALID INPUT...")
# END OF MODIFY MENU FUNCTIONS


def add_menu_verify(undo_lst, x, lst):
    if len(x) == 2 and x[0] == "add":
        add_add(undo_lst, lst, x[1])
        # add function
    elif len(x) == 4 and x[0] == "insert" and x[2] == "at":
        add_insert(undo_lst, lst, x[1], x[3])
        # insert function
    else:
        print("Invalid input...")
# END OF ADD MENU FUNCTIONS


def secondary_menu_input(lst):
    # the function receives the input from the user, a string
    # and returns a list of all the elements of the string
    x = input(">>")
    return input_formatter(x)


def filter_menu(undo_lst, lst):
    while True:
        print("\nWelcome to the filter menu")
        print("Use the following commands to filter the list:")
        print("filter real e.g. filter real")
        print("filter modulo [ < | = | > ] <number> e.g. filter modulo < 10")
        print("press -1 to exit the filter menu")
        x = secondary_menu_input(lst)  # exist sequence
        if len(x) == 1 and x[0] == "-1":
            return
        filter_menu_verify(undo_lst, x, lst)
        #verify_undo_list(undo_lst[len(undo_lst)-1], lst, undo_lst)


def sub_list_menu(lst):
    while True:
        print("\nWelcome to the display menu")
        print(
            "Use the following commands to obtain different characteristics of sub-lists:")
        print("sum <start position> to <end position> e.g. sum 1 to 5")
        print("product <start position> to <end position> e.g. product 1 to 5")
        print("press -1 to exit the sub-list menu")
        x = secondary_menu_input(lst)  # exist sequence
        if len(x) == 1 and x[0] == "-1":
            return
        sub_list_menu_verify(x, lst)


def display_menu(lst):
    while True:
        print("\nWelcome to the display menu")
        print("Use the following commands to list numbers:")
        print("list e.g. list")
        print("list real <start position> to <end position> e.g. list real 1 to 5")
        print("list modulo [ < | = | > ] <number> e.g. list modulo = 5")

        x = secondary_menu_input(lst)  # exist sequence
        if len(x) == 1 and x[0] == "-1":
            return
        display_menu_verify(x, lst)


def modify_menu(undo_lst, lst):
    while True:
        print("\nWelcome to the modify menu")
        print("Use the following commands to modify a number:")
        print("remove <position> e.g. remove 1")
        print("remove <start position> to <end position> e.g. remove 1 to 3")
        print("replace <old number> with <new number> e.g. replace 1+3i with 5-3i")
        print("press -1 to exit the modify menu")
        x = secondary_menu_input(lst)  # exist sequence
        if len(x) == 1 and x[0] == "-1":
            return
        modify_menu_verify(undo_lst, x, lst)
        #verify_undo_list(undo_lst[len(undo_lst)-1], lst, undo_lst)


def add_menu(undo_lst, lst):
    while True:
        print("\nWelcome to the add menu")
        print("Use the following commands to add a number:")
        print("add <number> e.g. add 4+2i")
        print("insert <number> at <position> e.g. insert 1+1i at 1")
        print("press -1 to exit the add menu")
        x = secondary_menu_input(lst)  # exist sequence
        if len(x) == 1 and x[0] == "-1":
            return
        add_menu_verify(undo_lst, x, lst)
        #verify_undo_list(undo_lst[len(undo_lst)-1], lst, undo_lst)


def main_menu():
    print("\nWelcome to the main menu")
    print("Press:")
    print("a for adding a number in 2 different ways")
    print("b for modifying a number in 3 different modes")
    print("c for displaying numbers having different properties using 3 different methods")
    print("d for displaying different sub-lists in 2 ways")
    print("e for filtering the list in 2 different modes")
    print("undo for undoing the last operation that modified program data ")
    print("-1 to quit the program")


def main_menu_invalid_command():
    # it prints an adequate message if
    # the user inputs anything else than a,b or c
    print("Invalid command")


def start():
    lst = {
        "a": [5, 3, 2, 1, 3, 5, 7, 5, 3, 9],  # real part
        "b": [5, 9, 2, 0, 0, 6, 2, 1, 3, 7]  # imaginary part
    }
    undo_lst = [{
        "a": [5, 3, 2, 1, 3, 5, 7, 5, 3, 9],
        "b": [5, 9, 2, 0, 0, 6, 2, 1, 3, 7]
    }
    ]
    while True:
        main_menu()
        cmd = input(">>>")
        if cmd == "a":
            add_menu(undo_lst, lst)
        elif cmd == "b":
            modify_menu(undo_lst, lst)
        elif cmd == "c":
            display_menu(lst)
        elif cmd == "d":
            sub_list_menu(lst)
        elif cmd == "e":
            filter_menu(undo_lst, lst)
        elif cmd == "undo":
            lst = undo_func(undo_lst, lst)
        elif cmd == "-1":
            return
        else:
            main_menu_invalid_command()
