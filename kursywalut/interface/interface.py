# -*- coding: utf-8 -*-

"""Interface module."""

from pprint import pprint

from kursywalut import version
from kursywalut.handlers import MoneyPlHandler

import six


def _to_unicode(value):
    """
    Converts value to unicode.
    :param value: (str)
    :return: (unicode)
    """
    return six.text_type(value)

def print_unicode(str):
    out = (six.text_type(str))
    print(out)

def get_moneypl():
    mpl = MoneyPlHandler()
    data = mpl.get_moneypl()
    # data = _to_unicode(data)
    return data

def format_data(data):
    for key, value in data.items():
        print(key)
        for name, detail in value.items():
            print(name + ' ' + str(detail))

def display_header():
    print(u'##################')
    print_unicode(u'$ KursyWalut ' + version.__version__ + u' $')
    print_unicode(u'##################')
    data = get_moneypl()
    pprint(data)
    format_data(data)

display_header()
