#Library Management System 

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    # Add a new book
    def add_book(self, book):
        self.books.append(book)
        print(book, "added successfully.")

    # Register a new user
    def register_user(self, user):
        self.users.append(user)
        print(user, "registered successfully.")

    # Borrow a book
    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("You borrowed:", book)
        else:
            print("Book is not available.")

    # Return a book
    def return_book(self, book):
        self.books.append(book)
        print("You returned:", book)

    # Display available books
    def show_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print("-", book)


# Main Program
library = Library()

while True:
    print("\n***** Library Management System *****")
    print("1. Add Book")
    print("2. Register User")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == "2":
        user = input("Enter user name: ")
        library.register_user(user)

    elif choice == "3":
        book = input("Enter book name to borrow: ")
        library.borrow_book(book)

    elif choice == "4":
        book = input("Enter book name to return: ")
        library.return_book(book)

    elif choice == "5":
        library.show_books()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")