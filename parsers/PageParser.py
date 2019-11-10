import aiohttp
import requests
from bs4 import BeautifulSoup


class PageParser:
    """
    this class parses web page and returns a list of parsed items
    """

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
        self.http_session = session
        self.soup = None
        self.items_locator = items_locator
        self.item_parser = item_parser
        self.page_url = page_url

    async def get_html(self):
        async with self.http_session.get(self.page_url) as response:
            return await response.text()

    async def get_items_async(self):
        html_str = await self.get_html()
        self.soup = BeautifulSoup(html_str, 'html.parser')

        return self.get_parsed_items_list()

    def get_items_sync(self):
        html_str = requests.get(self.page_url).text
        self.soup = BeautifulSoup(html_str, 'html.parser')

        return self.get_parsed_items_list()

    def get_parsed_items_list(self):
        items = self.soup.select(self.items_locator)
        return [self.item_parser(item) for item in items]
