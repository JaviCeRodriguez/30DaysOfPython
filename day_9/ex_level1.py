# 1.
age = int(input('Enter your age: '))

if age >= 18:
    print('You are old enough to drive.')
else:
    print('You need 3 more years to learn to drive.')


# 2.
my_age = int(input('Enter my age: '))
your_age = int(input('Enter your age: '))

age_diff = my_age - your_age

if age_diff == 1:
    print(f'You are {age_diff} year older than me.')
elif age_diff == 0:
    print('Same year older than me!.')
else:
    print(f'You are {age_diff} years older than me.')


# 3.
n1 = int(input('Enter number one: '))
n2 = int(input('Enter number two: '))

n_diff = n1 - n2

if n_diff == 0:
    print(f'{n1} is equal to {n2}')
elif n_diff > 0:
    print(f'{n1} is greater than {n2}')
else:
    print(f'{n2} is greater than {n1}')
