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

# 如果此模块被导入引入的话，那么这个模块内的__name__值就是文件的名字（不带.py），如果不涉及模块导入的话，__name__的值就是"__main__".
print(__name__)
