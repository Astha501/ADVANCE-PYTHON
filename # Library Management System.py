# Library Management System

# List to store all books
library = []

# Function to add a book
def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "title": title,
        "author": author,
        "available": True
    }

    library.append(book)
    print("Book added successfully!\n")


# Function to display all books
def display_books():
    if len(library) == 0:
        print("No books available in library.\n")
    else:
        print("\nLibrary Books:")
        for i, book in enumerate(library, start=1):
            status = "Available" if book["available"] else "Issued"
            print(f"{i}. {book['title']} by {book['author']} - {status}")
        print()


# Function to issue a book
def issue_book():
    title = input("Enter Book Title to Issue: ")

    for book in library:
        if book["title"].lower() == title.lower():
            if book["available"]:
                book["available"] = False
                print("Book issued successfully!\n")
            else:
                print("Book is already issued.\n")
            return

    print("Book not found.\n")


# Function to return a book
def return_book():
    title = input("Enter Book Title to Return: ")

    for book in library:
        if book["title"].lower() == title.lower():
            if not book["available"]:
                book["available"] = True
                print("Book returned successfully!\n")
            else:
                print("Book was not issued.\n")
            return

    print("Book not found.\n")


# Main Menu Function
def main():
    while True:
        print("===== Library Management System =====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Thank you for using Library System!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the program
main()