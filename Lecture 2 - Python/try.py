import random


def add(x, y):
    return x+y


def addtwice(a, x, y):
    return a(a(x, y), a(x, y))


try:
    print(5/0)
except ZeroDivisionError:
    print("error")
    raise
