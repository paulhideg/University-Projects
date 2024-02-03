"""
  Write non-UI functions below
"""


from math import sqrt


def main_menu_invalid_command():
    # it prints an adequate message if
    # the user inputs anything else than a,b or c
    print("Invalid command")


def input_formatter(x):
    # input  - a string
    # output  - a list of the elements of the string,
    # separated by a space
    # the function also removes any extra spaces
    x = x.strip()
    x = " ".join(x.split())
    x = x.split(" ")
    return x


# test function for the input_formatter(x) function
def test_input_formatter():
    x = "    test     test    "
    assert(['test', 'test'] == input_formatter(x))


def secondary_menu_input(lst):
    # the function receives the input from the user, a string
    # and returns a list of all the elements of thr string
    x = input(">>")
    return input_formatter(x)


# getter function to get a list item (real part) with the "i" index
def get_list_item_a(lst, i):
    return lst["a"][i]


# getter function to get a list item(imaginary part) with the "i" index
def get_list_item_b(lst, i):
    return lst["b"][i]


# test function for get_list_item_a and get_list_item_b
def test_get_list_item_a_and_b():
    lst = {
        "a": [10, 20],
        "b": [100, 200]
    }
    index1 = 0
    index2 = 1
    assert(lst['a'][index1] == get_list_item_a(lst, index1))
    assert(lst['a'][index2] == get_list_item_a(lst, index2))
    assert(lst['b'][index1] == get_list_item_b(lst, index1))
    assert(lst['b'][index2] == get_list_item_b(lst, index2))


# setter function to modify a list item (real part) with the set_num
def set_list_item_a(lst, i, set_num):
    lst['a'][i] = set_num


# setter function to modify a list item (imaginary part) with the set_num
def set_list_item_b(lst, i, set_num):
    lst['b'][i] = set_num


# test function for set_list_item_a and set_list_item_b
def test_set_list_item_a_and_b():
    lst = {
        "a": [10, 20],
        "b": [100, 200]
    }
    index1 = 0
    index2 = 1
    new_number1 = 11
    set_list_item_a(lst, index1, new_number1)
    check1 = lst['a'][0]
    set_list_item_a(lst, index2, new_number1)
    check2 = lst['a'][1]
    set_list_item_b(lst, index1, new_number1)
    check3 = lst['b'][0]
    set_list_item_b(lst, index2, new_number1)
    check4 = lst['b'][1]
    assert(new_number1 == check1)
    assert(new_number1 == check2)
    assert(new_number1 == check3)
    assert(new_number1 == check4)


def modify_remove_delete(lst, y):
    # removes the number with the y index
    lst['a'].pop(y)
    lst['b'].pop(y)


# test function for modify_remove_delete function
def test_modify_remove_delete():
    lst = {
        "a": [10, 20],
        "b": [100, 200]
    }
    index1 = 1
    modify_remove_delete(lst, index1)
    lst_var_1 = {
        'a': [10],
        'b': [100]
    }
    assert(lst_var_1 == lst)

    index2 = 0
    modify_remove_delete(lst, index2)
    lst_var_2 = {
        'a': [],
        'b': []
    }
    assert(lst_var_2 == lst)


def complex_number_splice_verify(num):
    # checks if the number has the imaginary part ending with i
    # (the condition for the number to be complex)
    # returns a list with 2 integers: the real part and the imaginary part of the number
    try:
        l = []
        real = int(num[0])
        if num[1].endswith("i"):
            if len(num[1]) == 1:
                # if the imaginary part is of the form "x+i", then the imaginary part is taken to be 1
                imag = 1
                l.append(real)
                l.append(imag)
                return l
            else:
                num[1] = num[1].rstrip("i")
                imag = int(num[1])
                l.append(real)
                l.append(imag)
                return l
        else:
            print("Invalid imaginary part")
            return
    except (ValueError, IndexError):
        print("INVALID INPUT!")


def complex_number_splice(number):
    # splits the input in a list using the split command with the + sign
    number = number.split("+")
    return complex_number_splice_verify(number)
# DISPLAY MENU FUNCTIONS


# "LIST" FUNCTION
def display_list(lst):
    # displays the entire list
    la = []
    lb = []
    for i in range(len(lst['a'])):
        la.append(get_list_item_a(lst, i))
        lb.append(get_list_item_b(lst, i))
    print(la)
    print(lb)
# END OF "LIST" FUNCTION


# "LIST REAL" FUNCTION
def list_real(lst, indice1, indice2):
    # function that creates 2 list and appends them each with
    # the real numbers that are found in the list between the 2 given indices
    la = []
    lb = []
    for i in range(int(indice1), int(indice2)+1):
        if(get_list_item_b(lst, i) == 0):
            la.append(get_list_item_a(lst, i))
            lb.append(get_list_item_b(lst, i))
    print(la)
    print(lb)


