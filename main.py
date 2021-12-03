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
# else:
        