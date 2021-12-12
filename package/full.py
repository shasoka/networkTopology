"""
Функция, проверяющая полносвязность сети.

Шенберг Аркадий Алексеевич. КИ21-17/1Б. Практическая работа 5. Вариант 11.
"""

import itertools


def is_full_connected(apexes: int, edges: int, links: list) -> bool:
    """
    Функция, определяющая, является ли указанная сеть полносвязной.
    True в случае полносвязной; False - в противном случае.
    """

    # 5 10 0 1 0 2 0 3 0 4 1 2 1 3 1 4 2 3 2 4 3 4 - полносвязная

    full_connected = list(itertools.combinations(range(apexes), 2))

    if len(full_connected) == edges and set(full_connected) == set(links):
        return True
    else:
        return False
