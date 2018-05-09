#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 生成器，使用yield关键字定义函数对象，第一次调用生成器时不能传递给生成器None以外的值，否则会引发错误。
# @Time    : 2018/5/9 下午3:44
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''

def myYield(n):
    while n > 0:
        print('开始生成...')
        yield n
        print('完成一次...')
        n -= 1


if __name__ == '__main__':
    for i in myYield(4):
        print('遍历得到的值：', i)

    print()
    my_yield = myYield(3)
    print('已经实例化生成器对象')
    my_yield.__next__()
    print('第二次调用__next__()方法：')
    my_yield.__next__()

'''

'''
def myYield(n):
    while n > 0:
        rec = yield n
        n -= 1
        if rec is not None:
            # send()方法来重置生成器的生成序列
            n = rec


if __name__ == '__main__':
    my_yield = myYield(3)
    print(my_yield.__next__())
    print(my_yield.__next__())
    print('传给生成器一个值，重新初始化生成器。')
    print(my_yield.send(10))
    print(my_yield.__next__())
'''

''' 生产者与消费者模型 '''


def consumer():
    print('等待接受处理任务...')
    while True:
        # 生成器
        data = yield
        print('收到任务：', data)


def producer():
    c = consumer()
    c.__next__()
    for i in range(3):
        print('发送一个任务...', '任务%d' % i)
        # 任务通过调用生成器的send()函数实现
        c.send('任务%d' % i)


if __name__ == '__main__':
    producer()
