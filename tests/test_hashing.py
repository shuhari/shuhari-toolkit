from unittest import TestCase

from shuhari_toolkit import hashing, fileutils


class HashingTest(TestCase):
    def test_get_file_sha1(self):
        file_path = fileutils.relative_of(__file__, '__init__.py')
        sha1 = hashing.get_file_sha1(file_path)
        # result verified use sha1sum __init__.py
        self.assertEqual('da39a3ee5e6b4b0d3255bfef95601890afd80709', sha1)
