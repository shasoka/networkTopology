"""
Тесты для функции connection_type модуля connections.
"""

import pytest
from package.connections import connection_type


@pytest.fixture
def generate_for_tire():
    """
    Функция-фикстура. Результат данной функции служит входными данными для
    теста.
    """

    return 5, 4, [(0, 1), (1, 2), (2, 3), (3, 4)]


def test_tire(generate_for_tire):
    """
    Тест на принадлежность сети типу Шина.
    """

    assert connection_type(*generate_for_tire) == 1


def test_ring():
    """
    Тест на принадлежность сети типу Кольцо.
    """

    assert connection_type(5, 5, [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]) == 2


def test_star():
    """
    Тест на принадлежность сети типу Звезда.
    """

    assert connection_type(5, 4, [(0, 1), (0, 2), (0, 3), (0, 4)]) == 3


def test_unrecognized():
    """
    Тест на принадлежность сети типу Неопознанная.
    """

    assert connection_type(5, 5, [(0, 1), (1, 2), (2, 3), (3, 4), (1, 4)]) == 4


def test_unrecognized_odd():
    """
    Тест на принадлежность сети типу Неопознанная, частный случай.
    """

    assert connection_type(5, 2, [(0, 1), (3, 4)]) is None
