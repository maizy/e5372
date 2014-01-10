# _*_ coding: utf-8 _*_
import unittest

from huapi import consts


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
