#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# KursyWalut - gets current exchange rates and converts between them to PLN and vice versa
# Copyright (C) 2014 Bart Grzybicki <bgrzybicki@gmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA

__author__ = u'Bart Grzybicki <bgrzybicki@gmail.com>'
__version__ = u'0.1'

from lxml import html
import requests
import re
import sys

def display_header():
    print(u'##################')
    print(u'$ KursyWalut ' + __version__ + u' $')
    print(u'##################\n')

def get_currencies():
    sys.stdout.write(u'Pobieram dane... ') # instead of print() to print without a new line
    sys.stdout.flush()
    try:
        page = requests.get('http://finanse.wp.pl/waluty.html')
    except Exception:
        print(u'Błąd pobrania danych ze strony http://finanse.wp.pl/waluty.html!')
        sys.exit(1)
    tree = html.fromstring(page.text)
    post_date = tree.xpath('//*[@id="wykres3"]/div[3]/text()')
    index = 1
    curr_list = []
    while True:
        curr_dict = {}
        curr = tree.xpath('//*[@id="wykresyWalutyT{}"]/a/span[1]/span/text()'.format(index))
        value = tree.xpath('//*[@id="wykresyWalutyT{}"]/a/span[2]/text()'.format(index))
        change = tree.xpath('//*[@id="wykresyWalutyT{}"]/a/span[3]/text()'.format(index))
        if value == []:
            break
        index += 1
        curr_dict[u'currency'] = curr[0]
        curr_dict[u'value'] = value[0]
        curr_dict[u'change'] = change[0]
        curr_list.append(curr_dict)
    curr_list.append({u'date':post_date[0].decode('utf-8')})
    print(u'OK!')
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

        exchg_dict[u'change'] = curr[u'change']
        exchg_list.append(exchg_dict)
    return exchg_list

def main():
    display_header()
    values = get_currencies()
    exchg_rate = get_exchg_rate(values)
    print(u'Kursy z godz. {} ze strony http://finanse.wp.pl/waluty.html:\n'.format(values[len(values) - 1]['date'].decode('utf-8')))
    for curr in exchg_rate:
        if curr[u'source'] == u'Forex':
            print(curr[u'source']+ u'|' + curr[u'currency'] + u'|' + str(curr[u'value'])
            + u'|' + curr[u'change'])
        else:
            print(curr[u'source']+ u'  |' + curr[u'currency'] + u'|' + str(curr[u'value'])
            + u'|' + curr[u'change'])

    if len(sys.argv) == 2 or len(sys.argv) == 3 and sys.argv[2].upper() == 'PLN':
        print(u'\n' + sys.argv[1].decode('utf-8') + u' PLN po przeliczeniu:\n')
        for curr in exchg_rate:
            value = u'{:,.2f}'.format(float(sys.argv[1]) / curr[u'value'])
            value = value.replace(',', ' ')
            if curr[u'source'] == u'Forex':
                print(curr[u'source']+ u'|' + curr[u'currency'] + u'|' + value.decode('utf-8'))
            else:
                print(curr[u'source']+ u'  |' + curr[u'currency'] + u'|' + value.decode('utf-8'))

    if len(sys.argv) == 3 and sys.argv[2].upper() != 'PLN' \
            or len(sys.argv) == 4 and sys.argv[3].upper() == 'PLN':
        print(u'\n' + sys.argv[1].decode('utf-8')
              + u' {} po przeliczeniu na PLN:\n'.format(sys.argv[2].upper()))
        for curr in exchg_rate:
            if curr[u'currency'] == sys.argv[2].decode('utf-8').upper() and curr[u'source'] == u'Forex':
                curr_forex = curr[u'value'] * float(sys.argv[1])
                curr_forex = round(curr_forex, 2)
                curr_forex = u'{:,.2f}'.format(curr_forex)
                print(u'Forex|PLN|' + str(curr_forex))
            elif curr[u'currency'] == sys.argv[2].decode('utf-8').upper() and curr[u'source'] == u'NBP':
                curr_nbp = curr[u'value'] * float(sys.argv[1])
                curr_nbp = round(curr_nbp, 2)
                curr_nbp = u'{:,.2f}'.format(curr_nbp)
                #print(u'NBP  |{}'.format(sys.argv[2].upper()) + u'|' + str(curr_nbp))
                print(u'NBP  |PLN|' + str(curr_nbp))

    if len(sys.argv) == 4 and sys.argv[3].upper() != 'PLN' and sys.argv[2].upper() != 'PLN':
        print(u'\n' + sys.argv[1].decode('utf-8')
              + u' {} po przeliczeniu na {}:\n'.format(sys.argv[2].upper(), sys.argv[3].upper()))
        for curr in exchg_rate:
            if curr[u'currency'] == sys.argv[2].decode('utf-8').upper() and curr[u'source'] == u'Forex':
                curr_from = curr[u'value'] * float(sys.argv[1])
                for curr_second in exchg_rate:
                    if curr_second[u'currency'] == sys.argv[3].decode('utf-8').upper() \
                            and curr_second[u'source'] == u'Forex':
                        curr_to = curr_from / curr_second[u'value']
                        curr_to = round(curr_to, 2)
                        curr_to = u'{:,.2f}'.format(curr_to)
                        print(u'Forex|{}'.format(sys.argv[3].upper()) + u'|' + str(curr_to))
                    else:
                        continue
            elif curr[u'currency'] == sys.argv[2].decode('utf-8').upper() and curr[u'source'] == u'NBP':
                curr_from = curr[u'value'] * float(sys.argv[1])
                for curr_second in exchg_rate:
                    if curr_second[u'currency'] == sys.argv[3].decode('utf-8').upper() \
                            and curr_second[u'source'] == u'NBP':
                        curr_to = curr_from / curr_second[u'value']
                        curr_to = round(curr_to, 2)
                        curr_to = u'{:,.2f}'.format(curr_to)
                        print(u'NBP  |{}'.format(sys.argv[3].upper()) + u'|' + str(curr_to))
                    else:
                        continue

    if len(sys.argv) == 4 and sys.argv[3].upper() != 'PLN' and sys.argv[2].upper() == 'PLN':
        print(u'\n' + sys.argv[1].decode('utf-8') + u' PLN po przeliczeniu args2:\n')
        for curr in exchg_rate:
            value = u'{:,.2f}'.format(float(sys.argv[1]) / curr[u'value'])
            value = value.replace(',', ' ')
            if curr[u'source'] == u'Forex' and curr[u'currency'] == sys.argv[3].upper():
                print(curr[u'source']+ u'|' + curr[u'currency'] + u'|' + value.decode('utf-8'))
            elif curr[u'source'] == u'NBP' and curr[u'currency'] == sys.argv[3].upper():
                print(curr[u'source']+ u'  |' + curr[u'currency'] + u'|' + value.decode('utf-8'))

if __name__ == '__main__':
    main()
