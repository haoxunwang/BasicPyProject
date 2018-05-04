#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : Input/Output
# @Time    : 2018/5/3 下午3:05
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me
import math

# s = 'Hello, Runoob'
# print(s)
# print(repr(s))
# print(str(1 / 7))
#
# x = 10 * 3.25
# y = 200 * 200
# s = 'x value is: ' + repr(x) + ', y value is: ' + repr(y) + '...'
# print(s)
#
# hello = 'hello, runoob\n'
# hellos = repr(hello)
# print(hellos)
#
# print(repr((x, y, ('Google', 'Apple'))))
#
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
#     print(repr(x * x * x).rjust(4))
#
# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
#
# print('12'.zfill(5))
# print('-3.14'.zfill(7))
# print('3.14159265359'.zfill(5))
#
# print('{}网址： "{}！"'.format('菜鸟教程', 'www.runoob.com'))
#
# print('{0} 和 {1}'.format('Google', 'Runoob'))
# print('{1} 和 {0}'.format('Google', 'Runoob'))
# print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
# print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
#
# print('常量 PI 的值近似为： {}。'.format(math.pi))
# print('常量 PI 的值近似为： {!r}。'.format(math.pi))
# print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
#
# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# for name, number in table.items():
#     print('{0:10} ==> {1:10d}'.format(name, number))
#
# print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
# print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
# print('常量 PI 的值近似为：%5.3f。' % math.pi)


# str = input("请输入：")
# print("你输入的内容是: ", str)
import pickle

'''
open & close file
'''

'''
f = open("/tmp/foo.txt", "w")
num = f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
value = ('www.runoob.com', 14)
s = str(value)
f.write(s)
str = f.read()
str = f.readline()
str = f.readlines()
for line in f:
    print(line, end='')

with open('tmp/foo.txt', 'r') as f:
    read_data = f.read()
print(f.closed)
f.seek(5)
f.seek(-3, 2)
print(str)
f.close()
'''

'''
pickle 模块
'''

data1 = {'a': [1, 2.0, 3, 4 + 6j], 'b': ('string', u'Unicode string'), 'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')
pickle.dump(data1, output)
pickle.dump(selfref_list, output, -1)
output.close()

pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
print(data1)

data2 = pickle.load(pkl_file)
print(data2)
pkl_file.close()
