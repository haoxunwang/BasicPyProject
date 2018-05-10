#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : decorator 装饰器
# @Time    : 2018/5/10 上午10:49
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''装饰函数'''
'''
def abc(fun):
    def wrapper(*args, **kwargs):
        print('开始运行...')
        fun(*args, **kwargs)
        print('运行结束！')

    return wrapper


@abc
def demo_decoration(x):
    a = []
    for i in range(x):
        a.append(i)
    print(a)


@abc
def hello(name):
    print('Hello ', name)


if __name__ == '__main__':
    demo_decoration(5)
    print()
    hello('Nelson')
'''

'''装饰类'''


def abc(myclass):
    class InnerClass:
        def __init__(self, z=0):
            self.z = 0
            self.wrapper = myclass()

        def position(self):
            self.wrapper.position()
            print('z axis: ', self.z)

    return InnerClass


@abc
class coordination:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def position(self):
        print('x axis: ', self.x)
        print('y axis: ', self.y)


if __name__ == '__main__':
    coor = coordination()
    coor.position()
