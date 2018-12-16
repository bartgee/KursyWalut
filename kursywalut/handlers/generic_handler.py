# -*- coding: utf-8 -*-

"""GenericHandler Class"""

from lxml import html
import requests
# import re
import sys

class GenericHandler(object):

    def __init__(self, url):
        self.site_mapping = None
        self.page_list = None
        self.page = None
        self.url = url

    def get_webpage(self):
        for key, value in self.site_mapping.items():
            if value == self.url:
                site = key
        sys.stdout.write(u'Pobieram dane... ' + site + '\n') # instead of print() to print without a new line
        sys.stdout.flush()
        try:
            page = requests.get(self.url)
            sys.stdout.write('OK\n')
            sys.stdout.flush()
            self.page = page.content
        except requests.exceptions.RequestException:
            print(u'Błąd pobrania danych ze strony http://finanse.wp.pl/waluty.html!')
            sys.exit(1)
