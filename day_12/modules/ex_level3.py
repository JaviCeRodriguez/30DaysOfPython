import random


# 1.
def shuffle_list(lista):
    for i in range(len(lista) - 1, 0, -1):
        j = random.randint(0, i + 1)
        lista[i], lista[j] = lista[j], lista[i]
    return lista


# 2.
def unique_numbers():
    unique_list = []
    while len(unique_list) < 7:
        n = random.randint(0, 9)
        if n not in unique_list:
            unique_list.append(n)
    return unique_list
