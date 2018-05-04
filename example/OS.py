#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : OS 文件/目录方法
# @Time    : 2018/5/3 下午5:32
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
获取指定目录及其子目录下的py文件
路径说明：l 用于存储找到的 py 文件路径 get_py函数，递归查找并存储 py 文件路径于 l
'''
import os

'''
l = []


def get_py(path, l):
    fileList = os.listdir(path)
    for filename in fileList:
        pathTmp = os.path.join(path, filename)
        if os.path.isdir(pathTmp):
            get_py(pathTmp, l)
        elif filename[-3:].upper() == '.PY':
            l.append(pathTmp)


path = input('please input path: ').strip()
get_py(path, l)
print('在%s目录及其子目录下找到%d个py文件\n分别为：\n' % (path, len(l)))
for filepath in l:
    print(filepath + '\n')
'''

'''
显示所有视频格式文件, mp4,avi,rmvb
os.chdir(path) 改变当前工作目录

'''


def search_file(start_dir, target):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)
        if os.path.isdir(each_file):
            search_file(each_file, target)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录


start_dir = input('请输入待查找的初始目录：')
program_dir = os.getcwd()
target = ['.mp4', '.avi', '.rmvb']
vedio_list = []
search_file(start_dir, target)
f = open(program_dir + os.sep + 'vedioList.txt', 'w')
f.writelines(vedio_list)
f.close()
