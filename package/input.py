"""
Функция, проверяющая входные данные.

Шенберг Аркадий Алексеевич. КИ21-17/1Б. Практическая работа 5. Вариант 11.
"""

import itertools


def input_check(v: int, r: int, links_ori: list, parser):
    """
    Функция, проверяющая вводимые данные.

    :param v: int, число вершин;
    :param r: int, число ребер;
    :param links_ori: list, список пар связей;
    :param parser: argpasre.ArgumentParser, парсер аргументов.
    """

    links = list(zip(*[iter(links_ori)] * 2))
    links = list(map(lambda x: tuple(sorted(x)), links))

    # if v <= 4 or r <= 3:
    #     parser.error('Неверный ввод. Число вершин должно быть больше 4, ребер '
    #                  '- больше 3.')

    if r > len(list(itertools.combinations(range(v), 2))):
        parser.error('Неверный ввод числа ребер. Ребер больше, чем может '
                     'существовать в данной системе.')

    if len(links_ori) % 2 != 0:
        parser.error('Неверный ввод координат связей. Нечетное число '
                     'координат.')

    if len(links) != r:
        parser.error('Неверный ввод. Число ребер не совпадает с количеством '
                     'пар связей')

    for i in range(len(links)):
        if links_ori[i] >= v:
            parser.error(f'Неверный ввод координат связей. Вершины с '
                         f'координатой {links[i]} в заданной системе'
                         f' не существует.')
