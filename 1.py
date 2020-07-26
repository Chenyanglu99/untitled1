import math
import os

from functools import reduce
from collections import Iterable


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("'bad operand type'")
    if x > 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


r = move(100, 100, 60, math.pi / 6)

# print(my_abs('-A'))

print(r)


def eroll(name, gender, age=6, city='Beijing'):
    print('name: ', name)
    print('gender: ', gender)
    print('age: ', age)
    print('city: ', city)


eroll('Sarah', 'F')
print('\n')
eroll('Bob', 'M', 7)
print('\n')
eroll('Adam', 'F', city='Tianjin')


def add_end(L=None):
    if L is None:
        L = ['null']
    L.append('end')
    return L


print(add_end())
print(add_end())
print(add_end())


def calc(numbers):
    sum = 0
    for x in numbers:
        sum += x * x
    return sum


print(calc([1, 2, 3]))


def calc2(*numbers):
    sum = 0
    for x in numbers:
        sum += x * x
    return sum


print(calc2(1, 2, 3))

num = [1, 2, 3]

print(calc2(*num))


# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)

def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)


# person('aaa', 21, city='Beijing', love=0)
#
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('jack', 24, **extra)


# 命名关键字参数

def person(name, age, *, city, job):
    print(name, age, city, job)


person('jack', 24, city='Beijing', job='Engineer')


# 递归函数
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(6))

# 解决递归调用栈溢出的方法是通过尾递归优化


# def fact(n):
#     return fact_iter(n, 1)
#
#
# def fact_iter(Snum1, product):
#     if Snum1 == 1:
#         return product
#     return fact_iter(Snum1 - 1, Snum1 * product)
#
#
# print(fact(100000))

# 利用切片操作，实现一个trim()函数，去除字符串首尾
# 的空格，注意不要调用str的strip()方法：
# def trim(s):
#     if s[0] == ' ':
#         s1 = s[1:]
#         if s1[-1] == ' ':
#             s2 = s1[:-2]
#         else:
#             s2 = s1
#     else:
#         if s[-1] == ' ':
#             s2 = s[:-2]
#         else:
#             s2 = s
#     return s2

def trim(s):
    if 0 == len(s):
        return s
    while ' ' == s[0]:
        s = s[1:]
        if 0 == len(s):
            return s
    while ' ' == s[-1]:
        s = s[:-1]
        if 0 == len(s):
            return s
    return s


if trim('hello  ') != 'hello':
    print('1测试失败!')
elif trim('  hello') != 'hello':
    print('2测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('3测试失败!')
elif trim('') != '':
    print('4测试失败!')
elif trim('    ') != '':
    print('5测试失败!')
else:
    print('测试成功!')

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

print('value')
for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

list(range(1, 11))
L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])

[d for d in os.listdir('.')]  # os.listdir可以列出文件和目录
print(d)
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

L = ['hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

g = (x * x for x in range(10))
print(g)

for n in g:
    print(n)


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'


# print(fib(9))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for n in fib(6):
    print(n)
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 杨辉三角定义如下：
# generator输出杨辉三角
#
# def add(x, y):
#     return x + y
#
#
# print(reduce(add, [1, 3, 5, 7, 9]))
#
#
# def fn(x, y):
#     return x * 10 + y
#
#
# print(reduce(fn, [1, 3, 5, 7, 9]))
#
# print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6])))


# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    # def fn(x, y):
    #     return x * 10 + y
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#
#     def char2num(s):
#         return DIGITS[s]
#
#     return reduce(fn, map(char2num, s))


print(str2int('13579'))


class Calculator:
    name = 'Good calculator'
    price = 18

    def __init__(self, price, name, height, width, weigt):
        self.name = name
        self.price = price
        self.h = height
        self.wi = width
        self.we = weigt

    def add(self, x, y):
        print(self.name)
        result = x + y
        print(result)

    def minus(self, x, y):
        result = x - y
        print(result)

    def times(self, x, y):
        print(x * y)

    def divide(self, x, y):
        print(x / y)


calcul = Calculator('a', 'a', 12, 12, 2)

print(calcul.name)
