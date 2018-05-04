#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2018/4/28 下午4:03
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''

def area(width, height):
    "Simple Function demo"
    return width * height


w = 4
h = 5
print('width = ', w, ' height = ', h, " area = ", area(w, h))
'''

'''
参数传递不可变对象实例
'''

'''
def changeInt(a):
    a = 10


b = 2
changeInt(b)
print(b)
'''

'''
参数传递可变实例
'''

'''
def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print('函数内取值：', mylist)
    return


mylist = [10, 20, 30]
changeme(mylist)
print('函数外取值：', mylist)
'''

'''
关键参数 & 默认参数
'''

'''

def printInfo(name, age=35):
    print('name: ', name)
    print('age: ', age)
    return


printInfo(age=1, name='nelson')
printInfo('jolly')

'''

'''
不定长参数
'''

'''
def printInfo(arg1, *vartuple):
    "打印任何传入的参数"
    print('first param: ', arg1)
    print('output tuple: ')
    for var in vartuple:
        print(var)
    return


printInfo(10)
printInfo(70, 60, 50)
'''

'''
匿名函数，主体是一个表达式，而不是一个代码块
'''

'''
sum = lambda arg1, arg2: arg1 + arg2

print('sum is : ', sum(10, 20))
print('sum is : ', sum(20, 20))
'''

'''
变量作用域 L->E->G->B
'''

'''
x = int(2.9)  # 内建作用域
g_count = 0  # 全局作用域


def outer():
    o_count = 1  # 闭包函数外的函数中

    def inner():
        i_count = 2  # 局部作用域
'''

'''
Python中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如if/elif/else、try/except、for/while等）是不会引入新的作用域的
'''
'''
if True:
    msg = 'I am from Runoob'

print(msg)
'''

'''
global和nonlocal关键字
'''

'''
num = 1

def fun1():
    global num
    print(num)
    num = 123
    print(num)


fun1()

def outer():
    num = 10

    def inner():
        nonlocal num
        num = 100
        print(num)

    inner()
    print(num)


outer()
'''

a = 10

def test():
    # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
    a = a + 1
    print(a)


test()
