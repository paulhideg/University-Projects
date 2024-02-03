class Time:
    """
    Class that encapsulate time, having a starting hour and minute and ending hour and minute
    """

    def __init__(self, start_h, start_m, end_h, end_m):
        """
        Initializes attributes
        :param start_h: int between 0 and 23
        :param start_m: int between 0 and 59
        :param end_h: int between 0 and 23
        :param end_m: int between 0 and 59
        """
        self.__start_h = start_h
        self.__start_m = start_m
        self.__end_h = end_h
        self.__end_m = end_m

    @property
    def start_h(self):
        return self.__start_h

    @start_h.setter
    def start_h(self, value):
        self.__start_h = value

    @property
    def start_m(self):
        return self.__start_m

    @start_m.setter
    def start_m(self, value):
        self.__start_m = value

    @property
    def end_h(self):
        return self.__end_h

    @end_h.setter
    def end_h(self, value):
        self.__end_h = value

    @property
    def end_m(self):
        return self.__end_m

    @end_m.setter
    def end_m(self, value):
        self.__end_m = value

    def __eq__(self, other):
        """
        Overrides = operator, because 2 times are equal if their attributes are equal
        :param other: time object
        :return: True if times are equal else False
        """
        return (self.__start_h == other.__start_h) and (self.__end_h == other.__end_h) and \
               (self.__start_m == other.__start_m) and (self.__end_m == other.__end_m)

    def __lt__(self, other):
        if self.__end_h < other.__start_h or (self.__end_h == other.__start_h and self.end_m < other.start_m):
            return True
        return False

    def __gt__(self, other):
        if self.__start_h > other.__end_h or (self.__start_h == other.__end_h and self.__start_m > other.end_m):
            return True
        return False

    def __str__(self):
        """
        Formats a string to display time like hh:mm - hh:mm
        :return: formatted string
        """
        hs, he, ms, me = str(self.__start_h), str(self.__end_h), str(self.__start_m), str(self.__end_m)
        if self.__start_h == 0:
            hs = '00'
        elif self.__start_h < 10:
            hs = '0'
            hs += str(self.__start_h)
        if self.__end_h == 0:
            he = '00'
        elif self.__end_h < 10:
            he = '0'
            he += str(self.__end_h)
        if self.__start_m == 0:
            ms = '00'
        elif self.__start_m < 10:
            ms = '0'
            ms += str(self.__start_m)
        if self.__end_m == 0:
            me = '00'
        elif self.__end_m < 10:
            me = '0'
            me += str(self.__end_m)

        return "{0}:{1} - {2}:{3}".format(hs, ms, he, me)
