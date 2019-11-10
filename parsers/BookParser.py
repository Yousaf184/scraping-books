import re

from Locators import BookLocators


class BookParser:
    """
    class to parse single book html
    receives html markup of single book to extract book info from it (name, rating, price)
    """
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, book):
        self.book = book

    @property
    def name(self):
        return self.book.select_one(BookLocators.NAME).attrs['title']

    @property
    def price(self):
        pattern = '£[0-9]+.[0-9]+'
        price = self.book.select_one(BookLocators.PRICE).string
        match = re.search(pattern, price)
        return match.group()

    @property
    def rating(self):
        rating_tag = self.book.select_one(BookLocators.RATING)

        for rating in rating_tag.attrs['class']:
            if rating in self.RATINGS:
                return self.RATINGS[rating]

    def __repr__(self):
        return f'<Book: name={self.name}, price={self.price}, rating={self.rating}>'
