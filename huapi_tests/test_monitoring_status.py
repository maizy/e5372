# _*_ coding: utf-8 _*_
from __future__ import unicode_literals, absolute_import

import unittest
from os import path

from requests import Response

from huapi import api, consts
from huapi_tests import RESPONSES_PATH


class MonitoringStatusTest(unittest.TestCase):

    def setUp(self):
        self.get_before = api.get_request

        def mock(*_, **__):  # FIXME use some special requests mock lib
            resp = Response()
            resp._content = open(path.join(RESPONSES_PATH, 'monitoring_status-4g_auto.xml')).read()
            return resp

        api.get_request = mock

    def tearDown(self):
        api.get_request = self.get_before

    def test_parsing(self):
        res = api.monitoring_status()
        self.assertIsNotNone(res)
        self.assertEqual(type(res), api.NetworkStatus)
        self.assertEqual(res.network_type, consts.get_from_enum(consts.NETWORK_TYPES, code='LTE'))
        self.assertEqual(res.battery_percent, 70)
        self.assertEqual(res.primary_dns, '10.10.10.1')
        self.assertEqual(res.secondary_dns, '10.10.10.2')
        self.assertEqual(res.wifi_users_amount, 1)
        self.assertEqual(res.wan_ip, '172.19.1.20')
