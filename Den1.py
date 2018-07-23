import random
import pygame as pg

a = enumerate([i for i in range(1, 10)])
print(list(enumerate([i for i in range(1, 10)])))
b = [(str(x) * 3) + (str(y) * 3) for x, y in a]
print(b, end='\n\n--------------------------------------------------------------\n\n')


class Wow:
    def __init__(self, x):
        self.x = x

    def __add__(self, y):
        return Wow(self.x - y.x)

    def __sub__(self, y):
        return Wow(self.x + y.x)

    def __repr__(self):
        return str(self.x)


a = Wow(5)
b = Wow(7)
c = Wow(3)
print(a - b + c, end='\n\n--------------------------------------------------------------\n\n')


def apply_twice(func, arg):
    return func(func(arg))


def add_10(x):
    return x - 44


print(abs(apply_twice(add_10, -44)), end='\n\n--------------------------------------------------------------\n\n')


def f(x):
    d = []
    for i in range(x):
        y = i + 2
        d.append(y)
    return d


z = 3
w = f(z)
print(sum(w), end='\n\n--------------------------------------------------------------\n\n')


def generator(n):
    i = n
    while i >= 0:
        if i % 3 == 0:
            yield i * i
        i -= 1


for k in generator(6):
    print(k, sep='', end=' ')
print(end='\n\n--------------------------------------------------------------\n\n')


def foo(**b):
    return b


c = foo(nm=4, nn=5)
print(c, end='\n\n--------------------------------------------------------------\n\n')

ages = [99, 11, 18, 75, 99]
p = ages.count(99) - ages.count(11)
print(p, end='\n\n--------------------------------------------------------------\n\n')

x = [0, [2, 4, 6], [13, 11, 9]]
y = x[2] + x[1] * 2
print(y)
print(y[x[1][0]], end='\n\n--------------------------------------------------------------\n\n')

Word = [["N", "D"], "K"]
Word[0][0] = "Nastya"
Word[0][1] = "Denis"
Word[1] = "Kolya"
print(Word, end='\n\n--------------------------------------------------------------\n\n')

a = random.randint(6, 8)
print (type(a))
print(a + 1000000, end='\n\n--------------------------------------------------------------\n\n')

pairs = [(x, x ** 2) for x in range(1, 5)]
print(pairs[2][1], end='\n\n--------------------------------------------------------------\n\n')

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
set1.add(7)
set2.add(10)
print(set1)
print(set2)
print(len(set1 ^ set2), end='\n\n--------------------------------------------------------------\n\n')

while True:
    for n in range(10):
        pass
    break
print(n, end='\n\n--------------------------------------------------------------\n\n')

num = [10]
print(num * 2, end='\n\n--------------------------------------------------------------\n\n')

a = [8, -1, 3]
a.sort()
print(a)


def den1(a, b, c):
    x = a + b + c
    return x


print(den1(1, 2, 3), end='\n\n--------------------------------------------------------------\n\n')


class Family:
    def printmembers(self, ss):
        prtext = ''
        allnum = 0
        inum = 0
        jnum = 0
        for i in ss:
            for j in i:
                print(ss[inum][jnum])
                allnum += 1
                prtext += j
                if jnum == 0:
                    prtext += ' - '
                jnum += 1
            if allnum == len(ss) * 2:
                prtext += '.'
            else:
                prtext += ', '
            inum += 1
            jnum = 0
        print(prtext, end='\n\n--------------------------------------------------------------\n\n')


VyazFamily = Family()
vyazmembers = [['папа', 'Денис'], ['мама', 'Катя'], ['сын', 'Елисей']]
VyazFamily.printmembers(vyazmembers)


class Family2:
    def printmembers2(self, **ss):
        less = list(enumerate(ss, 1))
        print(less)
        for i in list(ss):
            print("{0} - {1}".format(i, ss[i]))


VyazFamily2 = Family2()
vyazmembers2 = {"папа": "Денис", "мама": "Катя", "сын": "Елисей"}
VyazFamily2.printmembers2(**vyazmembers2)

import pyglet
from pyglet.window import mouse

window = pyglet.window.Window()

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')

@window.event
def on_draw():
    window.clear()

pyglet.app.run()