def list_real_verify(lst, indice1, indice2):
    # function that verifies if the indices are convenient
    try:
        indice1 = int(indice1)
        indice2 = int(indice2)
        if(indice1 < len(lst["a"]) and indice1 >= 0 and indice2 < len(lst["a"]) and indice2 >= 0 and indice1 <= indice2):
            list_real(lst, indice1, indice2)
        else:
            print("Invalid index positions")
    except ValueError:
        print("INVALID INPUT!!!")
# END OF "LIST REAL" FUNCTION


# "LIST MODULO" FUNCTION
def modulo_calculator(i, lst):
    # calculates the modulo of a complex number
    import math
    a = get_list_item_a(lst, i)
    b = get_list_item_b(lst, i)
    modul = sqrt(a**2 + b**2)
    return modul


def list_modulo_verify(lst, operation, number):
    # function that verifies if the complex number
    # corresponds to the requested modulo function
    try:
        number = int(number)
        la = []
        lb = []
        for i in range(len(lst['a'])):
            moduloo = modulo_calculator(i, lst)
            if operation == "<":
                if moduloo < number:
                    la.append(get_list_item_a(lst, i))
                    lb.append(get_list_item_b(lst, i))
            elif operation == "=":
                if moduloo == number:
                    la.append(get_list_item_a(lst, i))
                    lb.append(get_list_item_b(lst, i))
            elif operation == ">":
                if moduloo > number:
                    la.append(get_list_item_a(lst, i))
                    lb.append(get_list_item_b(lst, i))
            else:
                print("Invalid operation")
        if(len(la) == 0):
            print("No numbers corresponding to the requirements")
        else:
            print(la)
            print(lb)
    except ValueError:
        print("INVALID INPUT!!!")
# END OF "LIST MODULO" FUNCTION


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


# MODIFY MENU FUNCTIONS


# "REMOVE" FUNCTION
def modify_remove(lst, indexx):
    # if y meets the reqirements, the item
    # with the y index gets removed
    try:
        y = int(indexx)
        if y >= 0 and y < len(lst['a']):
            modify_remove_delete(lst, y)
            print("Item with the index " + str(y) + " has been removed")
        else:
            print("Invalid input")
    except ValueError:
        print("INVALID INPUT!!!")
# END OF "REMOVE" FUNCTION


# "REMOVE X TO Y" FUNCTION
def modify_remove_multiple(lst, starting_index, ending_index):
    # if the starting index and the ending indexes are
    # numbers and are meeting the requirements,
    # the complex numbers that are comtained in those indices are removed
    try:
        startt = int(starting_index)
        print(startt)
        endd = int(ending_index)
        print(endd)
        if startt >= 0 and startt < len(lst['a']) and endd >= startt and endd < len(lst['a']):
            for i in range(endd, startt-1, -1):
                print(i)
                modify_remove_delete(lst, i)
            print("Items from the position " + str(startt) +
                  " to position " + str(endd) + " have been removed")
        else:
            print("Invalid input")
    except ValueError:
        print("INVALID INPUT!!!")
# END OF "REMOVE X TO Y" FUNCTION


def modify_replace_ver(lst, replaced_number, replacement_number):
    # replaces all the appearances of the inputed number (to be replaced)
    # with the replacement number
    try:
        changes = 0
        for i in range(len(lst['a'])):
            if lst['a'][i] == replaced_number[0] and lst['b'][i] == replaced_number[1]:
                set_list_item_a(lst, i, replacement_number[0])
                # setter function called
                set_list_item_b(lst, i, replacement_number[1])
                # setter function called
                changes += 1  # counts how many times the numbers have been found and modified
        print(str(changes) + " numbers have been modified")
    except TypeError:
        print("INVALID INPUT!!!")


# "REPLACE X WITH Y" FUNCTION
def modify_replace(lst, number_in_list, number_replacement):
    # it replaces the old number (number_in_list) with
    # the new number (number_replacement)
    # but only  after the the 2 inputs are converted to 2 lists
    # containing the real and the imaginary part
    # of both numbers
    replaced = complex_number_splice(number_in_list)
    replacement = complex_number_splice(number_replacement)
    modify_replace_ver(lst, replaced, replacement)
# END OF "REPLACE X WITH Y" FUNCTION


