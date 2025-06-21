
# ==============================================================================
# Question 2 (25 points)
# Library Management System
# Date: may, 2025
# Author: 21 - 363 - 287 - 41
# ==============================================================================

# ==============================================================================
# This program implements a library-system where a user can choose between 
# ==============================================================================

# Book class
class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.checked_out = False  # checks if a book is checked out or available

    # Book info and availability
    def __str__(self):
        status = "Unavailable" if self.checked_out else "Available"
        return f"{self.title} by {self.author} ({self.num_pages} pages) - {status}"


# Library class
class Library:
    def __init__(self):
        self.books = []

    # Add book to library
    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} to library")

   # Remove book
    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book: {title} was removed from library.")
                
                return
        print(f"Book: {title} was not found")


    # Mark book as checked out
    def check_out(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.checked_out:
                    print(f"Book already checked out: {title}")
                else:
                    book.checked_out = True
                    print(f"You checked out: {title}")
                    
                return
        print(f"Book: {title} was not found")

    # Mark book as returned
    def check_in(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.checked_out:
                    print(f"Book already in library: {title}")
                else:
                    book.checked_out = False
                    print(f"Returned: {title}")
                    
                return
        print(f"Book: {title} was not found")

    # Print books currently in library
    def print_books(self):
        if not self.books:
            print("The library is empty.")
            return
        print("\nBooks in library:")
        for book in self.books:
            print(book)
        print()
        

# Main
def main():
    lib = Library()
    
    # Add some books to the library
    lib.add_book(Book("ALEX FERGUSON: My Autobiography", "Alex Ferguson", 370))
    lib.add_book(Book("The Fellowship of the Ring", "J. R. R. Tolkien", 448))
    lib.add_book(Book("Harry Potter and the Order of the Phoenix", "Rowling J.K.", 816))
    
    
    while True:
        print("\nLibrary Menu: ")
        print("1. Add book to library")
        print("2. Remove book from library")
        print("3. Check out book")
        print("4. Check in book")
        print("5. List all books")
        print("6. Quit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            try:
                pages = int(input("Enter number of pages: "))
                lib.add_book(Book(title, author, pages))
            except ValueError:
                print("Error, number of pages must be a number.")

        elif choice == "2":
            title = input("Enter title of book to remove: ")
            lib.remove_book(title)

        elif choice == "3":
            title = input("Enter book to check out: ")
            lib.check_out(title)

        elif choice == "4":
            title = input("Enter book to check in: ")
            lib.check_in(title)

        elif choice == "5":
            lib.print_books()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


