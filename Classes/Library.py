from .DataBase import DataBase


class Library:
    def __init__(self):
        self._db = DataBase()

    def added_book(self, title: str, author: str, year: str) -> str:
        data_book = {
            "title": title,
            "author": author,
            "year": year,
            "status": "в наличии"
        }
        self._db.add_book(data_book)
        return f"{title} успешно добавлена"

    def delete_book(self, id: str) -> str:
        return self._db.delete_book(id)

    def search_book(self, search_criteria: dict) -> list:
        return self._db.search_books(search_criteria)

    def get_all_books(self) -> dict:
        return self._db.get_all_books()

    def change_status_book(self, id: str, status: str) -> str:
        return self._db.change_status(id, status)