# -*- coding: utf-8 -*-
"""KursyWalut."""

import sys


from kursywalut.interface import interface


def main():
    """Main function."""
    interface.run(sys.argv)


if __name__ == '__main__':
    main()
