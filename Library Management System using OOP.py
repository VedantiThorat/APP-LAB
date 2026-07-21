# Library Management System using OOP

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron ID: {self.patron_id}, Name: {self.name}")


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add a new book
    def add_book(self, book):
        self.books[book.book_id] = book
        print("Book added successfully!")

    # Register a new patron
    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print("Patron registered successfully!")

    # Borrow a book
    def borrow_book(self, patron_id, book_id):
        if patron_id in self.patrons and book_id in self.books:
            book = self.books[book_id]
            patron = self.patrons[patron_id]

            if book.available:
                book.available = False
                patron.borrowed_books.append(book_id)
                print(f"{patron.name} borrowed '{book.title}'.")
            else:
                print("Book is already borrowed.")
        else:
            print("Invalid Patron ID or Book ID.")

    # Return a book
    def return_book(self, patron_id, book_id):
        if patron_id in self.patrons and book_id in self.books:
            patron = self.patrons[patron_id]
            book = self.books[book_id]

            if book_id in patron.borrowed_books:
                patron.borrowed_books.remove(book_id)
                book.available = True
                print(f"{patron.name} returned '{book.title}'.")
            else:
                print("This patron has not borrowed this book.")
        else:
            print("Invalid Patron ID or Book ID.")

    # Display all books
    def display_books(self):
        print("\n----- Book List -----")
        for book in self.books.values():
            book.display()

    # Display all patrons
    def display_patrons(self):
        print("\n----- Patron List -----")
        for patron in self.patrons.values():
            patron.display()


# Main Program
library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        library.add_book(Book(book_id, title, author))

    elif choice == 2:
        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")
        library.register_patron(Patron(patron_id, name))

    elif choice == 3:
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")
        library.borrow_book(patron_id, book_id)

    elif choice == 4:
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")
        library.return_book(patron_id, book_id)

    elif choice == 5:
        library.display_books()

    elif choice == 6:
        library.display_patrons()

    elif choice == 7:
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")