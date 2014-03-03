# _*_ coding: utf-8 _*_

from os import path

from e5372 import context

SRC_ROOT = path.abspath(path.join(path.dirname(__file__), '..'))
PKG_ROOT = path.join(SRC_ROOT, 'e5372')
BIN_ROOT = path.join(SRC_ROOT, 'bin')
RESPONSES_PATH = path.join(path.dirname(__file__), 'responses')


def build_test_context():
    return context.Context({'router_host': '192.168.8.1'})
