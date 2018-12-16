#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `kursywalut` package."""

import pytest
import mock

from requests.exceptions import RequestException

from kursywalut import interface


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    data = {'FOREX': {'CHF': ['3,8007', '3,8107'],
                      'DATA': 'Dziś, 16.12.2018 11:32',
                      'EUR': ['4,2864', '4,2964'],
                      'GBP': ['4,7698', '4,2964'],
                      'USD': ['3,7924', '3,8024']},
            'NBP': {'CHF': '3,8202',
                    'DATA': 'nr 243/A/NBP/2018 z dnia 14-12-2018',
                    'EUR': '4,3021',
                    'GBP': '4,7940',
                    'USD': '3,8095'}}

    interface.get_moneypl = mock.MagicMock(return_value=data)

    return interface.get_moneypl()


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    expected = {'FOREX': {'CHF': ['3,8007', '3,8107'],
                          'DATA': 'Dziś, 16.12.2018 11:32',
                          'EUR': ['4,2864', '4,2964'],
                          'GBP': ['4,7698', '4,2964'],
                          'USD': ['3,7924', '3,8024']},
                'NBP': {'CHF': '3,8202',
                        'DATA': 'nr 243/A/NBP/2018 z dnia 14-12-2018',
                        'EUR': '4,3021',
                        'GBP': '4,7940',
                        'USD': '3,8095'}}

    assert response == expected
