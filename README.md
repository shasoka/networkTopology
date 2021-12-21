# **Пакет, решающий задачу о топологии сетей**
![](https://img.shields.io/github/watchers/shasoka/prac_6?style=social)
## **1. Структура проекта**
```
prac_6
|    \
|    |.gitignore
|    |README.md
|    |package
|    |   \
|    |   |__init__.py
|    |   |__main__.py
|    |   |full.py
|    |   |connections.py
|    |   |input.py
|    |   |tests
|    |   |    \   
|    |   |   |__init__.py
|    |   |   |test_connections.py
|    |   |   |test_full.py
```
## **2. Описание**
Пакет package предназачен для решения задачи "О топологии сетей" практической работы №4 по ВВПД (см. [Топология сетей](https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D1%82%D0%B5%D0%B2%D0%B0%D1%8F_%D1%82%D0%BE%D0%BF%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F)).

При вызове скрипта программа первым делом определит полносвязна ли сеть, а затем ее тип (если потребуется):

+ Полносвязная сеть
+ Неполносвязная сеть
  + Звезда
  + Шина
  + Кольцо
  + Иной тип 

Программа проверяет входные значения на корректность. Доступен вызов ```-h``` для вывода справки.
```
C:\ВАШ_ПУТЬ>python package -h
usage: package [-h] v r [links ...]

Данная программа умеет определять топологический тип сети

positional arguments:
  v           Количество вершин сети
  r           Количество ребер сети
  links       Вводимый список связей между вершинами: V1 V2 V1 V3 Vi Vj ... Вершины нумеруются с 0.

optional arguments:
  -h, --help  show this help message and exit
```
## **3. Пример использования**
### **3.1 Примеры запуска скрипта**
Полносвязная сеть:
```
C:\ВАШ_ПУТЬ>python package 5 10 0 1 0 2 0 3 0 4 1 2 1 3 1 4 2 3 2 4 3 4
Сеть полносвязная
```
Неполносвзяная сеть:
```
C:\ВАШ_ПУТЬ>python package 5 4 0 1 1 2 2 3 3 4
Неполносвязная сеть типа "Шина"
```
Пример некорректного вода:
```
C:\ВАШ_ПУТЬ>python package 5 10 0 1 0 2 0 3 0 4 1 2 1 3 1 4 2 3
usage: package [-h] v r [links ...]
package: error: Неверный ввод. Число ребер не совпадает с количеством пар связей
```
### **3.2 Примеры исходного кода**
Все функции модулей пакета доступны в репозитории. 

Логика программы довольно проста. Основные вычисления связаны с математическими понятиями сочетаний (см. [Сочетания](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%87%D0%B5%D1%82%D0%B0%D0%BD%D0%B8%D0%B5)). В исходном коде используется модуль ```itertools```.

Пример функции, вычисляющей тип неполносвязной сети:
```python
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
```
В соответсвии с практической работой №6 все функции имеют информативную строку документации (см. [Docstring](https://www.python.org/dev/peps/pep-0257/)).

**Спасибо. Удачи!** :no_mouth:


![asuka](https://en.memesrandom.com/wp-content/uploads/2021/02/cosplay-asuka-brasileira.jpg)
