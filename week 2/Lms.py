import json
import os

FILE_NAME = "books.json"

def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    books = load_books()

    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "issued": False
    }

    books.append(book)
    save_books(books)

    print("Book Added Successfully!")

def view_books():
    books = load_books()

    if not books:
        print("No Books Available!")
        return

    print("\nLibrary Books")
    print("-" * 50)

    for book in books:
        status = "Issued" if book["issued"] else "Available"

        print(f"Book ID : {book['book_id']}")
        print(f"Title   : {book['title']}")
        print(f"Author  : {book['author']}")
        print(f"Status  : {status}")
        print("-" * 50)

def search_book():
    books = load_books()

    book_id = input("Enter Book ID: ")

    for book in books:
        if book["book_id"] == book_id:
            print("\nBook Found")
            print(book)
            return

    print("Book Not Found!")

def issue_book():
    books = load_books()

    book_id = input("Enter Book ID to Issue: ")

    for book in books:
        if book["book_id"] == book_id:

            if book["issued"]:
                print("Book Already Issued!")
                return

            book["issued"] = True
            save_books(books)

            print("Book Issued Successfully!")
            return

    print("Book Not Found!")

def return_book():
    books = load_books()

    book_id = input("Enter Book ID to Return: ")

    for book in books:
        if book["book_id"] == book_id:

            if not book["issued"]:
                print("Book is Already Available!")
                return

            book["issued"] = False
            save_books(books)

            print("Book Returned Successfully!")
            return

    print("Book Not Found!")

def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Thank You!")
            break
        else:
            print("Invalid Choice!")

main()