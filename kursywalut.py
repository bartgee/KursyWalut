#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# author Bart Grzybicki <bgrzybicki@gmail.com>

__author__ = u'Bart Grzybicki <bgrzybicki@gmail.com>'
__version__ = u'0.1'

from lxml import html
import requests
import re
import sys

def display_header():
    print(u'$$$ KursyWalut ' + __version__ + u' $$$\n')

def get_currencies():
    try:
        page = requests.get('http://finanse.wp.pl/waluty.html')
    except Exception:
        print('Błąd pobrania danych ze strony http://finanse.wp.pl/waluty.html!')
        sys.exit(1)
    tree = html.fromstring(page.text)
    post_date = tree.xpath('//*[@id="wykres3"]/div[3]/text()')
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
        curr_dict[u'currency'] = curr[0]
        curr_dict[u'value'] = value[0]
        curr_list.append(curr_dict)
    curr_list.append({u'date':post_date[0].decode('utf-8')})
    return curr_list

def get_exchg_rate(curr_list):
    exchg_list = []
    for curr in curr_list:
        exchg_dict = {}
        try:
            is_date = re.search(u'date', curr[u'date'])
            if is_date:
                continue
        except Exception:
            pass
        try:
            is_forex = re.search(u'Forex', curr[u'currency'])
        except Exception:
            continue
        if is_forex:
            curr_idx_forex = curr[u'currency'].index(u'/')
            val_idx_forex = curr[u'value'].index(u' PLN')
            curr_explct = curr[u'currency'][:curr_idx_forex]
            val_explct = curr[u'value'][:val_idx_forex]
            exchg_dict[u'source'] = u'Forex'
            exchg_dict[u'currency'] = curr_explct.decode('utf-8')
            exchg_dict[u'value'] = float(val_explct.replace(',', '.'))
        else:
            curr_idx_nbp = curr[u'currency'].index(u' (')
            val_idx_nbp = curr[u'value'].index(u' zł')
            curr_explct = curr[u'currency'][:curr_idx_nbp]
            val_explct = curr[u'value'][:val_idx_nbp]
            exchg_dict[u'source'] = u'NBP'
            exchg_dict[u'currency'] = curr_explct.decode('utf-8')
            exchg_dict[u'value'] = float(val_explct.replace(',', '.'))
        exchg_list.append(exchg_dict)
    return exchg_list

def main():
    display_header()
    values = get_currencies()
    print(u'Kursy walut z godz. {} ze strony http://finanse.wp.pl/waluty.html:\n'.format(values[len(values) - 1]['date'].decode('utf-8')))
    for curr in get_exchg_rate(values):
        if curr[u'source'] == u'Forex':
            print(curr[u'source']+ u'|' + curr[u'currency'] + u'|' + str(curr[u'value']))
        else:
            print(curr[u'source']+ u'  |' + curr[u'currency'] + u'|' + str(curr[u'value']))

    if len(sys.argv) == 2:
        print(u'\n' + sys.argv[1].decode('utf-8') + u' zł po przeliczeniu:\n')
        for curr in get_exchg_rate(values):
            value = '{:,.2f}'.format(float(sys.argv[1]) / curr[u'value'])
            value = value.replace(',', ' ')
            if curr[u'source'] == u'Forex':
                print(curr[u'source']+ u'|' + curr[u'currency'] + u'|' + value.decode('utf-8'))
            else:
                print(curr[u'source']+ u'  |' + curr[u'currency'] + u'|' + value.decode('utf-8'))

if __name__ == '__main__':
    main()