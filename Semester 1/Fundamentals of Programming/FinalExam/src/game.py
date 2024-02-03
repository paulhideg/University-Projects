class Game:
    def __init__(self, city):
        self.city = city
        self.year = 1

    def play(self):
        while self.checkYear() == True:
            self.print_year()
            if self.check_loss() == False:
                return
            #check if game is over
            self.decisions()
            self.city.set_land_price()
            self.city.set_harvest()
            self.city.calculate_grain()
            self.city.set_rats()
            self.year += 1
        else:
            self.print_year()
            self.check_win()

    def checkYear(self):
        """
        Checks if we reached year 5
        """
        if self.year < 5:
            return True
        return False

    def test_checkYear(self):
        """
        Tests checkYear()
        """
        self.year = 1
        assert self.checkYear() == True
        self.year = 5
        assert self.checkYear() == False

    def print_year(self):
        print("\nYear " + str(self.year) + "\n")
        self.city.print()

    def decisions(self):
        acres = 0
        food = 0
        acres_planted = 0
        temp_grain = self.city.grain
        print("How many acres do you want to buy/sell ?")
        valid1 = False
        while valid1 == False:
            try:
                acres = int(input())
                if acres < 0:
                    acres = -acres
                    if self.city.land_acres < acres:
                        print("You don't have enough acres to sell")
                    else:
                        #self.city.sell(acres)
                        acres = -acres
                        valid1 = True
                else: # acres > 0
                    if acres * self.city.land_price > self.city.grain:
                        print("You don't have enough grain to but this many acres")
                    else:
                        #self.city.buy(acres)
                        temp_grain -= acres * self.city.land_price
                        valid1 = True
            except ValueError:
                print("Please enter a number")
        
        print("\nHow many units of grain do you want to feed the population ?")
        valid2 = False
        while valid2 == False:
            try:
                units = int(input())
                if units > temp_grain:
                    print("You don't have enough grain to feed the population")
                else:
                    #self.city.feed(units)
                    food = units
                    temp_grain -= units
                    valid2 = True
            except ValueError:
                print("Please enter a number")
        
        print("\nHow many acres do you want to plant ?")
        valid3 = False
        while valid3 == False:
            try:
                acres_planted = int(input())
                if acres_planted > self.city.land_acres:
                    print("You don't have enough land to plant this many acres")
                elif acres_planted > temp_grain:
                    print("You don't have enough grain to plant this many acres")
                else:
                    #self.city.plant(acres_planted)
                    valid3 = True
            except ValueError:
                print("Please enter a number")

        self.execute_decisions(acres, food, acres_planted)

    def execute_decisions(self, acres, food, acres_planted):
        if acres > 0:
            self.city.buy(acres)
        else:
            self.city.sell(-acres)
        self.city.feed(food)
        self.city.plant(acres_planted)
    
    def check_loss(self):
        if (self.city.half_starved_population == True):
            print("Game Over...")
            print("You lost because half of your population starved")
            return False
        return True
    
    def check_win(self):
        if (self.city.population > 100) and (self.city.land_acres > 1000):
            print("You won!")
        else :
            print("Game Over. You did not do well.")