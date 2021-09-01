# Day 2: 30 Days of python programming

# Level 1
# 1. to 13
first_name, last_name = 'Javier', 'Rodriguez'
full_name = 'Javier Rodriguez'
country, city = 'Argentina', 'San Fernando'
year = 25
is_married = False
is_true = True
is_light_on = True

# Level 2
# 1.
print(f'El tipo de {first_name.__repr__()} es: {type(first_name)}')
print(f'El tipo de {last_name.__repr__()} es: {type(last_name)}')
print(f'El tipo de {full_name.__repr__()} es: {type(full_name)}')
print(f'El tipo de {country.__repr__()} es: {type(country)}')
print(f'El tipo de {city.__repr__()} es: {type(city)}')
print(f'El tipo de {year.__repr__()} es: {type(year)}')
print(f'El tipo de {is_married.__repr__()} es: {type(is_married)}')
print(f'El tipo de {is_true.__repr__()} es: {type(is_true)}')
print(f'El tipo de {is_light_on.__repr__()} es: {type(is_light_on)}')

# 2.
print(f'El largo de first_name es {len(first_name)}')

# 3.
print(f'Es el mismo largo first_name y last_name? {len(first_name) == len(last_name)}')

# 4.
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

# 5.
radius = float(input('Give me radius of circle: '))
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2 * 3.14 * radius
print(round(area_of_circle, 2), round(circum_of_circle, 2))

# 6.
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
age = int(input('And age? '))
print(f'{first_name} {last_name} have {age} years old!')