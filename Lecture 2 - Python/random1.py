import random


def my_random(x, y):
    lista = ["."*110]*100
    lista2 = [0]*100
    for i in range(3000):
        n = round(random.normalvariate(50, 13))
        lista2[n] += 1
    for i in range(99):
        lista[i] = lista[i][:lista2[i]]
        print(lista[i] + str(lista2[i]))


my_random(0, 99)
