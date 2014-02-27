# _*_ coding: utf-8 _*_
from __future__ import unicode_literals, absolute_import

from collections import namedtuple
from functools import partial

import requests

from e5372.context import get_default_context
from e5372 import consts, etree, Error

get_request = requests.get

# TODO: break to some modules
# TODO: Error subclasses
# TODO: requests mocks for tests


def _get_requests_args(context):
    return {
        'headers': {'user-agent': context.user_agent}
    }


class _Rule(object):
    def __init__(self, field, xml_field, convert_func=None):
        self.field = field
        self.xml_field = xml_field
        self.convert = convert_func if convert_func is not None else (lambda x: str(x.text))


class _NamedtupleWithDefaultsMixin(object):
    def __new__(cls, *args, **kwargs):
        namedtuple_kwargs = {key: kwargs.get(key) for key in cls._fields}
        return super(_NamedtupleWithDefaultsMixin, cls).__new__(cls, *args, **namedtuple_kwargs)


class NetworkStatus(_NamedtupleWithDefaultsMixin,
                    namedtuple('_Status', ['network_type', 'battery_percent', 'wan_ip', 'primary_dns',
                                           'secondary_dns', 'wifi_users_amount'])):

    def report(self):
        fields = '\n'.join('{}: {}'.format(x, str(getattr(self, x))) if getattr(self, x) is not None else '--'
                           for x in type(self)._fields)
        return 'Network status: \n{}'.format(fields)

_to_int = lambda x: int(x.text)

_MONITORING_STATUS_RULES = (
    _Rule('network_type', 'CurrentNetworkType', partial(consts.XmlValue.from_xml, enum=consts.NETWORK_TYPES,
                                                        type_=int)),
    _Rule('battery_percent', 'BatteryPercent', _to_int),
    _Rule('wan_ip', 'WanIPAddress'),
    _Rule('primary_dns', 'PrimaryDns'),
    _Rule('secondary_dns', 'SecondaryDns'),
    _Rule('wifi_users_amount', 'CurrentWifiUser', _to_int),
)


def monitoring_status(context=None):
    """
    :rtype NetworkType
    """
    context = context if context is not None else get_default_context()
    args = _get_requests_args(context)
    response = get_request('http://{}/api{}'.format(context.router_host, consts.URL_MONITORING_STATUS), **args)
    xml = _get_response_xml(response)
    if xml is not None:
        return NetworkStatus(**_parse_simple_xml(xml, rules=_MONITORING_STATUS_RULES))
    raise Error('unable to get monitoring status')  # todo


def _get_response_xml(response):
    if response is None:
        return None
    content = response.content
    if not content:
        return None
    try:
        return etree.fromstring(content)
    except etree.ParseError:
        return None


def _parse_simple_xml(xml, rules):
    res = {}
    for rule in rules:
        xml_value = xml.find(rule.xml_field)
        if xml_value is not None:
            res[rule.field] = rule.convert(xml_value)
    return res
