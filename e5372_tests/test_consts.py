# _*_ coding: utf-8 _*_
from __future__ import unicode_literals, absolute_import

import unittest

from e5372 import consts


class XmlValueTestCase(unittest.TestCase):
    def test_hash(self):
        a = consts.XmlValue(33, 'code1')
        b = consts.XmlValue(33, 'code2')

        self.assertEqual(hash(a), hash(b))

        test_dict = {}
        test_dict[a] = 1
        test_dict[b] = 2
        self.assertEqual(test_dict[a], 2)
        self.assertEqual(test_dict[b], 2)

    def test_eq(self):
        a = consts.XmlValue(33, 'code1')
        b = consts.XmlValue(33, 'code2')

        self.assertTrue(a == b)


class TestGetFromEnum(unittest.TestCase):

    def test_by_code(self):
        self.assertEqual(consts.get_from_enum(consts.NETWORK_MODES, code='2g_only'), consts.NETWORK_MODES[1])

    def test_by_unknown_code(self):
        self.assertIsNone(consts.get_from_enum(consts.NETWORK_MODES, code='abcd'))

    def test_by_value(self):
        self.assertEqual(consts.get_from_enum(consts.NETWORK_MODES, value=2), consts.NETWORK_MODES[2])

    def test_by_unknown_value(self):
        self.assertIsNone(consts.get_from_enum(consts.NETWORK_MODES, value=''))
        self.assertIsNone(consts.get_from_enum(consts.NETWORK_MODES, value='2'))
        self.assertIsNone(consts.get_from_enum(consts.NETWORK_MODES, value=None))
