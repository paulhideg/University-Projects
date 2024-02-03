import unittest

from a10_modules.filtering import Filtering
from a10_modules.iterable_ds import IterableDS
from a10_modules.sorting import Sorting
from domain.entities.person import Person


class Tests(unittest.TestCase):
    def test_iterable(self):
        repo = IterableDS()
        repo.append(Person(1, 'n1', '123'))
        repo.append(Person(2, 'n2', '1234'))
        self.assertEqual(len(repo), 2)
        repo[0] = Person(1, 'n1', '123')
        repo[1] = Person(2, 'n2', '1234')
        self.assertEqual(repo[0], Person(1, 'n1', '123'))
        iter(repo)
        self.assertEqual(next(repo), Person(1, 'n1', '123'))
        self.assertEqual(next(repo), Person(2, 'n2', '1234'))
        self.assertRaises(StopIteration, next, repo)
        del repo[0]

    def test_sorting(self):
        number_list = [-1, 12, -9, 7, 2, 1, 3]
        Sorting.sort(number_list)
        self.assertListEqual(number_list, [-9, -1, 1, 2, 3, 7, 12])
        Sorting.sort(number_list, reverse=True)
        self.assertListEqual(number_list, [12, 7, 3, 2, 1, -1, -9])
        Sorting.sort(number_list)
        self.assertListEqual(number_list, number_list)
        p1, p2, p3, p4, p5 = Person(1, 'd', '567'), Person(7, 'c', '236'), Person(3, 'a', '445'), Person \
            (4, 'e', '112'), Person(2, 'c', '15')
        people_list = [p1, p2, p3, p4, p5]
        Sorting.sort(people_list, key=lambda x: x.person_id)
        self.assertListEqual(people_list, [p1, p5, p3, p4, p2])

        def person_less_than(x, y):
            # name descending,phone ascending
            if x.name.lower() == y.name.lower():
                return x.phone_number < y.phone_number
            return x.name.lower() > y.name.lower()

        people_list = [p1, p2, p3, p4, p5]
        Person.__lt__ = person_less_than
        Person.__gt__ = lambda x, y: not person_less_than(x, y)
        Sorting.sort(people_list)

        def true(x, y):
            return True

        people_list = [p1, p2, p3, p4, p5]
        Person.__lt__ = true
        Person.__gt__ = lambda x, y: not true(x, y)
        Sorting.sort(people_list)
        self.assertListEqual(people_list, [p1, p2, p3, p4, p5])
        p1, p2 = Person(1, 'name', '123'), Person(2, 'name', '123')
        ppl_list = [p1, p2]
        Sorting.sort(ppl_list, key=lambda x: x.name)

    def test_filtering(self):
        number_list = [-1, 12, -9, 7, 2, 1, 3]
        Filtering.filter(number_list)
        self.assertListEqual(number_list, [-1, 12, -9, 7, 2, 1, 3])

        def keep_number(x):
            return x >= 0

        Filtering.filter(number_list, key=keep_number)
        self.assertListEqual(number_list, [12, 7, 2, 1, 3])

        p1, p2, p3, p4, p5 = Person(1, 'Nume', '567'), Person(2, 'Prenumescu', '236'), Person(3, 'Bun', '445'), Person \
            (4, 'Alt bun', '112'), Person(5, 'nume bun de sters', '15')
        people_list = [p1, p2, p3, p4, p5]

        def keep_person(x):
            return 'nume' not in x.name.lower()

        Filtering.filter(people_list, key=keep_person)
        self.assertListEqual(people_list, [p3, p4])
