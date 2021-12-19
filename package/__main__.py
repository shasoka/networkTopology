"""
Точка входа программы.

Шенберг Аркадий Алексеевич. КИ21-17/1Б. Практическая работа 6. Вариант 11.

Функции:
---------
main:
    Функция, реализующая интерфейс командрой строки.
"""

import argparse
from input import input_check
from full import is_full_connected
from connections import connection_type


def main():
    """
    Функция, реализующая интерфейс командной строки.
    """

    parser = argparse.ArgumentParser(description='Данная программа умеет '
                                                 'определять топологический '
                                                 'тип сети')
    parser.add_argument('v', type=int, help='Количество вершин сети')
    parser.add_argument('r', type=int, help='Количество ребер сети')
    parser.add_argument("links", type=int, nargs='*',
                        help='Вводимый список связей между вершинами: '
                        'V1 V2 V1 V3 Vi Vj ... Вершины нумеруются с 0.')
    args = parser.parse_args()

    links_ready = input_check(args.v, args.r, args.links, parser)

    if is_full_connected(args.v, args.r, links_ready):
        print('Сеть полносвязная.')
        quit()
    else:
        connections = {1: 'Шина', 2: 'Кольцо', 3: 'Звезда',
                       None: 'Неопознанная'}
        print(f'Неполносвязная сеть типа '
              f'"{connections[connection_type(args.v, args.r, links_ready)]}"')


if __name__ == '__main__':
    main()
