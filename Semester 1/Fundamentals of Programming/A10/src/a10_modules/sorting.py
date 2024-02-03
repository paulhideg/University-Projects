class GnomeSort:
    def __init__(self, obj_list, key, reverse):
        self.__obj_list = obj_list
        self.__key = key
        self.__reverse = reverse

    @property
    def obj_list(self):
        return self.__obj_list

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def reverse(self):
        return self.__reverse

    def sort(self):
        self.obj_list[:] = self.__gnome_sort(self.obj_list)

    def __gnome_sort(self, sorted_list):
        index = 0
        while index < len(sorted_list):
            if index == 0:
                index += 1
            if 0 < index < len(sorted_list):
                if self._in_order(sorted_list[index - 1], sorted_list[index]):
                    index += 1
                else:
                    sorted_list[index], sorted_list[index - 1] = sorted_list[index - 1], sorted_list[index]
                    index -= 1
        return sorted_list

    def _in_order(self, e1, e2, eq=True):
        if self.key is None:
            self.key = lambda x: x
        if self.key(e1) == self.key(e2):
            return eq
        if not self.reverse:
            return self.key(e1) < self.key(e2)
        return self.key(e1) > self.key(e2)


class Sorting(object):
    @staticmethod
    def sort(obj_list, key=None, reverse=False):
        GnomeSort(obj_list, key, reverse).sort()
