from functools import reduce


def miLista(lista):
    res = list(filter((lambda x : x % 2), lista))
    print(res)
    res = reduce((lambda x,y : x+y), res)
    print(res)

lista = list(range(50))

miLista(lista)