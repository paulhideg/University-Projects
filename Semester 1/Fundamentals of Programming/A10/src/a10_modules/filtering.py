class Filter:
    def __init__(self, obj_list, key):
        self.__obj_list = obj_list
        self.__key = key

    @property
    def obj_list(self):
        return self.__obj_list

    @property
    def key(self):
        return self.__key

    def filter(self):
        self.obj_list[:] = self.__filter_object_list(self.obj_list)

    def __filter_object_list(self, obj_list):
        filtered_list = []
        for obj in obj_list:
            if self._keep_elem(obj):
                filtered_list.append(obj)
        return filtered_list

    def _keep_elem(self, obj):
        if self.key is None:
            return True
        return self.key(obj)


class Filtering(object):
    @staticmethod
    def filter(obj_list, key=None):
        Filter(obj_list, key).filter()
