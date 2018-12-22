# -*- coding: utf-8 -*-

"""Tests for string operations package."""

import six

from kursywalut.funcs import string_operations


def test_unicode(string=u'zażółć gęślą jaźń', expected=six.text_type(u'zażółć gęślą jaźń')):
    """Test _to_unicode()."""

    out = string_operations._to_unicode(string)

    assert out == expected
