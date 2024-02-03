from city import City

class Service():
    def __init__(self):
        pass
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

    def execute_decisions(self, acres, food, acres_planted):
        if acres > 0:
            self.city.buy(acres)
        else:
            self.city.sell(-acres)
        self.city.feed(food)
        self.city.plant(acres_planted)
