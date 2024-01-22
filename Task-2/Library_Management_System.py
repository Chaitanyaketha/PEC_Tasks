class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_books(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)
        return book

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            if book.available:
                print(f"{book.title} by {book.author} ({book.year})")

    def borrow_book(self, member, book):
        if book.available:
            book.available = False
            member.borrowed_books.append(book)
            print(f"{member.name} has borrowed '{book.title}'")
        else:
            print(f"Book '{book.title}' is not available for borrowing.")

    def return_book(self, member, book):
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print(f"{member.name} has returned the '{book.title}'")
        else:
            print(f"Book '{book.title}' cannot be returned as it is not borrowed.")

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

# Example Usage:
library = Library()

#Addding books to the library
book1 = library.add_books("DBMS", "Reema Thareja", "1990")
book2 = library.add_books("Python", "Guido van Rossum", "1931")

#Display the Books in library
library.display_books()

#Define the students or members who are wants to borrow books
member1 = Member("Chaitanya")
member2 = Member("Likhith")
#many more 

library.borrow_book(member1, book1)
library.borrow_book(member2, book2)

library.display_books()

library.return_book(member1, book1)
# library.return_book(member2, book2)

library.display_books()
