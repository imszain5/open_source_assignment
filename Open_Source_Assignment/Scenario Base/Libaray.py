class Library:
    def _init_(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}")

# Abstraction
class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author

# Composition
class MemberLibrary:
    def _init_(self, library):
        self.library = library
        self.checked_out_books = []

    def check_out_book(self, book):
        if book in self.library.books:
            self.checked_out_books.append(book)
            self.library.remove_book(book)
            print(f"You've checked out '{book.title}' by {book.author}.")

    def return_book(self, book):
        if book in self.checked_out_books:
            self.checked_out_books.remove(book)
            self.library.add_book(book)
            print(f"You've returned '{book.title}' by {book.author}.")

# Example Usage
library = Library("Public Library")
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("Available books in the library:")
library.list_books()

member = MemberLibrary(library)
member.check_out_book(book2)
member.check_out_book(book3)

print("Books checked out by the member:")
for book in member.checked_out_books:
    print(f"Title: {book.title}, Author: {book.author}")

member.return_book(book3)
print("Available books in the library:")
library.list_books()