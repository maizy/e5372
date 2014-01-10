# _*_ coding: utf-8 _*_

from collections import namedtuple


class XmlValue(namedtuple('_XmlValue', ['value', 'code'])):

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if not isinstance(other, XmlValue):
            return False
        return self.value == other.value


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
    XmlValue(value=1, code='2g_only'),
    XmlValue(value=2, code='3g_only'),
    XmlValue(value=3, code='4g_only'),
)
