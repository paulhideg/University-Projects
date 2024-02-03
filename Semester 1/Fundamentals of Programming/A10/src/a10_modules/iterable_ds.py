class IterableDS:
    def __init__(self):
        self._index = 0
        self.__elems = []

    @property
    def elems(self):
        return self.__elems[:]

    def append(self, value):
        self.__elems.append(value)

    def __setitem__(self, key, value):
        self.__elems[key] = value

    def __getitem__(self, key):
        return self.__elems[key]

    def __delitem__(self, key):
        del self.__elems[key]

    def __next__(self):
        if self._index < len(self.__elems):
            result = self.__elems[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        self._index = 0
        return self
    def __len__(self):
        return len(self.__elems)
