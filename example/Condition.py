#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2018/4/27 下午2:58
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
dog.py
'''

'''
age = int(input('Please input your dog age: '))
print("")
if age < 0:
    print('Are you kidding me?')
elif age == 1:
    print('equals to 14 same with people')
elif age == 2:
    print('equals to 22 same with people')
elif age > 2:
    human = 22 + (age - 2) * 5
    print('equals to %d same with people' % human)
    
input('click enter to exit')

'''

'''
guess number
'''

'''
number = 7
guess = -1
print('Guess Number Game')
while guess != number:
    guess = int(input('please input your guess number: '))

    if guess == number:
        print('congratulate to you')
    elif guess < number:
        print('Your number is small...')
    elif guess > number:
        print('Your number is big...')
'''

'''
2和3整除
'''

num = int(input('input a number: '))
if num % 2 == 0:
    if num % 3 == 0:
        print('你输入的数字可以整除2和3')
    else:
        print('你输入的数字可以整除2，但不能整除3')
else:
    if num % 3 == 0:
        print('你输入的数字可以整除3，但不能整除2')
    else:
        print('你输入的数字不可以整除2和3')
