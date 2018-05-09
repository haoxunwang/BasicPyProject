#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 在第一次导入包中的任何部分，就会执行"__init__.py"文件中的代码，其中的变量和函数等也会自动导入。
# @Time    : 2018/5/8 下午5:55
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

name = 'advanced'
print('__init__.py中输出：', name)

# 注意：在包定义文件定义__all__的列表变量，那么在使用from package import *的时候就会把这个列表中的所有名字作为包内容导入。
__all__ = ["module_test", "Package"]


def advanced_test_fun():
    print('advanced包中的方法advanced_test_fun')
