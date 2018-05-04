#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 数据结构
# @Time    : 2018/4/28 下午5:09
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

from collections import deque

'''
列表
'''

'''
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(55.25), a.count('X'))

a.insert(2, -1)
a.append(333)
print(a)

print(a.index(333))
a.remove(333)
print(a)

a.reverse()
print(a)

a.sort()
print(a)
'''

'''
列表当堆栈
'''

'''
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)
'''

'''
列表当队列使用
'''

'''
queue = deque(["Eric", "John", "Michael"])
queue.append('Terry')
queue.append('Graham')
print(queue.popleft())
print(queue.popleft())

print(queue)

'''

'''
列表推导式
'''

'''
vec = [2, 4, 6]
list = [3 * x for x in vec]
print(list)

list = [[x, x ** 2] for x in vec]
print(list)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

list = [3 * x for x in vec if x > 3]
print(list)

list = [3 * x for x in vec if x < 2]
print(list)

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x * y for x in vec1 for y in vec2])

print([vec1[i] * vec2[i] for i in range(len(vec1))])
'''

'''
嵌套列表解析
'''

'''
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
'''

'''
del语句
'''

'''
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)

del a[:]
print(a)

del a
# NameError: name 'a' is not defined
print(a)
'''

'''
元组和序列
'''

'''
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)

'''

'''
集合
'''

'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)

print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
'''

'''
字典
'''
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])
del tel['sape']
print(tel)

print(list(tel.keys()))
print(sorted(tel.keys()))

dic = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dic)

dic = {x: x ** 2 for x in (2, 4, 6)}
print(dic)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
# 同时遍历2个或更多的序列
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
