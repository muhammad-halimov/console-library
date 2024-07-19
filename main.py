from modules import BookStore

print("Welcome to the Book Store!")


def main_menu():
    print("Please select an option:")
    print("1. Add a book")
    print("2. Eliminate a book")
    print("3. Search for a book")
    print("4. Show all books")
    print("5. Update book status")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        year = input("Enter the book year: ")
        book_store = BookStore()
        book_store.add_book(title, author, year)
        print("Book added successfully.")
        print()
        main_menu()
    elif choice == "2":
        b_id = input("Enter the book ID: ")
        result = BookStore.eliminate_book(b_id)
        print(result)
        print()
        main_menu()
    elif choice == "3":
        title = input("Enter the book title (optional): ")
        author = input("Enter the book author (optional): ")
        year = input("Enter the book year (optional): ")
        b_id = input("Enter the book ID (optional): ")
        books = BookStore.search_book(title, author, year, b_id)
        if books:
            for book in books:
                print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, ID: {book['b_id']}")
        else:
            print("No books found.")
        print()
        main_menu()
    elif choice == "4":
        books = BookStore.show_books()
        if books:
            print(f"{'Title':15}\t{'Author':15}\t{'Year'}\t{'ID':38}\t{'In Stock'}")
            print("-" * 100)
            for book in books:
                print(f"{book['title']:<15}\t{book['author']:<15}\t{book['year']}\t{book['b_id']}\t{book['in_stock']}")
                print("-" * 100)
        else:
            print("No books found.")
        print()
        main_menu()
    elif choice == "5":
        b_id = input("Enter the book ID: ")
        new_status = input("Enter the new status (True/False): ")
        result = BookStore.update_book_status(b_id, new_status == "True")
        print(result)
        print()
        main_menu()
    elif choice == "6":
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        print()
        main_menu()


if __name__ == "__main__":
    main_menu()
