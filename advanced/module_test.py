#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2018/5/8 下午6:07
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

print('导入测试模块的输出')

name = 'module_test'


def m_t_pr():
    print('module_test method: module_test')

# 独立运行的模块，需要将运行的程序段放入if __name__ == '__main__'中
if __name__ == '__main__':
    m_t_pr()
    print(name)
