import json
from book import Book
# steps to save books are loading the books
# then they can be edited


def load_books():
    try:
        file = open("book.dat", "r")
        books_dict = json.loads(file.read())  # converts the book into a dict
        books = []
        # id,name,description,isbn,page_cnt,issued,author,year
        for book in books_dict:
            books_obj = Book(book["id"], book['name'], book['description'], book['isbn'], book['page_cnt'], book['issued'],
                             book['author'], book['year'])
            books.append(books_obj)
        return books
    except:
        return []


def save_books(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
    with open("book.dat", 'w') as file:
        file.write(json.dumps(json_books, indent=4))
