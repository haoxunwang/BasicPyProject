#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 迭代器 Iterate
# @Time    : 2018/5/9 下午3:16
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
__iter__() 返回对象本身，是for语句使用迭代器的要求
__next__() 用于返回下一个元素或数据。当容器数据用尽时，会引发StopIteration异常

for item in iterator:
    pass
'''

''''
class MyIterator:
    def __init__(self, x=2, xmax=100):
        self.__mul, self.__x = x, x
        self.__xmax = xmax

    def __iter__(self):
        return self

    def __next__(self):
        if self.__x and self.__x != 1:
            self.__mul *= self.__x
            if self.__mul <= self.__xmax:
                return self.__mul
            else:
                raise StopIteration


if __name__ == '__main__':
    myIter = MyIterator()
    for i in myIter:
        print('迭代的数据元素为：', i)

'''


class Counter:
    def __init__(self, x=0):
        self.x = x


counter = Counter()


def used_iter():
    counter.x += 2
    return counter.x


for i in iter(used_iter, 8):
    print('本次遍历的数值：', i)
