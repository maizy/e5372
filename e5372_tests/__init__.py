# _*_ coding: utf-8 _*_

from os import path

from e5372 import context

RESPONSES_PATH = path.join(path.dirname(__file__), 'responses')

def build_test_context():
    return context.Context({'router_host': '192.168.8.1'})