def modify_menu_verify(x, lst):
    if len(x) == 2 and x[0] == "remove":
        modify_remove(lst, x[1])
        # remove function
    elif len(x) == 4 and x[0] == "remove" and x[2] == "to":
        modify_remove_multiple(lst, x[1], x[3])
        # remove x to y function
    elif len(x) == 4 and x[0] == "replace" and x[2] == "with":
        modify_replace(lst, x[1], x[3])
        # replace x with y function
    else:
        print("INVALID INPUT...")
# END OF MODIFY MENU FUNCTIONS


# ADD MENU FUNCTIONS


# "ADD" FUNCTION
def add_add_verify(lst, comp_num):
    # appends the real and imaginary part
    # of the number to the main list
    try:
        lst['a'].append(comp_num[0])
        lst['b'].append(comp_num[1])
        print("Number added to the list!")
    except TypeError:
        print("Invalid number...")


def add_add(lst, number_to_be_added):
    # converts the string to a list containing
    # the real part and the imaginary part
    add_num = complex_number_splice(number_to_be_added)
    add_add_verify(lst, add_num)
# END OF "ADD" FUNCTION


# "INSERT" FUNCTION
def add_insert_verify(lst, num, indexx):
    # insert a number (num) to the given position (indexx)
    try:
        if indexx >= 0 and indexx < len(lst['a']):
            # checks if the index is found in the list
            lst['a'].insert(indexx, num[0])
            lst['b'].insert(indexx, num[1])
            print("A number has been added on index ", indexx)
        else:
            print("Index not in range")
    except TypeError:
        print("Invalid number...")


def add_insert(lst, num_to_be_added, indexx):
    try:
        add_num = complex_number_splice(num_to_be_added)
        indexx = int(indexx)
        add_insert_verify(lst, add_num, indexx)
    except ValueError:
        # if the input is not a number,
        # the next message is displayed
        print("Incorrect index input")
# END OF "INSERT" FUNCTION


def add_menu_verify(x, lst):
    if len(x) == 2 and x[0] == "add":
        add_add(lst, x[1])
        # add function
    elif len(x) == 4 and x[0] == "insert" and x[2] == "at":
        add_insert(lst, x[1], x[3])
        # insert function
    else:
        print("Invalid input...")
# END OF ADD MENU FUNCTIONS


""" 
  Write the command-driven UI below
"""


def display_menu(lst):
    while True:
        print("Welcome to the display menu")
        print("Use the following commands to list numbers:")
        print("list e.g. list")
        print("list real <start position> to <end position> e.g. list real 1 to 5")
        print("list modulo [ < | = | > ] <number> e.g. list modulo = 5")
        print("press -1 to exit the display menu")
        x = secondary_menu_input(lst)  # exist sequence
        if len(x) == 1 and x[0] == "-1":
            return
        display_menu_verify(x, lst)


def modify_menu(lst):
    while True:
        print("Welcome to the modify menu")
        print("Use the following commands to modify a number:")
        print("remove <position> e.g. remove 1")
        print("remove <start position> to <end position> e.g. remove 1 to 3")
        print("replace <old number> with <new number> e.g. replace 1+3i with 5-3i")
        print("press -1 to exit the modify menu")
        x = secondary_menu_input(lst)  # exist sequence
        if len(x) == 1 and x[0] == "-1":
            return
        modify_menu_verify(x, lst)


def add_menu(lst):
    while True:
        print("Welcome to the add menu")
        print("Use the following commands to add a number:")
        print("add <number> e.g. add 4+2i")
        print("insert <number> at <position> e.g. insert 1+1i at 1")
        print("press -1 to exit the add menu")
        x = secondary_menu_input(lst)  # exist sequence
        if len(x) == 1 and x[0] == "-1":
            return
        add_menu_verify(x, lst)


def main_menu():
    print("Welcome to the main menu")
    print("Press:")
    print("a for adding a number in 2 different ways")
    print("b for modifying a number in 3 different modes")
    print("c for displaying numbers having different properties using 3 different methods")
    print("-1 to quit the program")


def start():
    lst = {
        "a": [5, 3, 2, 1, 3, 5, 7, 5, 3, 9],  # real part
        "b": [5, 9, 2, 0, 0, 6, 2, 1, 3, 7]  # imaginary part
    }
    while True:
        main_menu()
        cmd = input(">>>")
        if cmd == "a":
            add_menu(lst)
        elif cmd == "b":
            modify_menu(lst)
        elif cmd == "c":
            display_menu(lst)
        elif cmd == "-1":
            return
        else:
            main_menu_invalid_command()


def tests():
    test_input_formatter()
    print("1 test passed...")
    test_get_list_item_a_and_b()
    print("2 tests passed...")
    test_set_list_item_a_and_b()
    print("3 tests passed...")
    test_modify_remove_delete()
    print("All tests passed!")


def main():
    tests()
    start()


main()
