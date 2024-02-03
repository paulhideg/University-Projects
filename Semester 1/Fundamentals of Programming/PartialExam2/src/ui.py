from functions import *

def add_menu(flights):
    """Adds a flight to the list of flights"""
    print("\nAdd:")
    print("Code:")
    flight_code = input()
    print("Duration:")
    flight_duration = input()
    print("Departure:")
    flight_departure = input()
    print("Destination:")
    flight_destination = input()
    if(add_flight(flight_code, flight_duration, flight_departure,flight_destination)):
        print("Flight added!")
    else:
        print("Invalid input!")
    
def delete_menu(flights):
    print("\nDelete:\n")
    print("Code:")
    flight_code = input()
    if(delete_flight(flights, flight_code)):
        print("Flight deleted!")
    else:
        print("Flight not found!")
    
def show_all_menu(flights):
    print("\nShow All:\n")
    if (len(flights)) == 0:
        print("No flights found!")
    else:
        for i in range(len(flights)):
            print(flights[i])

def show_by_departure_menu(flights):
    print("\nShow By Departure:\n")
    print("Departure:")
    departure = input()
    found = False
    sort_flights(flights)
    for i in range(len(flights)):
        if flights[i][2] == departure:
            print(flights[i])
            found = True
    if found == False:
        print("No flights found!")

def strong_winds_menu(flights):
    print("\nStrong Winds:\n")
    print("Departure:")
    departure = input()
    print("Minutes (10-60):")
    minutes = input()
    if(validate_departure_minutes(flights, departure, minutes)):
        strong_winds(flights, departure, int(minutes))
        print("Flight duration(s) updated!")
    else:
        print("Invalid input!")

def main_menu_print():
    print("\nWelcome to the main menu")
    print("Use the following commands to navigate through the menus:")
    print("1 - Add")
    print("2 - Delete")
    print("3 - Show All")
    print("4 - Show By Departure")
    print("5 - Strong Winds")

def main_menu():
    flights = [[123, 110, "Bucharest", "London"], [124, 120, "Cluj-Napoca", "Paris"], 
                [125, 115, "New York", "Madrid"], [126, 130, "Cluj-Napoca", "Berlin"], 
                [127, 125, "Bucharest", "Rome"]]
    main_menu_print()
    while True:
        command = input("Command: ")
        if command == "1":
            add_menu(flights)
        elif command == "2":
            delete_menu(flights)
        elif command == "3":
            show_all_menu(flights)
        elif command == "4":
            show_by_departure_menu(flights)
        elif command == "5":
            strong_winds_menu(flights)
        else:
            print("Invalid command!")

main_menu()
