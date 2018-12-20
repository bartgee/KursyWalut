# -*- coding: utf-8 -*-
"""Interface module.

Simple CLI interface to run the program.

"""

import logging

import six

from .. import version
from ..handlers import MoneyPlHandler


logger = logging.getLogger(__name__)


class Config(object):
    """Class for program configuration data.

    Attributes:
        opts: sys.args passed while running the program

    """

    opts = None


def _to_unicode(value):
    """Convert value to unicode.

    Args:
        value (str): Value to be converted to unicode.

    Returns:
        string (Python 3) or unicode (Python 2).

    """
    return six.text_type(value)


def print_unicode(str):
    """Print unicode function.

    Prints string (Python 3) or string converted to unicode (Python 2).

    """
    out = (six.text_type(str))
    print(out)


def get_moneypl():
    """Get money.pl currency data.

    Returns:
        OrderedDict: Parsed data.

    """
    print_unicode('Getting data from website.')
    # start = now()
    mpl = MoneyPlHandler()
    data = mpl.get_moneypl()
    # end = elapsed_time(start, now())
    # logger.debug(end)
    print_unicode('data download time: {}'.format(mpl.download_time))
    print_unicode('parse time: {}'.format(mpl.parse_time))
    return data


def pretty_print_data(data):
    """Format received data.

    Args:
        data (ordereddict): OrderedDict to be printed.

    """
    detail_str = ''
    for key, value in data.items():
        if key == 'FOREX':
            print_unicode(key + u'\tkupno\tsprzedaż\n')
        elif key == 'NBP':
            print_unicode(key + u'\tkurs średni\n')

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
                print_unicode(name + u'{}'.format(tab) + detail_str)
            elif key == 'NBP':
                print_unicode(name + u'\t' + detail_str)
            detail_str = ''
        print_unicode('')


def display_header():
    """Display header."""
    print_unicode(u'##################')
    print_unicode(u'$ KursyWalut ' + version.__version__ + u' $')
    print_unicode(u'##################\n')


def run(*args):
    """Run the program."""
    Config.opts = args
    display_header()
    data = get_moneypl()
    # pprint(data)
    print_unicode('')
    pretty_print_data(data)
