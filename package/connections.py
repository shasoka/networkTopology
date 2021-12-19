"""
Функция, проверяющая, к какому типу неполносвязных сетей принадлежит данная
сеть.

Шенберг Аркадий Алексеевич. КИ21-17/1Б. Практическая работа 6. Вариант 11.

Функции:
---------
connection_type:
    Аргументы:
        apexes: int, число вершин сети;
        edges: int, число ребер сети;
        links: list, списко пар связей сети;

        return: int/None.

    В теле функции описан класс ConnectionType. Это класс, атрибуты которого
        - целые числа, соответсвующие типам сети.
"""

from enum import Enum


def connection_type(apexes: int, edges: int, links: list) -> int:
    """
    Функция, определяющая тип неполносвязной сети.

    :param apexes: int, число вершин сети;
    :param edges: int, число ребер сети;
    :param links: list, списко пар связей сети;
    :return int/None, 1 - шина, 2 - кольцо, 3 - звезда, None - неопознанный
        тип.
    """

    # 5 4 0 1 1 2 2 3 3 4 - шина
    # 5 5 0 1 1 2 2 3 3 4 0 4 - кольцо
    # 5 4 1 0 2 0 0 3 4 0 - звезда
    # 5 5 0 1 1 2 2 3 3 4 4 1 - неопознанный тип

    class ConnectionType(Enum):
        """
        Класс, атрибуты которого - целые числа, соответсвующие типам сети.

        Атрибуты:
        ---------
        tire: int
            Тип Шина.
        ring:
            Тип Кольцо.
        star:
            Тип Звезда.
        """

        tire = 1
        ring = 2
        star = 3

    if apexes == edges:
        k = 0
        for i in range(1, apexes):
            if (i-1, i) in links:
                k += 1
        if k == edges - 1 and (0, apexes - 1) in links:
            return ConnectionType.ring.value
    elif apexes == edges + 1:
        is_star = False
        for i in range(apexes):
            flag = 0
            for j in range(len(links)):
                if i in links[j]:
                    flag += 1
            if flag == edges:
                is_star = True
                break
        if is_star is True:
            return ConnectionType.star.value
        else:
            t = 0
            for i in range(1, apexes):
                if (i - 1, i) in links:
                    t += 1
            if t == edges:
                return ConnectionType.tire.value
