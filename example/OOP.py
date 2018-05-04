#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : OOP PROGRAM
# @Time    : 2018/5/4 上午11:18
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
class TestClass:
    """一个简单的类实例"""

    def prt(self):
        print(self)
        print(self.__class__)


t = TestClass()
t.prt()
'''


class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("%s say: I %d years old." & (self.name, self.age))


class student(people):
    grade = ''

    def __init__(self, name, age, weight, grade):
        people.__init__(self, name, age, weight)
        self.grade = grade

    def speak(self):
        print("%s say: I %d years old,I am reading %d grade." % (self.name, self.age, self.grade))


class speaker():
    topic = ''
    name = ''

    def __init__(self, name, topic):
        self.name = name
        self.topic = topic

    def speak(self):
        print('I am %s, i am a speaker,the talk of speak is %s.' % (self.name, self.topic))


class sample(speaker, student):
    age = ''

    def __init__(self, name, age, weight, grade, topic):
        student.__init__(self, name, age, weight, grade)
        speaker.__init__(self, name, topic)


# s = student('Nelson', 25, 60, 4)
# s.speak()

t = sample('Nelson', 25, 60, 4, 'Python')
t.speak()


class Parent:
    def myMethod(self):
        print('call parent method')


class Child(Parent):
    def myMethod(self):
        print('call child method')


c = Child()
c.myMethod()
super(Child, c).myMethod()


class JustCounter:
    __secretCounter = 0
    publicCount = 0

    def count(self):
        self.__secretCounter += 1
        self.publicCount += 1
        print(self.__secretCounter)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)


# AttributeError: 'JustCounter' object has no attribute '__secretCounter'
# print(counter.__secretCounter)

class Site:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def who(self):
        print('name: ', self.name)
        print('url: ', self.url)

    def __foo(self):
        print("This is private method.")

    def foo(self):
        print("This is public method.")
        self.__foo()


s = Site('菜鸟网络', 'www.runoob.com')
s.who()
s.foo()

# AttributeError: 'Site' object has no attribute '__foo'
# s.__foo()

'''
类的专有方法：__add__
'''


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
# Vector(7, 8)
print(v1 + v2)
