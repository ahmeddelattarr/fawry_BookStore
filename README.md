


# Quantum Bookstore — OOP Design Challenge

A console-based Python bookstore system designed with clean OOP principles, modular structure, and extensibility in mind. Simulates adding, buying, and managing different types of books like paperbacks, ebooks, and demo/showcase copies.

---

##  Features

- ✅ Add books to inventory
- ✅ Handle 3 distinct book types:
  - **PaperBook** – Shipped physically to a given address
  - **EBook** – Sent via email in a specific filetype
  - **ShowcaseBook** – Display/demo copy, not for sale
- ✅ Buy books using ISBN, quantity, email, and address
- ✅ Prevent buying out-of-stock or non-sellable books
- ✅ Remove outdated books (based on publication year)
- ✅ Simulated email and shipping delivery services
- ✅ Graceful error handling for all edge cases
- ✅ Clean, extensible class-based architecture

---

##  Project Structure

```

fawry-bookstore/
│
├── test.py                        # Entry point: QuantumBookstoreFullTest
├── README.md
│
├── inventory.py                  # BookInventory: add, buy, remove logic
│
├── books/
│   ├── base_book.py              # BaseBook with shared logic
│   ├── paper_book.py             # PaperBook (stock-based, shippable)
│   ├── ebook.py                  # EBook (email delivery)
│   └── non_buyable.py          # ShowcaseBook (not for sale)
│
└── services/
├── mail_service.py           # MailService: simulates email sending
└── shipping_service.py       # ShippingService: simulates physical shipping

````

---

##  How to Run

```bash
python test.py
````

This will simulate:

* Adding books of different types
* Removing outdated books
* Attempting valid and invalid purchases

---

##  Sample Console Output

```
Quantum book store: Added Clean Code (2008) by Robert Martin
Quantum book store: Added Deep Learning (2016) by Ian Goodfellow
Quantum book store: Added msh3aref (1950) by ana

Quantum book store: Removed 1 outdated books.

Quantum book store: Shipping 'Clean Code' to 123 Street, giza
Quantum book store: Paid amount = 600

Quantum book store: Sending 'Deep Learning' to fawry@hobalala.com
Quantum book store: Paid amount = 150

Quantum book store: This book is not for sale.
```

---

##  OOP Concepts Used

* **Inheritance**: `PaperBook`, `EBook`, and `ShowcaseBook` all extend `BaseBook`
* **Polymorphism**: The `buy()` method behaves differently depending on the book type
* **Encapsulation**: Inventory and book logic is modular and self-contained
* **Exception-based Control**: `ShowcaseBook` blocks purchase attempts by raising exceptions
* **Extensibility**: Add new book types without modifying inventory logic

---



##  Notes

* All behaviors are simulated with print statements (no real email or shipping integration)
* Console output always starts with `Quantum book store:` for clarity
* All business rules (e.g., non-sellable books, stock checks) are enforced via exceptions inside the `buy()` methods

---




