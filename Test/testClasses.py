import pytest
from Classes.DataBase import DataBase
from Classes.Library import Library


@pytest.fixture(scope="module")
def db():
    return DataBase()


@pytest.fixture(scope="module")
def lib():
    return Library()


def test_added_book(db, lib):
    title = "Test Book"
    author = "Test Author"
    year = "2024"
    expected = f"{title} успешно добавлена"
    actual = lib.added_book(title, author, year)
    assert expected == actual


def test_delete_book(db, lib):
    title = "Test Book"
    author = "Test Author"
    year = "2024"
    book_id = int(db.get_new_id())-1
    lib.added_book(title, author, year)
    expected = "книга успешно удалена"
    actual = lib.delete_book(str(book_id))
    assert expected == actual


def test_change_status_book(db, lib):
    title = "Test Book"
    author = "Test Author"
    year = "2024"
    book_id = db.get_new_id()
    lib.added_book(title, author, year)
    status = "в наличии"
    expected = "статус успешно изменен"
    actual = lib.change_status_book(str(book_id), status)
    assert expected == actual


def test_get_all_books(db, lib):
    books = lib.get_all_books()
    assert isinstance(books, dict)


def test_search_book(db, lib):
    search_criteria = {"status": "в наличии"}
    result = lib.search_book(search_criteria)
    assert isinstance(result, list)