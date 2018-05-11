#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 正则表达式元字符表
# @Time    : 2018/5/11 下午2:09
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import re

# str = 'http://nelsonblog.me'
# (http://www|www)\.[a-z0-9-]*\.[a-z]{2,3}

# search、match

'''
s = 'Life can be good'
print(re.match('can', s))
print(re.search('can', s))
print(re.match('l.*', s))
print(re.match('l.*', s, re.I))
print(re.findall('[a-z]{3}', s))
print(re.findall('[a-z]{1,3}', s))
'''

import re
import sys

'''
运用正则表达式分析并获取python程序中定义的所有方法和变量

分组扩展："(?P<组名>)" 来命名组名
    (?:...) 匹配但不捕获该匹配的子表达式，即它是一个非捕获匹配，不存储，供以后使用的匹配。
    (?#...) 表示注释
    (?=...) 表示如果"="后的内容在字符串中出现规则匹配，但不返回"="后的内容
    
'''


def DealWithFunc(s):
    r = re.compile(r'''
		(?<=def\s)
		\w+
		\(.*?\)
		(?=:)
		''', re.X | re.U)  # 设置编译选项，忽略模式中的注释
    return r.findall(s)


def DealWithVar(s):
    vars = []
    r = re.compile(r'''
		\b
		\w+
		(?=\s=)
		''', re.X | re.U)
    vars.extend(r.findall(s))
    r = re.compile(r'''
		(?<=for\s)
		\w+
		\s
		(?=in)
		''', re.X | re.U)
    vars.extend(r.findall(s))
    return vars


if len(sys.argv) == 1:
    sour = input('请输入要处理的文件路径：')
else:
    sour = sys.argv[1]
file = open(sour, encoding="utf-8")
s = file.readlines()
file.close()
print('********************************')
print(sour, '中的函数有：')
print('********************************')
i = 0
for line in s:
    i = i + 1
    function = DealWithFunc(line)
    if len(function) == 1:
        print('Line: ', i, '\t', function[0])
print('********************************')
print(sour, '中的变量有：')
print('********************************')
i = 0
for line in s:
    i = i + 1
    var = DealWithVar(line)
    if len(var) == 1:
        print('Line: ', i, '\t', var[0])
