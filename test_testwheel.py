from __future__ import (absolute_import, division, print_function)

import pytest
import testwheel


class TestBase(object):
    def test_zero(self):
        """ Testing author name string. """
        assert "giumas" == testwheel.__author__
