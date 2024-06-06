class Library:
    def __init__(self):
        self.books = {}  # Dictionary to store book details with book ID as the key
        self.issued_books = {}  # Dictionary to store issued book details with book ID as the key

    def add_book(self, book_id, title, author, copies):
        if book_id in self.books:
            self.books[book_id]['copies'] += copies
        else:
            self.books[book_id] = {
                'title': title,
                'author': author,
                'copies': copies
            }
        print(f"Book '{title}' added successfully.")

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("Available books in the library:")
        for book_id, details in self.books.items():
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Copies: {details['copies']}")

    def issue_book(self, book_id, user):
        if book_id not in self.books:
            print("Book ID not found.")
            return
        if self.books[book_id]['copies'] == 0:
            print("No copies of this book are available for issue.")
            return
        self.books[book_id]['copies'] -= 1
        self.issued_books[book_id] = {
            'title': self.books[book_id]['title'],
            'author': self.books[book_id]['author'],
            'issued_to': user
        }
        print(f"Book '{self.books[book_id]['title']}' issued to {user}.")

    def return_book(self, book_id, user):
        if book_id not in self.issued_books:
            print("This book was not issued.")
            return
        if self.issued_books[book_id]['issued_to'] != user:
            print("This book was not issued to you.")
            return
        self.books[book_id]['copies'] += 1
        del self.issued_books[book_id]
        print(f"Book '{self.books[book_id]['title']}' returned successfully.")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            copies = int(input("Enter number of copies: "))
            library.add_book(book_id, title, author, copies)
        elif choice == '2':
            library.view_books()
        elif choice == '3':
            book_id = input("Enter book ID to issue: ")
            user = input("Enter user name: ")
            library.issue_book(book_id, user)
        elif choice == '4':
            book_id = input("Enter book ID to return: ")
            user = input("Enter user name: ")
            library.return_book(book_id, user)
        elif choice == '5':
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
