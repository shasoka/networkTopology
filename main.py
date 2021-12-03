"""Шенберг Аркадий Алексеевич. КИ21-17/1Б. Практическая работа 4. Вариант 8"""

import argparse
import itertools


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


CLI = argparse.ArgumentParser(description='Данная программа умеет определять '
                                          'топологический тип сети')
CLI.add_argument('v', type=int, help='Количество вершин сети')
CLI.add_argument('r', type=int, help='Количество ребер сети')
CLI.add_argument("links", type=int, nargs='*',
                 help='Вводимый список связей между вершинами: V1 V2 V1 V3 Vi'
                      ' Vj ... Вершины нумеруются с 0.')
args = CLI.parse_args()

args.links = list(zip(*[iter(args.links)] * 2))
args.links = list(map(lambda x: tuple(sorted(x)), args.links))

if is_full_connected(args.v, args.r, args.links):
    print('Сеть полносвязная.')
    quit()
# else:
