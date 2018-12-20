# -*- coding: utf-8 -*-
"""Generic handler module.

It consists of GenericHandler() class, which is ihnerited by MoneyPlHandler()
class from kursywalut.handlers.moneypl_handler module. In the future, it could
be used by another handlers used to request currency data from various
websites.

"""

import logging

import six
import requests


logger = logging.getLogger(__name__)


class GenericHandler(object):
    """GenericHandler class.

    This is main handler class. All other handlers should inherit from it.

    Attributes:
        site_mapping (dict): A dict containing website mapping.
        page_list (list): A list of string containing responses from websites.
        page (str): data retrieved from website.
        url (str): URL to retrieve data from.

    """

    def __init__(self, url):
        """Initialization method."""
        self.site_mapping = None
        self.page_list = None
        self.page = None
        self.url = url
        self.download_time = None
        self.parse_time = None

    def get_webpage(self):
        """get_webpage method.

        Send the request from self.site_mapping list.

        """
        # for key, value in self.site_mapping.items():
        #     if value == self.url:
        #         site = self._to_unicode(key)

        logger.debug('Data retrieving...')

        try:
            page = requests.get(self.url)
            logger.debug('Done.')
            self.page = page.content
        except requests.exceptions.RequestException as error:
            msg = self._to_unicode('Błąd pobrania danych ze strony {}!'.format(self.url))
            logger.error(msg + ': ' + str(error))

    def _to_unicode(self, value):
        """Convert value to unicode.

        Args:
            value (str): Value to be converted to unicode.

        Returns:
            string (Python 3) or unicode (Python 2).

        """
        return six.text_type(value)
