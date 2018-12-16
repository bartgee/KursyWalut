# -*- coding: utf-8 -*-
"""Interface module.

Simple CLI interface to run the program.
"""

from pprint import pprint

from kursywalut import version
from kursywalut.handlers import MoneyPlHandler
import six


class Config(object):
    """Class for main program sys args."""

    opts = None


def _to_unicode(value):
    """Converts value to unicode.

    :param value: (str)
    :return: (unicode)
    """
    return six.text_type(value)


def print_unicode(str):
    """Print unicode function."""
    out = (six.text_type(str))
    print(out)


def get_moneypl():
    """Get money.pl currency data.

    Returns string or unicode.

    :return: string or unicode
    """
    mpl = MoneyPlHandler()
    data = mpl.get_moneypl()
    return data


def pretty_print_data(data):
    """Format received data."""
    detail_str = ''
    for key, value in data.items():
        if key == 'FOREX':
            print_unicode(key + '\tkupno\tsprzedaż\n')
        elif key == 'NBP':
            print_unicode(key + '\tkurs średni\n')

        for name, detail in value.items():
            if type(detail) == list:
                for item in detail:
                    detail_str = detail_str + '\t' + item
            else:
                detail_str = detail
            if name == 'DATA':
                tab = '\t'
            else:
                tab = ''
            if key == 'FOREX':
                print_unicode(name + '{}'.format(tab) + detail_str)
            elif key == 'NBP':
                print_unicode(name + '\t' + detail_str)
            detail_str = ''
        print_unicode('')


def display_header():
    """Display header."""
    print_unicode('##################')
    print_unicode('$ KursyWalut ' + version.__version__ + ' $')
    print_unicode('##################\n')


def run(*args):
    """Run the program."""
    Config.opts = args
    display_header()
    data = get_moneypl()
    # pprint(data)
    print_unicode('')
    pretty_print_data(data)
