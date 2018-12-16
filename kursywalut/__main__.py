# -*- coding: utf-8 -*-
"""KursyWalut."""

import six

from .interface import interface


def main():
    """Main function."""
    print(six.text_type('in main'))
    interface.run()


if __name__ == '__main__':
    main()
