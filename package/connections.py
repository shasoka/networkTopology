"""
Функция, проверяющая, к какому типу неполносвязных сетей принадлежит данная
сеть.

Шенберг Аркадий Алексеевич. КИ21-17/1Б. Практическая работа 5. Вариант 11.
"""

from enum import Enum


def connection_type(apexes: int, edges: int, links: list) -> int:
    """
    Функция, определяющая тип неполносвязной сети.
    1 - шина, 2 - кольцо, 3 - звезда, 4 - неопознанный тип.
    """

    # 5 4 0 1 1 2 2 3 3 4 - шина
    # 5 5 0 1 1 2 2 3 3 4 0 4 - кольцо
    # 5 4 1 0 2 0 0 3 4 0 - звезда
    # 5 5 0 1 1 2 2 3 3 4 4 1 - неопознанный тип

    class ConnectionType(Enum):
        """
        Enum перечисление возможных вариантов.
        """
        tire = 1
        ring = 2
        star = 3
        unrecognized = 4

    if apexes == edges:
        k = 0
        for i in range(1, apexes):
            if (i-1, i) in links:
                k += 1
            else:
                k = 0
                break
        if k == edges - 1 and (0, apexes - 1) in links:
            return ConnectionType.ring.value
        else:
            return ConnectionType.unrecognized.value
    elif apexes == edges + 1:
        is_star = False
        for i in range(apexes):
            flag = 0
            for j in range(len(links)):
                if i in links[j]:
                    flag += 1
                else:
                    flag = 0
                    break
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
                else:
                    t = 0
                    break
            if t == edges:
                return ConnectionType.tire.value
            else:
                return ConnectionType.unrecognized.value
