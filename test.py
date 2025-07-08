from books.paper_book import PaperBook
from books.ebook import Ebook
from books.non_buyable import ShowcaseBook
from inventory import BookInventory

class QuantumBookstoreFullTest:
    @staticmethod
    def run():
        inventory = BookInventory()

        # Add books
        b1 = PaperBook("001", "Clean Code", 2008, 300, "Robert Martin", 10)
        b2 = Ebook("002", "Deep Learning", 2016, 150, "Ian Goodfellow", "pdf")
        b3 = ShowcaseBook("003", "The Art of War", 1950, 0, "Sun Tzu")

        inventory.add_book(b1)
        inventory.add_book(b2)
        inventory.add_book(b3)

        # Remove outdated books
        inventory.remove_outdated(threshold_years=10)

        # Buy books
        try:
            inventory.buy_book("001", 2, "user@example.com", "123 Street, Cairo")
        except Exception as e:
            print(e)

        try:
            inventory.buy_book("002", 1, "user@example.com", "123 Street, Cairo")
        except Exception as e:
            print(e)

        try:
            inventory.buy_book("003", 1, "user@example.com", "123 Street, markazmotobas")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    QuantumBookstoreFullTest.run()
