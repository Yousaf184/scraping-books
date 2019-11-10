import re

import aiohttp
import requests

from parsers.PageParser import PageParser
from Locators import BooksLocator


class BooksPageParser(PageParser):
    def __init__(self, page_url, items_locator, item_parser, session: aiohttp.client = None):
        """
        :param page_url: url of the page to scrap
        :param items_locator: selector of the items to look for in the page
        :param item_parser: class which will be used to parse each item
                             selected using 'items_locator'
        :param session: aiohttp.client session, used for making get request
                        if it is not passed to the __init__ method then
                        requests package will be used to make GET request
        """
        super().__init__(page_url, items_locator, item_parser, session)

    def page_count(self):
        pattern = '[0-9]+'
        page_count = self.soup.select_one(BooksLocator.PAGE_COUNT).string
        return int(re.findall(pattern, page_count)[1])
