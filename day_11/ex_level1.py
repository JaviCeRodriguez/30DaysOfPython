# 1.
def add_two_numbers(a, b):
    return a + b


# 2.
def area_of_circle(radio):
    return 3.14 * radio * radio


# 3.
def add_all_nums(*nums):
    suma = 0
    for num in nums:
        if type(num) == int or type(num) == float:
            suma += num
        else:
            return 'Che, no todos los elementos son números'
    return suma


# 4.
def convert_celsius_to_fahrenheit(temp):
    return temp * (9 / 5) + 32


# 5.
def check_season(month):
    if month in ['Diciembre', 'Enero', 'Febrero']:
        return 'Winter'
    if month in ['Marzo', 'Abril', 'Mayo']:
        return 'Spring'
    if month in ['Septiembre', 'Octubre', 'Noviembre']:
        return 'Autumn'
    if month in ['Junio', 'Julio', 'Agosto']:
        return 'Summer'


# 6. x e y son tuplas
def calculate_slope(x, y):
    """
    x e y, son tuplas, entonces: x = (2, 3), y = (5, 3)
    """
    slope = (y[1] - y[0]) / (x[1] - x[0])
    return slope


# 7.
def solve_quadratic_eqn(a: float, b: float, c: float, x: float) -> list[float]:
    """
    \- b +- sqrt(b**2 - 4 * a *c) / (2 * a)
    """
    sqrt = ((b ** 2) - (4 * a * c)) ** 1 / 2
    root1 = (- b + sqrt) / (2 * a)
    root2 = (- b - sqrt) / (2 * a)

    solution = (a * x ** 2) + (b * x) + c

    return [root1, root2, solution]


# 8.
def print_list(lista):
    for elem in lista:
        print(elem)


# 9.
def reverse_list(lista):
    rev_lista = list()
    for elem in lista:
        rev_lista = [elem] + rev_lista
    return rev_lista


# 10.
def capitalize_list_items(lista: list[str]):
    for n in range(len(lista)):
        lista[n] = lista[n].capitalize()
    return lista


# 11.
def add_item(lista: list, item):
    return lista + [item]


# 12.
def remove_item(lista: list, item):
    position = -1

    for i, elem in enumerate(lista):
        if elem == item:
            position = i

    if position == -1:
        return lista
    elif len(lista) == 1:
        return []
    elif lista[0] == item:
        return lista[1:]
    elif lista[-1] == item:
        return lista[:-1]
    else:
        return lista[:position] + lista[position + 1:]


# 13.
def sum_of_numbers(num):
    sum_total = 0
    for n in range(1, num + 1):
        sum_total += n
    return sum_total


# 14.
def sum_of_odds(num):
    odds = []
    for n in range(num +1):
        if n % 2:
            odds.append(n)
    return odds


# 15.
def sum_of_evens(num):
    evens = []
    for n in range(num +1):
        if not n % 2:
            evens.append(n)
    return evens
