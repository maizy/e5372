# _*_ coding: utf-8 _*_
from __future__ import unicode_literals, absolute_import

try:
    from lxml import etree
except ImportError:
    try:
        from xml.etree import cElementTree as etree
    except ImportError:
        from xml.etree import ElementTree as etree

__version__ = '0.1'
VERSION = __version__


class Error(Exception):
    pass


class FatalError(Error):
    pass
