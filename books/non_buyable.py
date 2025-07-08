from books.base import Book

class ShowcaseBook(Book):
    def buy(self, quantity, email, address):
        raise Exception("Quantum book store: This book is not for sale.")
