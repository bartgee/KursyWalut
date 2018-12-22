# -*- coding: utf-8 -*-

"""Tests for MoneyPlHandler class."""

import mock
import pytest

from kursywalut.handlers.generic_handler import GenericHandler


SITE_MAP = {
            'FOREX': 'https://www.money.pl/pieniadze/forex/',
            'NBP': 'https://www.money.pl/pieniadze/nbp/srednie/',
}

DATA = {'FOREX': {'CHF': ['3,8007', '3,8107'],
                  'DATA': 'Dziś, 16.12.2018 11:32',
                  'EUR': ['4,2864', '4,2964'],
                  'GBP': ['4,7698', '4,2964'],
                  'USD': ['3,7924', '3,8024']},
        'NBP': {'CHF': '3,8202',
                'DATA': 'nr 243/A/NBP/2018 z dnia 14-12-2018',
                'EUR': '4,3021',
                'GBP': '4,7940',
                'USD': '3,8095'}}


@pytest.fixture
def generic_handler_mock():
    """Yield mocked GenericHandler class instance"""
    with mock.patch('kursywalut.handlers.generic_handler.GenericHandler') as MockGenericHandler:
        handler = MockGenericHandler.return_value
        handler.get_webpage.return_value = mock.Mock()
        handler.page = 'test'
        yield MockGenericHandler


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, string, status_code):
            self.string = string
            self.status_code = status_code
            self.content = 'test'

    return MockResponse('test', 200)


class TestGenericHandler(object):
    """
    GenericHandler class tests.
    """
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_webpage(self, generic_handler_mock, expected='test'):
        """Test get_webpage()."""
        h = GenericHandler(SITE_MAP['FOREX'])
        h.get_webpage()
        page = h.page

        assert page == expected


    def test_get_webpage_error(self):
        """Test get_webpage() exception."""
        h = GenericHandler('https://boo.nonexistent/test')
        with pytest.raises(RuntimeError) as err:
            h.get_webpage()

        assert 'Błąd pobrania danych ze strony' in str(err.value)
