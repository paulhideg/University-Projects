from service import Service
import random

class UI:
    def __init__(self, service):
        self.service = service

    def run(self):
        self.service.open_file("players.txt")
        print("All players:")
        self.service.print_players()
        self.service.play_qualifying_round()
        self.play_tournament()
        print(f"Tournament winner: {self.service.players[0]}")

    def play_qualifying_round(self):
        num_players = len(self.players)
        if num_players & (num_players - 1) == 0:
            return
        num_to_eliminate = 2 ** (num_players.bit_length() - 1) - num_players
        qualifying_players = self.players[-num_to_eliminate:]
        random.shuffle(qualifying_players)
        for i in range(num_to_eliminate-1, 0, 2):
            """
            we start from the last 2 elements, 
            beacause each time we remove an element, 
            the list gets shorter
            """
            self.play_round(i)

    def play_tournament(self):
        num_players = len(self.service.players)
        round_count = num_players.bit_length() - 1
        while num_players > 1:
            if (round_count == 1):
                print("\nFinal round:")
            if (round_count == 2):
                print("\nSemi-final round:")
            if (round_count == 3):
                print("\nQuarter-final round:")
            if (round_count > 3):
                print(f"\nRound {round_count}:")
            random.shuffle(self.service.players)
            for i in range(num_players-1, 0, -2):
                """
                we start from the last 2 elements, 
                beacause each time we remove an element, 
                the list gets shorter
                """
                self.play_round(i)
            num_players = len(self.service.players)
            round_count -= 1

    def play_round(self, i):
        print(f"{self.service.players[i]} vs {self.service.players[i-1]}")
        winner = int(input("Enter which player won (1 or 2): "))
        self.service.round_winner(self.service.players, winner, i)

