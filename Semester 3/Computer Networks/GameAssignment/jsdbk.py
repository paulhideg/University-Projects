import random

def play_menu():
    print("There will be one Lie and 2 Truth statements .\nYou need to choose which is the lie by writing the number of the statement")
    list_truths = ["Has 3 girlfriends", "Never kissed a girl", "Has a phone", "Lives in Cluj", "Has a dog", "Eats out one a week"]
    list_lies = ["No girlfriend", "Size 11 shoes", "Never been to Italy"]
    list_game = []
    random.shuffle(list_truths)
    list_game.append(list_truths[0])
    list_game.append((list_truths[1]))
    list_game.append(list_lies[random.randint(0,2)])
    print("The list for the game is:\n")
    random.shuffle(list_game)
    print(list_game)
    print("\n")
    option = int(input("Now you need to choose which of the sentences is wrong by writing the number of the sentence:\n"))
    if option >= 0 and option <= 2:
        for i in list_lies:
            if list_game[0] == i:
                print("You choose the corect answer!!\n")
                break
            else:
                print("You choose the wrong answer:(\n")
                break
    else:
        print("Input is invalid, try again!")
        print("\n")



def print_menu():
    print("----------------2Truth1Lie-------------------------")
    print("1) Press 1 to Play")
    print("2) Press 2 to Exit")

def start():
        while True:
            print_menu()
            option = int(input("Choose a number: "))
            print("\n")

            if option == 1:
                play_menu()

            elif option == 2:
                exit()
            else:
                print("Input is invalid, try again!")
                print("\n")


start()