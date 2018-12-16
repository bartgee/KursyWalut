# -*- coding: utf-8 -*-

"""MoneyPlHandler Class"""

from .generic_handler import GenericHandler
from kursywalut.parsers.moneypl_parser import MoneyPlParser

class MoneyPlHandler(GenericHandler):
    """
    bla
    """
    def __init__(self):
        super(MoneyPlHandler, self).__init__(None)
        self.site_mapping = {
            'FOREX': 'https://www.money.pl/pieniadze/forex/',
            'NBP': 'https://www.money.pl/pieniadze/nbp/srednie/',
        }
        self.url_forex = self.site_mapping['FOREX']
        self.url_nbp = self.site_mapping['NBP']
        self.page_list = []


    def _get_forex(self):
        self.url = self.url_forex
        self.get_webpage()
        self.page_list.append(self.page)
        self.parser = MoneyPlParser(self, self.site_mapping)
        self.data_parsed = self.parser.parse()

    def _get_nbp(self):
        self.url = self.url_nbp
        self.get_webpage()
        self.page_list.append(self.page)

    def get_moneypl(self):
        self.page_list = []
        self._get_forex()
        self._get_nbp()

        return self.data_parsed
