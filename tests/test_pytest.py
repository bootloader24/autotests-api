def test_first_try():
    print("Hello World!")  # Для вывода print() в консоль добавляем к pytest параметр "-s"


def test_second_try():
    pass


class TestUserLogin:
    def test_one(self):
        pass

    def test_two(self):
        pass


def test_assert_positive_case():
    assert (2 + 2) == 4  # Ожидается, что тест пройдет
    assert (2 + 3) == 5  # В тесте может быть несколько assert'ов
    assert (2 + 4) == 6


def test_assert_negative_case():
    assert (2 + 2) == 5, "Failed: 2 + 2 != 5"  # Тут должна быть ошибка
