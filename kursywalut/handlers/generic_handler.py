# -*- coding: utf-8 -*-

"""GenericHandler Class."""

import sys

import six
import requests


class GenericHandler(object):
    """GenericHandler class."""

    def __init__(self, url):
        """Initialization method."""
        self.site_mapping = None
        self.page_list = None
        self.page = None
        self.url = url

    def get_webpage(self):
        """get_webpage method.

        Send the request from self.site_mapping list.
        """
        for key, value in self.site_mapping.items():
            if value == self.url:
                site = self._to_unicode(key)
        sys.stdout.write(
            u'Pobieram dane... ' + site + '\n')  # instead of print() to print without a new line
        sys.stdout.flush()
        try:
            page = requests.get(self.url)
            sys.stdout.write(u'OK\n')
            sys.stdout.flush()
            self.page = page.content
        except requests.exceptions.RequestException:
            print(
                u'Błąd pobrania danych ze strony http://finanse.wp.pl/waluty.html!')
            sys.exit(1)

    def _to_unicode(self, value):
        """Converts value to unicode.

        :param value: (str)
        :return: (unicode)
        """
        return six.text_type(value)
