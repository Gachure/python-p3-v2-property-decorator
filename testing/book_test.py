import sys
import os

# Add the lib directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib')))

from book import Book

def test_book_initialization():
    book = Book("1984", "George Orwell", 328)
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.pages == 328

def test_book_str():
    book = Book("1984", "George Orwell", 328)
    assert str(book) == "'1984' by George Orwell, 328 pages"
