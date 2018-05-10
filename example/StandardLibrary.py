#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : Standard Library
# @Time    : 2018/5/4 下午4:14
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me
import doctest
import glob
import math
import file
import random
import re
import shutil
import smtplib
import sys
import unittest
import zlib
from datetime import date, datetime
from timeit import Timer
from urllib.parse import urlencode
from urllib.request import urlopen, Request

'''
print(file.getcwd())
file.chdir('/BasicPyProject')
file.system('mkdir today')
'''

'''
print(dir(file))
print(help(file))
'''

'''
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')
'''

'''
print(glob.glob('*.py'))

print(sys.argv)
'''

'''
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
print('tea for too'.replace('too', 'two'))

print(math.cos(math.pi / 4))
print(math.log(1024, 2))
'''

'''
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(6))
'''

# open internet
'''
for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line = line.decode('utf-8')
    if 'EST' in line or 'EDT' in line:
        print(line)
'''

# send email
'''
server = smtplib.SMTP('localhost')
server.sendmail('nelson@gmai.com', 'nelson@163.com',
                """To:nelson@gmai.com
                From:nelson@gmail.com
                Beware the Ids of March.""")
server.quit()
'''

'''
now = date.today()
print(now)

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)
'''

'''
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s))
'''

'''
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())
'''

""" Unit Test"""

'''
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


doctest.testmod()


class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)


unittest.main()  # Calling from the command line invokes all tests
'''

# 处理get请求，不传data，则为get请求
url = 'http://www.xxx.com/login'
data = {"username": "admin", "password": 123456}
req_data = urlencode(data)
res = urlopen(url + '?' + req_data)
res = res.read().decode()
print(res)

# 处理post请求,如果传了data，则为post请求
url = 'http://www.xxx.com/login'
data = {"username": "admin", "password": 123456}
data = urlencode(data)
data = data.encode('ascii')
req_data = Request(url, data)
with urlopen(req_data) as res:
    res = res.read().decode()

print(res)
