# 1.
score = int(input('What is the score? '))

if 80 <= score <= 100:
    print('Grade A')
elif 70 <= score <= 89:
    print('Grade B')
elif 60 <= score <= 69:
    print('Grade C')
elif 50 <= score <= 59:
    print('Grade D')
elif 0 <= score <= 49:
    print('Grade F')
else:
    print('Incorrect score')


# 2.
month = input('Insert month: ')

if month in ['September', 'October', 'November']:
    print('Autumn!')
elif month in ['December', 'January', 'February']:
    print('Winter!')
elif month in ['March', 'April', 'May']:
    print('Spring!')
elif month in ['June', 'July', 'August']:
    print('Summer!')
else:
    print('Incorrect month!')

# 3.
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('What is your favourite fruit? ')

print('Esta en la lista!') if fruit in fruits else print('No la tenia! La agrego')
