# -*- coding: utf-8 -*-

"""Interface module."""


from kursywalut import version
from kursywalut.handlers import MoneyPlHandler

import six

def print_unicode(str):
    out = (six.text_type(str))
    print(out)

def get_moneypl():
    mpl = MoneyPlHandler()
    data = mpl.get_moneypl()
    print(data)

def display_header():
    print_unicode('##################')
    print_unicode('$ KursyWalut ' + version.__version__ + ' $')
    print_unicode('##################')
    get_moneypl()
