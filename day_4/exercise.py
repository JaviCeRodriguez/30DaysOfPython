# 1.
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')

# 2.
a, b, c = 'Coding', 'For', 'All'
print(f'{a} {b} {c}')

# 3.
company = 'Boke'
sentence = company + ' ' + a + ' ' + b + ' ' + c
print(f'{sentence}')

# 4.
print(company)

# 5.
print(len(company))

# 6.
print(company.upper())

# 7.
print(company.lower())

# 8.
p = a + ' ' + b + ' ' + c
print(p.capitalize())
print(p.title())
print(p.swapcase())
print(p.swapcase())

# 9.
print(p[:6])

# 10.
print(p.index(a))
print(p.find(a))

# 11.
print('Python' + p[6:])

# 12.
coso = 'Python For Everyone'
print(coso.replace('Python', 'All'))

# 13.
print(p.split(' '))

# 14.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

# 15.
print(p[0])  # C

# 16.
print(p[-1])  # l

# 17.
print(p[10])  # 2do espacio

# 18.
acronym_1 = [x for x in coso if x.isupper()]
print(''.join(acronym_1))

# 19.
acronym_2 = [x for x in p if x.isupper()]
print(''.join(acronym_2))

# 20.
print(p.index('C'))

# 21.
print(p.index('F'))

# 22.
print('Coding For All People'.rfind('l'))

# 23.
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

# 24.
print(sentence.rindex('because'))

# 25.
idx_1 = sentence.find('because')
idx_2 = sentence.rfind('because')
print(sentence[:idx_1 - 1] + sentence[idx_2 + len('because'):])

# 26.
print(idx_1)

# 27.
# same 25

# 28 y 29.
p_list = p.split(' ')
print('Coding' == p_list[0])
print('Coding' == p_list[-1])

# 30.
spaces = '   Coding For All      '
print(f'"{spaces}" --> strip --> "{spaces.strip()}"')

# 31.
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# 32.
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(f'{" ".join(libs)}')

# 33.
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34.
print("Name\t\tAge\t\tCountry\t\tCity")
print("Asabeneh\t250\t\tFinland\t\tHelsinki")

# 35.
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')

# 36.
print(f'8 + 6 = {8 + 6}')
print(f'8 - 6 = {8 - 6}')
print(f'8 * 6 = {8 * 6}')
print(f'8 / 6 = {8 / 6}')
print(f'8 % 6 = {8 % 6}')
print(f'8 // 6 = {8 // 6}')
print(f'8 ** 6 = {8 ** 6}')
