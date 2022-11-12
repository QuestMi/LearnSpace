# -*- coding: utf-8 -*-
"""
Create on : 2022/10/3
@Author   : Xiao QingLin
@File    : effective_python_code
"""
import itertools

"""
1-3 bytes 与 str
"""


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


"""
1-5 辅助函数取代复杂表达式
Don't Repeat Yourself
"""


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default


"""
1-6 unpacking 拆分
"""
snacks = [('a', 1), ('b', 2)]
for n, (name, calories) in enumerate(snacks, 1):
    print(f'{n}-{name}-{calories}')

"""
1-7 enumerate
enumerate能够把任何一种迭代器（iterator）封装成惰性生成器（lazy generator)
"""

"""
1-8 zip函数同时遍历两个迭代器
"""
# 两个迭代器长度相同
names = ['xql', 'xqq', 'xqs']
counts = [19, 20, 21]
for name, count in zip(names, counts):
    print(f'{name}-{count}')

# 两个迭代器长度不相同
from itertools import zip_longest

for name, count in zip_longest(names, counts):
    print(f'{name}-{count}')

"""
1-10 赋值表达式
海象运算符  a := b
"""


def pick_fruit():
    return {}


def make_juice(fruit, count):
    return fruit, count


bottles = []
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)

"""
2-11 序列做切片
实现 __getitem__ 与 __setitem__ 这两个特殊方法的类都可以切割
"""

"""
类型注解
"""
from typing import Dict, MutableMapping


def populate_ranks(votes: Dict[str, int], ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))


"""
2-17 defaultdict处理内部状态中缺失的元素
"""
visits = {
    'Mex': {'A', 'B'},
    'Japan': {'Kyoto'}
}

visits.setdefault('France', set()).add('Arles')

if (japan := visits.get('Japan')) is None:
    visits['Japan'] = japan = set()
japan.add('Kyoto')


class Visits:
    def __init__(self):
        self.data = {}

    def add(self, country, city):
        city_set = self.data.setdefault(country, set())
        city_set.add(city)


from collections import defaultdict


class Visits:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)


"""
3 函数 
"""


def careful_divide(a: float, b: float) -> float:
    """Divides a by b

    Raises:
        ValueError: When the inputs cannot be divided
    :param a:
    :param b:
    :return:
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')


"""
3-21 如何在闭包里使用外围作用域中的变量
"""

group = {2, 3, 5, 7}
numbers = [1, 3, 7, 2, 10]


class Sorter:
    def __init__(self, group):
        self.group = group
        self.fund = False

    def __call__(self, x):
        if x in self.group:
            self.fund = True
            return 0, x
        return 1, x


sorter = Sorter(group)
numbers.sort(key=sorter)

"""
3-26 用functools.wraps定义函数修饰器
"""

from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) -> {res!r}')
        return res

    return wrapper


def fib(n):
    if n in (0, 1):
        return n
    return fib(n - 2) + fib(n - 1)


"""
3-30
"""


def index_words(text):
    res = []
    if text:
        res.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            res.append(index + 1)
    return res


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


with open('address.txt', 'r') as f:
    it = index_file(f)
    res = itertools.islice(it, 0, 10)
    print(list(res))
