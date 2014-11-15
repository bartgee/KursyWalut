#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# author Bart Grzybicki <bgrzybicki@gmail.com>

__author__ = u'Bart Grzybicki <bgrzybicki@gmail.com>'
__version__ = u'0.1'

from lxml import html
import requests
import re

def display_header():
    print(u'$$$ KursyWalut ' + __version__ + u' $$$\n')

def get_currencies():
    page = requests.get('http://finanse.wp.pl/waluty.html')
    tree = html.fromstring(page.text)
    lt_list = []
    index = 1
    curr_list = []
    while True:
        curr_dict = {}
        curr = tree.xpath('//*[@id="wykresyWalutyT{}"]/a/span[1]/span/text()'.format(index))
        value = tree.xpath('//*[@id="wykresyWalutyT{}"]/a/span[2]/text()'.format(index))
        if value == []:
            break
        index += 1
        #print(curr)
        curr_dict[u'currency'] = curr[0]#.encode('utf-8')
        curr_dict[u'value'] = value[0]#.encode('utf-8')
        curr_list.append(curr_dict)
    return curr_list

def get_exchg_rate(curr_list):
    exchg_list = []
    for curr in curr_list:
        exchg_dict = {}
        is_forex = re.search(u'Forex', curr[u'currency'])
        if is_forex:
            curr_idx_forex = curr[u'currency'].index(u'/')
            val_idx_forex = curr[u'value'].index(u' PLN')
            curr_explct = curr[u'currency'][:curr_idx_forex]
            val_explct = curr[u'value'][:val_idx_forex]
            exchg_dict[u'source'] = u'Forex'
            exchg_dict[u'currency'] = curr_explct
            exchg_dict[u'value'] = float(val_explct.replace(',', '.'))
        else:
            curr_idx_nbp = curr[u'currency'].index(u' (')
            val_idx_nbp = curr[u'value'].index(u' zł')
            curr_explct = curr[u'currency'][:curr_idx_nbp]
            val_explct = curr[u'value'][:val_idx_nbp]
            exchg_dict[u'source'] = u'NBP'
            exchg_dict[u'currency'] = curr_explct
            exchg_dict[u'value'] = float(val_explct.replace(',', '.'))
        exchg_list.append(exchg_dict)
    return exchg_list
        #print_header('')

def main():
    display_header()
    values = get_currencies()
    print(values)
    for curr in values:
        print(curr['currency'] + ': ' + curr['value'])
    print(get_exchg_rate(values))
    for curr in get_exchg_rate(values):
        if curr['source'] == 'Forex':
            print(curr[u'source']+ u'|' + curr[u'currency'] + u'|' + str(curr[u'value']))
        else:
            print(curr[u'source']+ u'  |' + curr[u'currency'] + u'|' + str(curr[u'value']))


if __name__ == '__main__':
    main()