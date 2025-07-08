from books.base import Book
from services.shipping_service import ShippingService

class PaperBook(Book):
	def __init__(self, isbn, title, year, price, author,stock):
		super().__init__(isbn, title, year, price, author)
		self.stock = stock

	def buy (self, quantity, email, address):
		if quantity > self.stock:
			raise ValueError(f"Only {self.stock} copies available in stock.")
		self.stock -= quantity
		ShippingService.send(self.title, address)
		return self.price * quantity

