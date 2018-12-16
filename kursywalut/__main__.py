# -*- coding: utf-8 -*-

"""Main module."""

import six

from .interface import interface


def main():
    """MAIN.

    :return:
    """
    print(six.text_type('in main'))
    interface.run()


if __name__ == '__main__':
    main()
