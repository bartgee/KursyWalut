# -*- coding: utf-8 -*-

"""Main module."""

# from kursywalut.handlers import MoneyPlHandler
from lxml import html

class MoneyPlParser(object):

    def __init__(self, moneypl_handler):
        self.moneypl_handler = moneypl_handler
        self.currency = {}

    def _get_text(self):
        if self.moneypl_handler.page_list is not None:
            return self.moneypl_handler.page_list
        else:
            return self.moneypl_handler.page

    def parse(self):
        page_raw = self._get_text()
        if type(page_raw) == list:
            page = page_raw[0] # TODO: na razie tylko pierwszy element listy
        else:
            page = page_raw
        tree = html.fromstring(page)
        post_date = tree.xpath('//span[@class="xqiouj-5 kFhDeu"]/text()')[0]
        # eur_pln = tree.xpath('//div[@class="xje3ps-2 fqrPPi"]/text()')

        eur_pln_buy = tree.xpath('//*[@id="app"]/div/div[7]/div/div[2]/div/main/div/section[1]/div[2]/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div')[0].text_content()
        eur_pln_sell = tree.xpath('//*[@id="app"]/div/div[7]/div/div[2]/div/main/div/section[1]/div[2]/div/div/div/div[1]/div[2]/div[4]/div/div[3]/div')[0].text_content()

        chf_pln_buy = tree.xpath('//*[@id="app"]/div/div[7]/div/div[2]/div/main/div/section[1]/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div[2]/div')[0].text_content()
        chf_pln_sell = tree.xpath('//*[@id="app"]/div/div[7]/div/div[2]/div/main/div/section[1]/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div[3]/div')[0].text_content()

        gbp_pln_buy = tree.xpath('//*[@id="app"]/div/div[7]/div/div[2]/div/main/div/section[1]/div[2]/div/div/div/div[1]/div[2]/div[5]/div/div[2]/div')[0].text_content()
        gbp_pln_sell = tree.xpath('//*[@id="app"]/div/div[7]/div/div[2]/div/main/div/section[1]/div[2]/div/div/div/div[1]/div[2]/div[4]/div/div[3]/div')[0].text_content()

        usd_pln_buy = tree.xpath('//*[@id="app"]/div/div[7]/div/div[2]/div/main/div/section[1]/div[2]/div/div/div/div[1]/div[2]/div[6]/div/div[2]/div')[0].text_content()
        usd_pln_sell = tree.xpath('//*[@id="app"]/div/div[7]/div/div[2]/div/main/div/section[1]/div[2]/div/div/div/div[1]/div[2]/div[6]/div/div[3]/div')[0].text_content()

        self.currency['DATA'] = post_date
        self.currency['EUR'] = [eur_pln_buy, eur_pln_sell]
        self.currency['CHF'] = [chf_pln_buy, chf_pln_sell]
        self.currency['GBP'] = [gbp_pln_buy, gbp_pln_sell]
        self.currency['USD'] = [usd_pln_buy, usd_pln_sell]

        return self.currency
