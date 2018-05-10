#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : file system 文件与文件系统
# @Time    : 2018/5/10 下午4:46
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me


# open函数
'''
def file_hdl(name='python.txt'):
    f = open(name)
    res = 0
    i = 0
    for line in f:
        i += 1
        print('第%s行的数据为：' % line.strip(), line)
        res += int(line)

    print('这些数的和为：', res)
    f.close()


if __name__ == '__main__':
    file_hdl()
'''

# fileinput操作文件，对文件中行的懒惰迭代

'''
import fileinput


def demo_fileinput():
    with fileinput.input(['fpa.txt', 'fpb.txt']) as lines:
        for line in lines:
            print("总第%d行," % fileinput.lineno(), "文件%s中第%d行：" % (fileinput.filename(), fileinput.filelineno()))
            print(line.strip())


if __name__ == '__main__':
    demo_fileinput()
'''

# 常用文件和目录操作

# 由文件名批量获取姓名和考号

'''
import sys

print(sys.stdout)

import os

filenames = []

# os.walk()遍历当前目录后输出的格式为多个元组，每个元组的第一项为遍历的目录名(字符串)，第二项为遍历目录中的子目录列表，第三项为遍历目录中所有文件的列表
for a, b, files in os.walk('test/test'):
    # test/test [] ['周兰巧12.txt', '李文34.txt']
    print(a, b, files)
    if files:
        filenames.append([file[:-4] for file in files])

fname = 'testexam'
i = 0

for files in filenames:
    f = open(fname + str(i) + '.xls', 'w')
    for name in files:
        f.write(name[-2:] + '\t' + name[:-2] + '\n')

    f.close()
    i += 1
print('生成成功！')

'''

# 批量文件重命名
import os

perfix = 'Python'
length = 2
base = 1
format = 'mdb'


def PadLeft(str, num, padstr):
    '''
    将文件名补全到指定长度
    :param str: 要补全的字符
    :param num: 要达到的长度
    :param padstr: 未达到长度所添加的字符
    :return:
    '''
    stringlenghth = len(str)
    n = num - stringlenghth
    if n >= 0:
        str = padstr * n + str
    return str


print('the files in %s will be renamed.' % os.getcwd())
all_files = os.listdir(os.getcwd())
print([f for f in all_files if os.path.isfile(f)])
input = input('press y or Y to continue\n')
if input.lower() != 'y': exit()
filenames = os.listdir(os.curdir)

i = base - 1
for filename in filenames:
    i = i + 1
    if filename != 'rename.py' and os.path.isfile(filename):
        name = str(i)
        name = PadLeft(name, length, '0')
        t = filename.split('.')
        m = len(t)
        if format == '':  # 未指定文件类型，则更改当前目录中所有的文件
            os.rename(filename, perfix + name + '.' + t[m - 1])
        else:
            if t[m - 1] == format:
                os.rename(filename, perfix + name + '.' + t[m - 1])
            else:
                i = i - 1
    else:
        i = i - 1

all_files = os.listdir(os.getcwd())
print([f for f in all_files if os.path.isfile(f)])
