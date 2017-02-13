# -*- coding: utf-8 -*-
import unittest
import os

from mkv import attacher


class AttacherTests(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.current_dir = os.getcwd()

    def test_should_check_utf_8_success(self):
        absolute_path = os.path.join(
                self.current_dir,
                'tests/resource_tests/utf.srt'
        )
        self.assertTrue(
                attacher.check_charset_utf(absolute_path)
        )


if __name__ == '__main__':
    unittest.main()
