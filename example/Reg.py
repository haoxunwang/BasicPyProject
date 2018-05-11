#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : reg正则
# @Time    : 2018/5/4 下午6:21
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me
import re

print(re.match('www', 'www.runoob.com').span())
print(re.match('com', 'www.runoob.com'))

line = "Cats are smarter than dogs"
matchObject = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
print(matchObject.group())
print(matchObject.group(1))
print(matchObject.group(2))

phone = "2004-959-559 # 这是一个电话号码"
num = re.sub(r'#.*$', '', phone)
print('电话号码：', num)


# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
print(m)
m = pattern.match('one12twothree34four', 2, 10)  # 从'e'的位置开始匹配，没有匹配
print(m)
m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
print(m)  # 返回一个 Match 对象
m.group(0)  # 可省略 0
m.start(0)  # 可省略 0
m.end(0)  # 可省略 0
m.span(0)  # 可省略 0
