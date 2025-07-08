from books.base import Book
from services.mail_service import MailService

class Ebook(Book):
	def __init__(self, isbn, title, year, price, author,filetype):
		super().__init__(isbn, title, year, price, author)
		self.filetype = filetype

	def buy(self, quantity, email, address=None):
		MailService.send(self.title, email)

		return self.price # theres no quantity in the ebooks