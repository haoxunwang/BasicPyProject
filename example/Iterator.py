#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : Iterator & Generator
# @Time    : 2018/4/27 下午5:29
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me
import sys

'''
Iterator
'''

'''
list = list(range(1, 5))
it = iter(list)
for x in it:
    print(x, end=" ")

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
'''

'''
Generator
'''


# 使用了yield的函数被称为生成器 generator  <generator object fibonacci at 0x102211d58>
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)
print(f)
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
