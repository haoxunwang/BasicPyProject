#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    :
# @Time    : 2018/4/27 下午5:09
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
1+2+...+100之和
'''

'''
n = 100
sum = 0
counter = 1
while counter <= n:
    sum += counter
    counter += 1
print('1 to %d sum is: %d' % (n, sum))
'''

'''
无限循环
'''

'''
var = 1
while var == 1:
    num = int(input('input a number: '))
    print('you input numner is: ', num)
print('Good bye!')
'''

'''
for 语句
'''

'''
languages = ['C', 'C++', 'Perl', 'Python']
for x in languages:
    print(x)
'''

'''
range()函数
'''

'''
for i in range(0, 10, 3):
    print(i)

for i in range(-10, -100, -30):
    print(i)

a = ['Google', 'Runoob', 'Facebook', 'Medium']
for i in range(len(a)):
    print(i, a[i])

print(list(range(5)))


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
        else:
            # 'not found result'
            print(n, ' 是质数')
'''

'''
pass语句
'''

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('execute pass code block')
    print('current letter: %c' % letter)
    print("That's all")
