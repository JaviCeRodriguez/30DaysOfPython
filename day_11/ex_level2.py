# 1.
def evens_and_odds(num):
    evens = 0
    odds = 0

    for n in range(num + 1):
        if n % 2 == 0:
            odds += 1
        else:
            evens += 1

    print(f'The number of odds are {odds}')
    print(f'The number of evens are {evens}')


# 2.
def factorial(num):
    factorial_num = 1
    if num == 0:
        return 0

    for n in range(1, num + 1):
        factorial_num += n
    return factorial_num


# 3.
