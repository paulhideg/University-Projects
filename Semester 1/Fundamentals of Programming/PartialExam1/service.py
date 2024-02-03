from repo import Repo
from entities import Player
import random

class Service:
    def __init__(self, repo):
        repo = repo
        self.players = repo.players

    def open_file(self, players_file):
        with open(players_file, 'r') as file:
            for line in file:
                id, name, strength = line.strip().split(',')
                self.players.append(Player(id, name, int(strength)))
        self.players.sort(key=lambda x: x.strength, reverse=True)

    def print_players(self):
        for player in self.players:
            print(player)

    def play_qualifying_round(self):
        num_players = len(self.players)
        if num_players & (num_players - 1) == 0:
            return
        num_to_eliminate = 2 ** (num_players.bit_length() - 1) - num_players
        qualifying_players = self.players[-num_to_eliminate:]
        random.shuffle(qualifying_players)
        for i in range(num_to_eliminate-1, 0, 2):
            print(f"Qualifying round: {qualifying_players[i]} vs {qualifying_players[i-1]}")
            winner = int(input("Enter which player won (1 or 2): "))
            if winner == 1:
                self.players.remove(qualifying_players[i])
            else:
                self.players.remove(qualifying_players[i-1])

    def round_winner(self, players, winner, i):
        if winner == 1:
            players[i].strength += 1
            players.remove(players[i-1])
        else:
            players[i-1].strength += 1
            players.remove(players[i])

    #determines the number of players that will play the qualifying round
    def qualifying_players_number(self):
        num_players = len(self.players)
        check = 1
        if num_players & (num_players - 1) == 0:
            return 0
        while check < num_players:
            check *= 2
        if check == num_players:
            return 0
        else:   
            check /= 2
        num_to_eliminate = num_players - check
        return num_to_eliminate