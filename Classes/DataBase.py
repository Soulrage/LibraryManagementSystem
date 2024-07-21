import json


class DataBase:
    def __init__(self):
        self.file_path = "books.json"
        self._data = {}
        self._open_file()

    def get_all_books(self):
        return self._data

    def get_new_id(self) -> str:
        return str(max(map(int, self._data.keys()), default=0) + 1)

    def add_book(self, data_book: dict):
        new_id = self.get_new_id()
        self._data[new_id] = data_book
        self._save_data()

    def search_books(self, search_criteria: dict) -> list:
        matching_books = []
        for id, book in self._data.items():
            matches_all_criteria = all(book.get(key) == value for key, value in search_criteria.items())
            if matches_all_criteria:
                matching_books.append({id: book})
        return matching_books

    def delete_book(self, id: str) -> str:
        if id in self._data:
            self._data.pop(id)
            self._save_data()
            return "книга успешно удалена"
        else:
            return "книги под таким ID нет"

    def change_status(self, id: str, status: str) -> str:
        if id in self._data:
            self._data[id]["status"] = status
            self._save_data()
            return "статус успешно изменен"
        else:
            return "книги под таким ID нет"

    def _open_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self._data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self._data = {}
            self._save_data()

    def _save_data(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self._data, file, indent=4, ensure_ascii=False)
