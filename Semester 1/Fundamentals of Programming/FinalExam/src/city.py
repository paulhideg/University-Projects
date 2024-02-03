import random

class City:
    def __init__(self):
        self.starved_people = 0
        self.new_people = 0
        self.population = 100
        self.land_acres = 1000
        self.harvest = 3
        self.rats = 200
        self.land_price = 20
        self.planted_acres = 0
        self.grain = 2800
        self.half_starved_population = False

    def set_starved_people(self, starved_people):
        self.starved_people = starved_people


    def print(self):
        print(str(self.starved_people) + " people starved")
        print(str(self.new_people) + " people came to the city")
        print("City population is " + str(self.population))
        print("City owns " + str(self.land_acres) + " acres of land")
        print("Harvest was " + str(self.harvest) + " units per acre")
        print("Rats ate " + str(self.rats) + " units")
        print("Land price is " + str(self.land_price) + " units per acre\n")
        print("Grain stocks are " + str(self.grain) + " units\n")

    #decisions
    def buy(self, acres):
        self.land_acres += acres
        self.grain -= acres * self.land_price

    def sell(self, acres):
        self.land_acres -= acres
        self.grain += acres * self.land_price

    def feed(self, units):
        self.grain -= units
        required_units = self.population * 20
        if units < required_units:
            missing_units = (required_units - units)
            if missing_units % 20 == 0:
                self.starved_people = missing_units / 20
            else:
                self.starved_people = (missing_units / 20) + 1
            if self.starved_people >= self.population / 2:
                self.half_starved_population = True
            self.population -= self.starved_people
        else:
            self.new_people = random.randint(0,10)
            self.population += self.new_people

    def plant(self, acres):
        self.planted_acres = acres
        self.grain -= acres
        
    #setters
    def set_land_price(self):
        self.land_price = random.randint(15, 25)

    def set_harvest(self):
        self.harvest = random.randint(1, 6)
    
    def set_rats(self):
        is_rats = random.randint(1, 100)
        if is_rats <= 20:
            if self.grain < 1:
                self.rats = 0
            self.rats = random.randint(0, 0.2 * self.grain)
            self.grain -= self.rats

    #calculate_grain
    def calculate_grain(self):
        max_harvest = self.population * 10
        if self.planted_acres > max_harvest:
            self.grain = self.harvest * max_harvest
        else:
            self.grain = self.harvest * self.planted_acres
        self.planted_acres = 0
