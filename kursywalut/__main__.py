# -*- coding: utf-8 -*-

"""Main module."""

from .interface import interface

import six


def main():
    print(six.text_type('in main'))
    interface.run()


if __name__ == '__main__':
    main()
