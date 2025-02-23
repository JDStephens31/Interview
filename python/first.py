# 
# There is 1 error within this file.
# 

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f"Error: '{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed.")

    def return_book(self):
        if not self.is_borrowed:
            print(f"Error: '{self.title}' was not borrowed.")
        else:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned.")

    def display(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            book.display()

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        print(f"Error: Book '{title}' not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"Error: Book '{title}' not found.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(title)
                print(f"'{title}' has been removed from the library.")
                return
        print(f"Error: Book '{title}' not found.")


# Main Program
library = Library()

library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

print("\nLibrary Collection:")
library.display_books()

print("\nBorrowing Books:")
library.borrow_book("1984")
library.borrow_book("The Great Gatsby")

print("\nReturning a Book:")
library.return_book("1984")

print("\nRemoving a Book:")
library.remove_book("To Kill a Mockingbird")

print("\nUpdated Library Collection:")
library.display_books()
