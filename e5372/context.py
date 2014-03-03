# _*_ coding: utf-8 _*_
from __future__ import unicode_literals, absolute_import

import os
from os import path

from e5372 import VERSION, FatalError

_default_context = {'c': None}

_path_priorities = (
    'e5372.cfg',
    '~/.config/e5372/e5372.cfg',
    '/etc/e5372/e5372.cfg',
)

_env_key = 'E5372_CONFIG'


class Context(object):

    def __init__(self, config):
        self.config = config
        self.user_agent = self.config.get('user_agent', 'e5372/{}').format(VERSION)
        self.router_host = self.config['router_host']


def from_config_file(file_path=None):
    if file_path is None:
        file_path = os.environ.get(_env_key)
        if file_path is not None and not path.isfile(file_path):
            raise FatalError('Config file not exists: {}'.format(file_path))
    if file_path is None:
        for p in map(path.expanduser, _path_priorities):
            if path.isfile(p):
                file_path = p
                break
    if file_path is None:
        raise FatalError('Unable to find config file. Create one in {} or define path in {} env variable'
                         .format(','.join(_path_priorities), _env_key))
    config = {}
    execfile(file_path, {}, config)
    return Context(config)


def get_default_context():
    if _default_context['c'] is None:
        set_default_context(from_config_file())
    return _default_context['c']


def set_default_context(context):
    _default_context['c'] = context
