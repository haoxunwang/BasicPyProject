#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : closure 闭包
# @Time    : 2018/5/10 下午2:35
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import contextlib

# 闭包
import random

'''
x = 14
def foo():
    x = 3

    def bar():
        print('x is %d' % x)

    # 调用嵌套的内层函数
    bar()


if __name__ == '__main__':
    foo()
'''

# 闭包与延迟求值

'''
def delay_fun(x, y):
    def caculator():
        return x + y

    return caculator


if __name__ == '__main__':
    print('返回一个求和的函数，并不求和。')
    sum = delay_fun(3, 4)
    print()
    print('调用并求和', sum())
'''

# 闭包与泛型函数（应用嵌套函数持有定义环境变量的特性来完成的）

'''
def line(a, b):
    def aline(x):
        return a * x + b

    return aline


if __name__ == '__main__':
    line23 = line(2, 3)
    line50 = line(5, 0)
    print(line23(4))
    print(line50(2))
'''

'''
上下文管理器，协议方法：
__enter__(self)
 __exit__(self,type,value,tb)
 
with context as var:
    pass
 
'''

# 自定义上下文管理器及其使用方法

'''
class FileMgr:

    def __init__(self, filename):
        self.filename = filename
        self.f = None

    def __enter__(self):
        self.f = open(self.filename, encoding='utf-8')
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.f:
            self.f.close()


if __name__ == '__main__':
    with FileMgr('Closure.py') as f:
        for line in f.readlines():
            print(line, end='')
'''

# 装饰器contextmanager实现一个上下文管理器

'''
@contextlib.contextmanager
def my_mgr(s, e):
    print(s)
    # yield后的表达值即为as后变量的值，在进入管理器时执行了yield语句之前的语句，退出with语句时，执行了yield语句之后的语句
    yield s + ' ' + e
    print(e)


if __name__ == '__main__':
    with my_mgr('start', 'end') as val:
        print(val)
'''

# 字符串操作对象属性

'''
class DemoClass:
    class_val = 3

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.info()

    def info(self):
        print('类属性class_val: ', DemoClass.class_val)
        print('实例属性x: ', self.x)
        print('实例属性y: ', self.y)


if __name__ == '__main__':
    dc = DemoClass()
    if hasattr(DemoClass, 'class_val'):
        setattr(DemoClass, 'class_val', 1000)
    if hasattr(dc, 'x'):
        setattr(dc, 'x', 'xxxxxxx')
        setattr(dc, 'y', 'yyyyyyy')
    dc.info()
    setattr(dc, 'z', 'zzzzzzzz')
    print('添加的属性z', dc.z)
'''

# 用字典构造分支程序

'''
def path_a():
    print('路径分支A')


def path_b():
    print('路径分支B')


def path_c():
    print('路径分支C')


if __name__ == '__main__':
    path_dict = {}
    path_dict['a'] = path_a
    path_dict['b'] = path_b
    path_dict['c'] = path_c
    paths = 'abc'
    for i in range(4):
        path = random.choice(paths)
        print('选择了路径：', path)
        path_dict[path]()
'''

# 重载类的特殊方法

'''
class Book:
    def __init__(self, name='Python 从入门到精通'):
        self.name = name

    def __add__(self, other):
        return self.name + ' add ' + other.name

    def __len__(self):
        return len(self.name)


if __name__ == '__main__':
    booka = Book()
    bookb = Book('Java 从入门到放弃')
    print('len(booka): ', len(booka))
    print('len(bookb): ', len(bookb))
    print(booka + bookb)
'''

# 鸭子类型（duck typing）与多态

"""
在Python面向对象的编程中，没有谈及多态，也不用定义接口。在Python语言中，调用是不用检查参数类型的，如果被调用的方法不存在，则会引发错误。
"""


class Duck:
    def __init__(self, name='duck'):
        self.name = name

    def quack(self):
        print('嘎嘎嘎...')


class Cat:
    def __init__(self, name='cat'):
        self.name = name

    def quack(self):
        print('喵喵喵...')


class Tree:
    def __init__(self, name='tree'):
        self.name = name


def duck_demo(obj):
    obj.quack()


if __name__ == '__main__':
    duck = Duck()
    cat = Cat()
    tree = Tree()
    duck_demo(duck)
    duck_demo(cat)
    duck_demo(tree)
