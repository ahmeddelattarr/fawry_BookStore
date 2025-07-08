from datetime import datetime

class BookInventory:
	def __init__(self):
		self.books = {}

	def add_book(self, book):
		self.books[book.isbn] = book
		print(f"Quantum book store: Added {book}")

	def remove_outdated(self,threshold_years):
		current_year = datetime.now().year
		removed = []

		for isbn in list(self.books):
			book = self.books[isbn]
			if book.is_outdated(current_year, threshold_years):
				removed.append(self.books.pop(isbn))
		print(f"Quantum book store: Removed {len(removed)} outdated books.")
		return removed

	def buy_book(self, isbn, quantity, email, address):
		if isbn not in self.books:
			raise Exception("Quantum book store: Book not found in inventory.")

		amount = self.books[isbn].buy(quantity, email, address)
		print(f"Quantum book store: Paid amount = {amount}")
		return amount
