def top_ten_books(books_list):
    top_10_books = sorted(books_list, key=lambda book: book.rating * -1)  # desc order
    print(top_10_books[:10])


def top_ten_cheapest_books(books_list):
    top_10_cheap_books = sorted(books_list, key=lambda book: (book.price, book.rating))
    print(top_10_cheap_books[:10])


def print_all_books(books_list):
    for book in books_list:
        print(book)


def next_book(books_generator):
    print(next(books_generator))


def total_book_count(books_list):
    print(len(books_list))


menu_str = '''
Enter on of the following:
1. press 'c' to see 10 cheapest books
2. press 'b' to see best 10 books
3. press 'n' to see next book in catalogue
4. press 'l' to see total number of books
5. press 'q' to quit

your choice: '''

menu_dict = {
    'c': top_ten_cheapest_books,
    'b': top_ten_books,
    'n': next_book,
    'l': total_book_count
}


def menu(books_list, books_generator):
    user_input = input(menu_str)
    while user_input != 'q':
        if user_input in menu_dict:
            if user_input == 'n':
                menu_dict[user_input](books_generator)
            else:
                menu_dict[user_input](books_list)
            user_input = input(menu_str)
        else:
            print('invalid command, try again.')
            user_input = input('')
