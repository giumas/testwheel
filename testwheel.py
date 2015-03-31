from __future__ import absolute_import, division, print_function

__version__ = '0.0.1-dev'
__author__ = 'giumas'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 giumas'


class _Base(object):
    def __init__(self, _name_str):
        self.name_str = _name_str

    def __str__(self):
        return self.name_str

    def __repr__(self):
        return '<%r(str={%r})>' % (self.__class__.__name__, self.name_str )