import pytest


# Фикстура для очистки данных из базы данных
@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из базы данных")


# Фикстура для заполнения данных в базу данных
@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Создаем новые данные в базе данных")

# Если не нужно возвращать какой-то объект, то используем декоратор usefixtures.
@pytest.mark.usefixtures('fill_books_database') # Использование для теста
def test_read_all_books_in_library():
    ...


@pytest.mark.usefixtures(
    'clear_books_database',
    'fill_books_database'
) # Использование для класса
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...
