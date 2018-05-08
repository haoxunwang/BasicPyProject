#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2018/5/8 下午5:56
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

import math
import sys
from math import sqrt
import math as shuxue
import module_test

print('调用math.sqrt:\t', math.sqrt(2))
print('直接调用sqrt:\t', sqrt(2))
print('重命名调用shuxue.sqrt:\t', shuxue.sqrt(2))

# 添加advanced为模块查找路径
sys.path.append('/Users/haoxunwang/coding/python_projects/BasicPyProject/advanced')

module_test.m_t_pr()
print('使用module_test模块中的变量: ', module_test.name)
