"""Шенберг Аркадий Алексеевич. КИ21-17/1Б. Практическая работа 4. Вариант 8"""

import argparse
import itertools
from enum import Enum


def is_full_connected(apexes, edges, links):
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


def connection_type(apexes, edges, links):
    """
    Функция, определяющая тип неполносвязной сети.
    1 - шина, 2 - кольцо, 3 - звезда.
    """

    class ConnectionType(Enum):
        """
        Enum перечисление возможных вариантов.
        """
        tire = 1
        ring = 2
        star = 3

    if apexes == edges:
        return ConnectionType.ring.value
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


CLI = argparse.ArgumentParser(description='Данная программа умеет определять '
                                          'топологический тип сети')
CLI.add_argument('v', type=int, help='Количество вершин сети')
CLI.add_argument('r', type=int, help='Количество ребер сети')
CLI.add_argument("links", type=int, nargs='*',
                 help='Вводимый список связей между вершинами: V1 V2 V1 V3 Vi'
                      ' Vj ... Вершины нумеруются с 0.')
args = CLI.parse_args()

if args.v <= 4 or args.r <= 3:
    CLI.error('Неверный ввод. Число вершин должно быть больше 4, ребер - '
              'больше 3.')

if args.r > len(list(itertools.combinations(range(args.v), 2))):
    CLI.error('Неверный ввод числа ребер. Ребер больше, чем может '
              'существовать в данной системе.')

if len(args.links) % 2 != 0:
    CLI.error('Неверный ввод координат связей. Нечетное число координат.')

if len(args.links) / 2 != args.r:
    CLI.error('Неверный ввод. Число ребер не совпадает с количеством пар '
              'связей')

for i in range(len(args.links)):
    if args.links[i] >= args.v:
        CLI.error(f'Неверный ввод координат связей. Вершины с координатой '
                  f'{args.links[i]} в заданной системе не существует.')

args.links = list(zip(*[iter(args.links)] * 2))
args.links = list(map(lambda x: tuple(sorted(x)), args.links))

if is_full_connected(args.v, args.r, args.links):
    print('Сеть полносвязная.')
    quit()
else:
    temp = connection_type(args.v, args.r, args.links)
    if temp == 1:
        print('Неполносвязная сеть типа "шина"')
        quit()
    if temp == 2:
        print('Неполносвязная сеть типа "кольцо"')
        quit()
    if temp == 3:
        print('Неполносвязная сеть типа "звезда"')
        quit()
