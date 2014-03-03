# _*_ coding: utf-8 _*_
from os import path
import unittest

import pep8

from e5372_tests import PKG_ROOT, BIN_ROOT, SRC_ROOT

SOURCES = [PKG_ROOT, BIN_ROOT, path.join(SRC_ROOT, 'setup.py'),
           path.join(SRC_ROOT, 'e5372.cfg.ex')]


class StyleTestCase(unittest.TestCase):
    def test_pep8(self):
        pep8style = pep8.StyleGuide(
            show_pep8=False,
            show_source=True,
            repeat=True,
            max_line_length=119,
            statistics=True,
            )
        result = pep8style.check_files(SOURCES)
        if result.total_errors > 0:
            print('\nStatistics:')
            result.print_statistics()
            self.fail('PEP8 styles errors')
