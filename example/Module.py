#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 模块
# @Time    : 2018/4/28 下午6:41
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me
# Filename: Package.py
import sys

if __name__ == '__main__':
    print('program is running self')
else:
    print("I am from another module!")

print('命令行参数如下：')
for i in sys.argv:
    print(i)

print('\nPython路径为：', sys.path, '\n')


def print_func(par):
    print("Hello : ", par)
    return
