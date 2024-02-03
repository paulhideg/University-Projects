"""
  Program functionalities module
"""
import copy

from math import sqrt


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
    """
    !!getter function implementation!!

    getter function in functions file

    display_list function in ui
    """
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
    """
   !!getter function implementation!!

   getter function in functions file

   list_real function in ui
     """
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
    """
   !!! parse the function in 2 or more!!!
    """

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


# "REMOVE" FUNCTION
def modify_remove(undo_lst, lst, indexx):
    # if y meets the reqirements, the item
    # with the y index gets removed
    try:
        y = int(indexx)
        if y >= 0 and y < len(lst['a']):
            modify_remove_delete(lst, y)
            print("Item with the index " + str(y) + " has been removed")
            lstt = copy.deepcopy(lst)
            add_to_undo_list(undo_lst, lstt)
        else:
            print("Invalid input")
    except ValueError:
        print("INVALID INPUT!!!")
# END OF "REMOVE" FUNCTION


# "REMOVE X TO Y" FUNCTION
def modify_remove_multiple(undo_lst, lst, starting_index, ending_index):
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
            lstt = copy.deepcopy(lst)
            add_to_undo_list(undo_lst, lstt)
        else:
            print("Invalid input")
    except ValueError:
        print("INVALID INPUT!!!")
# END OF "REMOVE X TO Y" FUNCTION


def modify_replace_ver(undo_lst, lst, replaced_number, replacement_number):
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
        lstt = copy.deepcopy(lst)
        add_to_undo_list(undo_lst, lstt)
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


# "ADD" FUNCTION
def add_add_verify(undo_lst, lst, comp_num):
    # appends the real and imaginary part
    # of the number to the main list
    try:
        lst['a'].append(comp_num[0])
        lst['b'].append(comp_num[1])
        print("Number added to the list!")
        lstt = copy.deepcopy(lst)
        add_to_undo_list(undo_lst, lstt)
    except TypeError:
        print("Invalid number.!..")


def add_add(undo_lst, lst, number_to_be_added):
    # converts the string to a list containing
    # the real part and the imaginary part
    add_num = complex_number_splice(number_to_be_added)
    add_add_verify(undo_lst, lst, add_num)
# END OF "ADD" FUNCTION


# "INSERT" FUNCTION
def add_insert_verify(undo_lst, lst, num, indexx):
    # insert a number (num) to the given position (indexx)
    try:
        if indexx >= 0 and indexx < len(lst['a']):
            # checks if the index is found in the list
            lst['a'].insert(indexx, num[0])
            lst['b'].insert(indexx, num[1])
            print("A number has been added on index ", indexx)
            print(lst)
            lstt = lst.copy()
            lstt = copy.deepcopy(lst)
            add_to_undo_list(undo_lst, lstt)
        else:
            print("Index not in range")
    except TypeError:
        print("Invalid number...")


def add_insert(undo_lst, lst, num_to_be_added, indexx):
    try:
        add_num = complex_number_splice(num_to_be_added)
        indexx = int(indexx)
        add_insert_verify(undo_lst, lst, add_num, indexx)
    except ValueError:
        # if the input is not a number,
        # the next message is displayed
        print("Incorrect index input")
# END OF "INSERT" FUNCTION


def sum_verify(lst, indice1, indice2):
    # if the 2 given indices are correct, we calculate the sum of the elements
    # from indice1 to indice2
    sa = 0
    sb = 0
    for i in range(indice1, indice2+1):
        sa += get_list_item_a(lst, i)
        sb += get_list_item_b(lst, i)
    if sb >= 0:
        print("The sum is " + str(sa) + "+" + str(sb) + "i")
    else:
        print("The sum is " + str(sa) + str(sb) + "i")


