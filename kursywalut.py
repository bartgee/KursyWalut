#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# author Bart Grzybicki <bgrzybicki@gmail.com>

__author__ = 'Bart Grzybicki <bgrzybicki@gmail.com>'
__version__ = '0.1'

from lxml import html
import requests

#OUT_FILE = u'linuxtoday.txt'

def main():
    page = requests.get('http://finanse.wp.pl/waluty.html')
    tree = html.fromstring(page.text)
    lt_list = []
    index = 1
    while True:
        #lt_dict = {}
        curr = tree.xpath('//*[@id="wykresyWalutyT{}"]/a/span[1]/span/text()'.format(index))
        value = tree.xpath('//*[@id="wykresyWalutyT{}"]/a/span[2]/text()'.format(index))
        if value == []:
            break
        index += 1
        #print(curr)
        print(curr[0] + ': ' + value[0])

if __name__ == '__main__':
    main()