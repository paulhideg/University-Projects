class Date:
    """
    Class that encapsulate a Date having a day, month and year
    """

    def __init__(self, day, month, year):
        """
        Initializes attributes
        :param day: natural number between 1 and 31
        :param month: natural number between 1 and 12
        :param year: natural number
        """
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        self.__month = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def __eq__(self, other):
        return self.__day == other.__day and self.__month == other.__month and self.__year == other.__year

    def __lt__(self, other):
        if self.__year < other.__year:
            return True
        elif self.__year == other.__year and self.__month < other.__month:
            return True
        elif self.__year == other.__year and self.__month == other.__month and self.__day < other.__day:
            return True
        return False

    def __str__(self):
        day, month, year = str(self.__day), str(self.__month), str(self.__year)
        if self.__day < 10:
            day = '0'
            day += str(self.__day)

        if self.__month < 10:
            month = '0'
            month += str(self.__month)
        return "{0}.{1}.{2}".format(day, month, year)
