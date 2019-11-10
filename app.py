import aiohttp

import asyncio
import logging

from parsers.BooksPageParser import BooksPageParser
from Locators import BooksLocator
from parsers.BookParser import BookParser
from utils import menu

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.INFO,
    filename='logs.txt'
)

logger = logging.getLogger('scraping')

# make request to first page of (books.toscrape.com) and
# get the books on first page and total number of pages
page_url = 'http://books.toscrape.com/'
parser = BooksPageParser(page_url, BooksLocator.BOOKS, BookParser)
books_list = parser.get_items_sync()

print(f'books list size (initial request) = {len(books_list)}')


# fetch single book page
async def fetch_books_page(session: aiohttp.client, page_link):
    book_parser = BooksPageParser(page_link, BooksLocator.BOOKS, BookParser, session)
    return await book_parser.get_items_async()


# fetch multiple book pages
async def fetch_multiple_book_pages(page_url_list):
    task_list = []
    async with aiohttp.ClientSession() as session:
        for url in page_url_list:
            task_list.append(fetch_books_page(session, url))
        return await asyncio.gather(*task_list)

url_list = []
for page_number in range(1, parser.page_count()):
    url_list.append(f'http://books.toscrape.com/catalogue/page-{page_number + 1}.html')

print('scraping...')
parsed_books_list = asyncio.run(fetch_multiple_book_pages(url_list))
print('done!')

for sub_list in parsed_books_list:
    books_list.extend(sub_list)

books_generator = (book for book in books_list)
menu(books_list, books_generator)
