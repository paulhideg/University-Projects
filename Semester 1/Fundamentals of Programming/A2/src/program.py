#
# Write the implementation for A2 in this file
#

# UI section
# (write all functions that have input or print statements here).
# Ideally, this section should not contain any calculations relevant to program functionalities
def print_menu():
    print("Complex Numbers App")
    print("Welcome!")


def ui_read_complex_number_list(d, a, b):
    d['a'].append(a)
    d['b'].append(b)


def ui_read_complex_number(d):
    while True:
        try:
            print("a = ")
            a = int(input())
            if a == 0:
                print("Back to the main menu...")
                return
            print("bi = ")
            b = int(input())
            if b == 0:
                print("Back to the main menu...")
                return
            ui_read_complex_number_list(d, a, b)
        except ValueError:
            print("Invalid input")


def ui_read_list_of_complex(d):
    print("Please input a valid complex number")
    print("Input the number representing the real part (a), press Enter")
    print("and input another number representing the imaginary part (bi)")
    ui_read_complex_number(d)


def ui_print_existing_complex_number_(d, x):
    if d['b'][x] < 0:
        nr = str(d['a'][x]) + str(d['b'][x]) + "i"
    else:
        nr = str(d['a'][x]) + "+" + str(d['b'][x]) + "i"
    print(nr)


def ui_print_complex_number(d):
    while True:
        try:
            x = int(input(">>>"))
            if x == -1:
                print("Back to the main menu...")
                return
            if x != -1:
                ui_print_existing_complex_number_(d, x)
        except IndexError:
            print("Invalid number position")


def ui_print_complex_list(d):
    maxi = str(len(d['a'])-1)
    print("choose number position: 0 to " + maxi)
    ui_print_complex_number(d)


def ui_print_list(d):
    for i in range(len(d["a"])):
        if d['b'][i] < 0:
            print("z" + str(i) + " = " + str(d['a'][i]) + str(d['b'][i]))
        else:
            print("z" + str(i) + " = " + str(d['a'][i]) + "+" + str(d['b'][i]))


def property_8(d):
    print("Property 8:The modulus of all elements ")
    print("is in the `[0, 10]` range.")
    k = len(d['a'])
    sec = int(0)
    max_sec = -1
    first = -1
    max_sec_first = -1
    for i in range(0, k):
        import math
        x = math.sqrt(d['a'][i]**2+d['b'][i]**2)
        if(x >= 0 and x <= 10):
            if sec == 0:
                first = i
            sec += 1
            if max_sec < sec:
                max_sec = sec
                max_sec_first = first
        else:
            sec = 0
    for j in range(max_sec_first, max_sec_first+max_sec):
        if d['b'][j] < 0:
            print("z" + str(j) + " = " + str(d['a'][j]) + str(d['b'][j]))
        else:
            print("z" + str(j) + " = " + str(d['a'][j]) + "+" + str(d['b'][j]))


def property_9(d):
    print("Property 9: Consecutive number ")
    print("pairs have equal sum.")
    l = []
    k = len(d['a'])
    for i in range(0, k):
        l.insert(i, d['a'][i]+d['b'][i])
    sec = int(0)
    max_sec = -1
    first = -1
    max_sec_first = -1
    for i in range(0, k-2, 2):
        if l[i] == l[i+2] and l[i+1] == l[i+3]:
            if sec == 0:
                first = i
            sec += 3
            if max_sec < sec:
                max_sec = sec
                max_sec_first = first
        else:
            sec = 0
    for j in range(max_sec_first, max_sec_first+max_sec+1):
        if d['b'][j] < 0:
            print("z" + str(j) + " = " + str(d['a'][j]) + str(d['b'][j]))
        else:
            print("z" + str(j) + " = " + str(d['a'][j]) + "+" + str(d['b'][j]))


def run():
    d = {
        "a": [2, 10, 3, 1, 3, 1, 3, 1, 5, 2],
        "b": [-1, 8, 5, 3, 5, 3, 5, 3, 6, 9]
    }
    print_menu()
    while True:
        print("You're currently in the main menu")
        cmd = input(">>>>>")
        if cmd == "1":
            ui_read_list_of_complex(d)
        elif cmd == "2":
            ui_print_complex_list(d)
        elif cmd == "3":
            ui_print_list(d)
        elif cmd == "8":
            property_8(d)
        elif cmd == "9":
            property_9(d)
        elif cmd == "4":
            print("Bye-bye")
            return
        else:
            print("Invalid command!")


# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values

# print('Hello A2'!) -> prints aren't allowed here!

def main():
    run()


main()
