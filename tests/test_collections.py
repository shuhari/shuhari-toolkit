from unittest import TestCase

from shuhari_toolkit import collections


class CollectionsTest(TestCase):
    def test_find_first(self):
        items = range(10)
        self.assertEqual(4, collections.find_first(items, lambda x: x == 4))
        self.assertIsNone(collections.find_first(items, lambda x: x > 10))

    def test_find_first_by_key(self):
        items = [
            {'key': 11},
            {'key': 22}
        ]
        self.assertEqual({'key': 22}, collections.find_first_by_key(items, 'key', 22))
        self.assertIsNone(collections.find_first_by_key(items, 'key', -1))

    def test_find_first_by_attr(self):
        items = (1+4j, 2+8j)
        self.assertEqual(2+8j, collections.find_first_by_attr(items, 'real', 2))
        self.assertIsNone(collections.find_first_by_attr(items, 'real', -1))
