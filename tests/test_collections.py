from unittest import TestCase

from shuhari_toolkit import collections


class CollectionsTest(TestCase):
    def test_find_first(self):
        collection = range(10)
        self.assertEqual(4, collections.find_first(collection, lambda x: x == 4))
        self.assertIsNone(collections.find_first(collection, lambda x: x > 10))
