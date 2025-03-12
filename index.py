library = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    read = input("Have you read this book? (yes/no): ")

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": True if read.lower() == "yes" else False
    }

    library.append(book)
    print("Book added successfully!")

def remove_book():
    title = input("Enter title of the book to remove: ")
    
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    
    print("Book not found.")

def display_books():
    if not library:
        print("No books in the library.")
        return

    for idx, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def search_book():
    keyword = input("Enter title or author to search: ").lower()

    found = False
    for book in library:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            status = "Read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
            found = True

    if not found:
        print("No matching books found.")

def display_stats():
    total = len(library)
    
    if total == 0:
        print("No books in the library.")
        return

    read_books = len([book for book in library if book["read"]])
    percent_read = (read_books / total) * 100

    print(f"Total books: {total}")
    print(f"Books read: {read_books} ({percent_read:.1f}%)")

def menu():
    while True:
        print("\nPersonal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_stats()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

menu()
