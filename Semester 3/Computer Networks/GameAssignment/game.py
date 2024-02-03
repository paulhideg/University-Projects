import time
import socket
import random
from threading import Thread


def handle_client(cs, i, list_game,correct):
    print("Handling  client [" + str(i) + "]")
    print("The list for the game is:\n")
    print(list_game)
    # for j in list_game:
    #     cs.send(f": {''.join(j)}".encode())
            
    current_guess = list()
    tries = 2

    rcv = cs.recv(1)
    clientChar = rcv.decode() #client guess
    try:
        guess = int(clientChar)
    except ValueError:
        print("Not a number")
    
    if(guess == 0):
        cs.send(f"Game started: {' '.join(list_game)}".encode())
        while True:
            found = 0
            rcv = cs.recv(1)
            clientChar = rcv.decode() #client guess
            print("Client "+str(i)+" input: " + clientChar)
            try: 
                guess = int(clientChar)
            except ValueError:
                print("Not a number")

            if (guess >= 0 and guess <=2):
                if guess == correct:
                    found = 1
                else: found = 0
            else: print("guess index not in list")


            if found == 0:
                tries -= 1
                print("Wrong guess")
            if tries <= 0:
                cs.send(f"You lost, the lie was: {''.join(list_game[correct])}".encode())
                print("Client " + str(i) + " lost")
                cs.close()
                break
            elif found == 1:
                cs.send(f"You won, the lie was: {''.join(list_game[correct])}".encode())
                print("Client " + str(i) + " won")
                cs.close()
                break
            else:
                cs.send(f"Wrong guess, you have tries left: {''.join(str(tries))}".encode())
    else:
        cs.send(f"Wrong input".encode())
        cs.close()
        print("Client " + str(i) + " wrong input")


list_truths = ["Has 3 girlfriends", "Never kissed a girl", "Has a phone", "Lives in Cluj", "Has a dog", "Eats out one a week"]
list_lies = ["No girlfriend", "Size 11 shoes", "Never been to Italy"]
list_game = []
random.shuffle(list_truths)
list_game.append(list_truths[0])
list_game.append((list_truths[1]))
list_game.append(list_lies[random.randint(0,2)])
random.shuffle(list_game)

correct = -1
for i in  range(2):
    if list_game[i] in list_lies:
        correct = i
        print(correct)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("172.30.112.112", 7777))
s.listen(5)
i = 0
while True:
    i = i + 1
    cs, address = s.accept()
    t = Thread(target=handle_client, args=(cs, i, list_game,correct))
    t.start()