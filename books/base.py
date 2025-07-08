class Book:
	def __init__(self,isbn,title,year,price,author):
		self.isbn = isbn
		self.title = title
		self.year = year
		self.price = price
		self.author = author


	def is_outdated(self,current_year,years_threshold):

		return (current_year - self.year) > years_threshold

	def buy(self,quantity,email,address):

		raise NotImplementedError("This method would be implemented in subclasses")

	def __str__(self):
		return f"{self.title} by {self.author} "
