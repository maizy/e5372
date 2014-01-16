# _*_ coding: utf-8 _*_
from __future__ import unicode_literals, absolute_import

from huapi import api

if __name__ == '__main__':
    print(api.monitoring_status().report())
