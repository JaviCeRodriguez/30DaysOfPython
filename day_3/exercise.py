# 1. to 3.
age = 25
height_user = 170.2
comp = 1 + 1j

# 4.
base = float(input('Enter base: '))
height = float(input('Enter height: '))
print(f'The area of the triangle is {(base * height) / 2}')

# 5.
a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))
print(f'The perimeter of the triangle is {a + b + c}')

# 6.
rect_length = float(input('Enter length of rectangle: '))
rect_width = float(input('Enter width of rectangle: '))
rect_area = rect_width * rect_length
rect_per = 2 * (rect_width + rect_length)
print(f'The area of the rectangle is {rect_area} and the perimeter is {rect_per}')

# 7.
circle_radius = float(input('Enter radius of circle: '))
pi = 3.14
circle_area = pi * (circle_radius ** 2)
circle_circ = 2 * pi * circle_radius
print(f'The area and circumference of circle is {circle_area} and {circle_circ}, respectively')

# 8.
# Ecuation: y = 2x-2
slope = 2  # y = (m * x) - 2
x_intercept = 2/2  # y = 0
y_intercept = -2  # x = 0

# 9.
# slope: m = (y2 - y1) / (x2 - x1)
(x1, y1) = (2, 2)
(x2, y2) = (6, 10)
slope_def = (y2 - y1) / (x2 - x1)
dist_euclidean = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# 10.
print(f'If the same slope in 8 and 9? {slope == slope_def}')

# 11.
# Ecuation: y = (x ** 2) + (6 * x) + 8
a, b, c = 1, 6, 9
root = b ** 2 - 4 * a * c
x1 = (- b + root ** 0.5) / (2 * a)
x2 = (- b - root ** 0.5) / (2 * a)

# 12.
print(f'python and dragon have same length? {len("python") == len("dragon")}')

# 13.
print(f'"on" in "python" and "dragon"? ', end="")
if 'on' in 'python' and 'on' in 'dragon':
    print(True)
else:
    print(False)

# 14.
frase = 'I hope this course is not full of jargon'
if 'jargon' in frase:
    print('"jargon" in "I hope this course is not full of jargon"')
else:
    print('"jargon" not in')

# 15.
print(f'"on" not in "python" and "dragon"? ', end="")
if 'on' in 'python' and 'on' in 'dragon':
    print(False)
else:
    print(True)

# 16.
print('Convert "python" length to string: ', str(float(len("python"))))

# 17.
if not (24 % 2):
    print(True)  # Even
else:
    print(False)  # Odd

# 18.
print('floor division of 7 by 3 is equal to the int converted value of 2.7')
print((7 // 3) == int(2.7))

# 19.
print("type of '10' is equal to type of 10")
print(type(10) == type('10'))

# 20.
print("int('9.8') is equal to 10")
# print(int('9.8') == 10) # O sea, no, pero no puedo comparar tipos distintos

# 21.
hours = int(input('Enter hours: '))
rate = int(input('Enter rate per hour: '))
print(f'Your weekly earning is {hours * rate}')

# 22.
years = int(input('Enter number of years you have lived: '))
print(f'You have lived for {years * 365 * 24 * 60 * 60} seconds.')

# 23.
for x in range(1, 6):
    print(x, end=' ')
    for exp in range(0, 4):
        print(x ** exp, end=' ')
    print('')
