from uuid import uuid4
import json


class BookStore:
    def __init__(self):
        self.b_id = str(uuid4())

    def add_book(self, title: str, author: str, year: str, status: bool = True):
        """
        Adds a new book to the book store.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
            status (bool): Indicates whether the book is in stock.

        Void function
        """
        book_data = {
            "b_id": self.b_id,
            "title": title,
            "author": author,
            "year": year,
            "in_stock": status
        }

        with open("db.json", "r+", encoding="UTF-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = list()
            data.append(book_data)
            file.seek(0)
            json.dump(data, file, indent=4)

    @staticmethod
    def eliminate_book(b_id: uuid4()):
        """
        Removes a book from the book store

        Args:
            b_id (str): The ID of the book.

        Void function
        """
        with open("db.json", "r+", encoding="UTF-8") as file:
            try:
                data = json.load(file)
                original_length = len(data)
                data = [book for book in data if book["b_id"] != b_id]
                if len(data) == original_length:
                    return "Unsuccessful elimination"
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
                return "Successful elimination"
            except json.JSONDecodeError:
                return "Unsuccessful elimination"

    @staticmethod
    def search_book(title: str = None, author: str = None, year: str = None, b_id: uuid4() = None) -> list:
        """
        Search a book in the book store.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
            b_id (uuid4): ID of the book.

        Returns:
            list: The list of books that met the requirements.
        """
        with open("db.json", "r", encoding="UTF-8") as file:
            try:
                data = json.load(file)
                if title:
                    data = [book for book in data if book["title"] == title]
                if author:
                    data = [book for book in data if book["author"] == author]
                if b_id:
                    data = [book for book in data if book["b_id"] == b_id]
                if year:
                    data = [book for book in data if book["year"] == year]
                return data
            except json.JSONDecodeError:
                return list()

    @staticmethod
    def show_books() -> list:
        """
        List of all kinds of books in the book store.

        Args:

        Returns:
            list: The list of all books.
        """
        with open("db.json", "r", encoding="UTF-8") as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                return list()

    @staticmethod
    def update_book_status(b_id: uuid4(), new_status: bool) -> str:
        """
        Updates a book status in the book store.

        Args:
            b_id (uuid4): ID of the book.
            new_status(bool): funny, however new status

        Returns:
            str: Operation status.
        """
        with open("db.json", "r+", encoding="UTF-8") as file:
            try:
                data = json.load(file)
                for book in data:
                    if book["b_id"] == b_id:
                        book["in_stock"] = new_status
                        file.seek(0)
                        file.truncate()
                        json.dump(data, file, indent=4)
                        return "Successful update"
                return "Book not found"
            except json.JSONDecodeError:
                return "Unsuccessful update"
