class MailService:
    @staticmethod
    def send(book_title, email):
        print(f"Quantum book store: Sending '{book_title}' to {email}")
