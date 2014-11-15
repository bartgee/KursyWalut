#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# author Bart Grzybicki <bgrzybicki@gmail.com>

__author__ = 'Bart Grzybicki <bgrzybicki@gmail.com>'
__version__ = '0.1'

from lxml import html
import requests

#OUT_FILE = u'linuxtoday.txt'

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
        curr_dict['currency'] = curr[0]
        curr_dict['value'] = value[0]
        curr_list.append(curr_dict)
    return curr_list

def main():
    values = get_currencies()
    for curr in values:
        print(curr['currency'] + ': ' + curr['value'])

if __name__ == '__main__':
    main()