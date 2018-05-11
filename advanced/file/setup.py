#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 编译为可执行文件
# @Time    : 2018/5/11 下午12:06
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

from distutils.core import setup
import py2exe

setup(console=['PackageTest.py'])
