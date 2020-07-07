import os
from unittest import TestCase

from shuhari_toolkit import fileutils
from .fixtures import ensure_var_folder, get_var_path


class FileUtilsTest(TestCase):
    def test_relative_of(self):
        full_path = fileutils.relative_of(__file__, 'test_fileutils.py')
        self.assertTrue(os.path.isabs(full_path))
        self.assertTrue(os.path.exists(full_path))

    def test_read_file_text(self):
        content = fileutils.read_file_text(__file__)
        self.assertIn(self.__class__.__name__, content)

    def test_write_file_bytes(self):
        file_path = get_var_path('test.bin')
        fileutils.write_file_bytes(file_path, b'')
        self.assertTrue(os.path.exists(file_path))
        os.unlink(file_path)

    def test_read_write_file_json(self):
        file_path = get_var_path('test.json')
        written = {'key': 'value'}
        fileutils.write_file_json(file_path, written)
        readed = fileutils.read_file_json(file_path)
        self.assertEqual(readed, written)
        os.unlink(file_path)

    def test_purge_folder(self):
        var_folder = ensure_var_folder()
        fileutils.write_file_bytes(get_var_path('file1'), b'')
        os.makedirs(get_var_path('dir1'), exist_ok=True)
        fileutils.purge_folder(var_folder)
        self.assertEqual(0, len(os.listdir(var_folder)))