def summ(lst, indice1, indice2):
    # sub-list sum function
    try:
        # we check if the 2 given indices are correct
        indice1 = int(indice1)
        indice2 = int(indice2)
        if(indice1 < len(lst["a"]) and indice1 >= 0 and indice2 < len(lst["a"]) and indice2 >= 0 and indice1 <= indice2):
            sum_verify(lst, indice1, indice2)
        else:
            print("Invalid index positions")
    except ValueError:
        print("INVALID INPUT!!!")


def product_verify(lst, indice1, indice2):
    # if the 2 given indices are correct, we calculate the product of the elements
    # from indice1 to indice2
    a = get_list_item_a(lst, indice1)
    b = get_list_item_b(lst, indice1)
    for i in range(indice1+1, indice2+1):
        x = a
        a = a*get_list_item_a(lst, i) - (b*get_list_item_b(lst, i))
        b = b*get_list_item_a(lst, i) + x * get_list_item_b(lst, i)
        print(i)
    if b >= 0:
        print("The product is " + str(a) + "+" + str(b) + "i")
    else:
        print("The product is " + str(a) + str(b) + "i")


def productt(lst, indice1, indice2):
    # sub-list product function
    try:
        # we check if the 2 given indices are correct
        indice1 = int(indice1)
        indice2 = int(indice2)
        if(indice1 < len(lst["a"]) and indice1 >= 0 and indice2 < len(lst["a"]) and indice2 >= 0 and indice1 <= indice2):
            product_verify(lst, indice1, indice2)
        else:
            print("Invalid index positions")
    except ValueError:
        print("INVALID INPUT!!!")


def filter_real(undo_lst, lst):
    # filter real function
    # it removes all the numbers that are not real
    s = 0
    for i in range(len(lst['a'])-1, -1, -1):
        if(get_list_item_b(lst, i) != 0):
            modify_remove_delete(lst, i)
            s += 1
    print(str(s) + " non-real numbers have been removed")
    add_to_undo_list(undo_lst, lst)


def filter_modulo_verify(undo_lst, lst, operation, number):
    # filter modulo function that receives the undo list, the current list, the operation that has to be executed
    # and the number that is used in the operation
    mod = 0
    try:
        # we check if the operation sign is correct
        # if the operation is correct, we remove all the elements that do not meet the condition
        number = int(number)
        for i in range(len(lst['a'])-1, -1, -1):
            moduloo = modulo_calculator(i, lst)
            if operation == "<":
                if moduloo >= number:
                    modify_remove_delete(lst, i)
                    mod += 1
            elif operation == "=":
                if moduloo != number:
                    modify_remove_delete(lst, i)
                    mod += 1
            elif operation == ">":
                if moduloo <= number:
                    modify_remove_delete(lst, i)
                    mod += 1
            else:
                print("Invalid operation")
        if mod > 0:
            print(str(mod)+" numbers have been removed")
            lstt = copy.deepcopy(lst)
            add_to_undo_list(undo_lst, lstt)
        else:
            print("No numbers have been removed from the list")
    except ValueError:
        print("INVALID INPUT!!!")


def add_to_undo_list(undo_lst, listt):
    # if a function modified the list, the new list is added in the undo_list of all previous lists
    c = listt
    undo_lst.insert(len(undo_lst), c)
    print("undo list updated")


def undo_list_modify(undo_list):
    # Rremoves the last operation from the list of operation (undo_list)
    undo_list.pop(len(undo_list)-1)
    print("undo list shortened")
    print(undo_list)


def undo_func(undo_list, lst):
    # the undo function
    if len(undo_list) > 1:  # if we haven't reached at the end of the undo_list, we undo the last operation
        print("Undo successful")
        lst = dict(undo_list[len(undo_list)-2])
        print("list to be returned:")
        print(lst)
        undo_list_modify(undo_list)
        return lst
    if len(undo_list) == 1:
        print("can't undo anymore")
        return lst


def tests():
    test_input_formatter()
    print("1 test passed...")
    test_get_list_item_a_and_b()
    print("2 tests passed...")
    test_set_list_item_a_and_b()
    print("3 tests passed...")
    test_modify_remove_delete()
    print("All tests passed!")
