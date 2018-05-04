#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2018/4/27 下午2:47
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
Fibonacci series: 斐波那契数列
两个元素的总和确定了下一个数
'''

a, b = 0, 1
while b < 1000:
    # end关键字可用于将结果输出到同一行
    print(b, end=',')
    a, b = b, a + b
