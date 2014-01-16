# _*_ coding: utf-8 _*_
from __future__ import unicode_literals, absolute_import

from collections import namedtuple


class XmlValue(namedtuple('_XmlValue', ['value', 'code'])):

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if not isinstance(other, XmlValue):
            return False
        return self.value == other.value

    @classmethod
    def from_xml(cls, xml, enum, type_=str):
        value = type_(xml.text)
        for item in enum:
            if item.value == value:
                return item
        return None

    def __unicode__(self):
        return '{s.value} ({s.code})'.format(s=self)

    def __str__(self):
        return unicode(self).encode('utf-8')


# also see /js/main.js: MACRO_NET_WORK_TYPE_*
NETWORK_TYPES = (
    XmlValue(value=3, code='EDGE'),
    XmlValue(value=9, code='HSPA+'),
    XmlValue(value=19, code='LTE'),
)

# also see /js/mobilenetworksettings.js: g_arrNetworkBand
NETWORK_BANDS = (
    XmlValue(value=0x3FFFFFFF, code='any'),
)

# also see
#  * /js/mobilenetworksettings.js: g_networknodes, NETWORKMODES, g_setting_netWorkModeList
#  * /api/net/net-mode-list
NETWORK_MODES = (
    XmlValue(value=0, code='auto'),
    XmlValue(value=1, code='2g_only'),
    XmlValue(value=2, code='3g_only'),
    XmlValue(value=3, code='4g_only'),
)

URL_MONITORING_STATUS = b'/monitoring/status'


def get_from_enum(enum, value=None, code=None):
    if all((code is not None, value is not None)):
        raise TypeError("Can't use value and code at one time")
    for item in enum:
        if value is not None and item.value == value:
            return item
        if code is not None and item.code == code:
            return item
    return None
