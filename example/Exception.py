#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2018/5/3 下午5:55
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

# 10 * (1 / 0)
# '2' + 2

'''
while True:
    try:
        x = int(input('Please enter a number: '))
    except ValueError:
        print('Oops! That was no valid number. Try again ')
'''
import sys

'''
try:
    f = open('file.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print('Os error: {0}'.format(err))
except ValueError:
    print('Could not convert data to an integer.')
except:
    print('Unexpected error:', sys.exc_info()[0])
    raise
'''

'''
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
        raise  # 继续抛出去
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
'''


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result is ', result)
    finally:
        print('executing finally clause')


divide(2, 1)
divide(2, 0)
divide('2', '1')


def temp_convert(var):
    try:
        return int(var)
    except (ValueError) as Argument:
        print('参数中没有包含数字\n', Argument)


temp_convert('xyz')

for line in open('file.txt'):
    print(line, end="")

# 关键字with语句可以保证诸如文件之类的对象在使用完毕之后一定会正确的执行清理方法。
with open('file.txt') as f:
    for line in f:
        print(line, end="")


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    """Raised when an operation attempts a state transiton that's not allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


class MyError(Exception):

    def __int__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
