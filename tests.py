import unittest
import json
from modules import BookStore


class TestBookStore(unittest.TestCase):
    def setUp(self):
        self.bookstore = BookStore()
        self.bookstore.add_book("Book 1", "Author 1", "2022")
        self.bookstore.add_book("Book 2", "Author 2", "2023")
        self.bookstore.add_book("Book 3", "Author 1", "2022")
        with open("db.json", "r") as file:
            self.data = json.load(file)

    def test_add_book(self):
        self.bookstore.add_book("Book 4", "Author 4", "2024")
        with open("db.json", "r") as file:
            data = json.load(file)
            self.assertEqual(len(data), 4)
            self.assertEqual(data[3]["title"], "Book 4")
            self.assertEqual(data[3]["author"], "Author 4")
            self.assertEqual(data[3]["year"], "2024")
            self.assertTrue(data[3]["in_stock"])

    def test_eliminate_book(self):
        b_id = self.data[0]["b_id"]
        result = self.bookstore.eliminate_book(b_id)
        self.assertEqual(result, "Successful elimination")
        with open("db.json", "r") as file:
            data = json.load(file)
            self.assertEqual(len(data), 2)

        b_id = "123456"
        result = self.bookstore.eliminate_book(b_id)
        self.assertEqual(result, "Unsuccessful elimination")

    def test_search_book(self):
        result = self.bookstore.search_book(title="Book 1")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Book 1")

        result = self.bookstore.search_book(author="Author 1")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["author"], "Author 1")
        self.assertEqual(result[1]["author"], "Author 1")

        result = self.bookstore.search_book(year="2022")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["year"], "2022")
        self.assertEqual(result[1]["year"], "2022")

        result = self.bookstore.search_book(b_id=self.data[0]["b_id"])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["b_id"], self.data[0]["b_id"])

    def test_update_book_status(self):
        b_id = self.data[0]["b_id"]
        result = self.bookstore.update_book_status(b_id, False)
        self.assertEqual(result, "Successful update")
        with open("db.json", "r") as file:
            data = json.load(file)
            self.assertFalse(data[0]["in_stock"])

        result = self.bookstore.update_book_status("123456", False)
        self.assertEqual(result, "Book not found")


if __name__ == '__main__':
    unittest.main()
