age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1.
age_new = set(age)
print(f'Largo de lista: {len(age)}')
print(f'Largo de set: {len(age_new)}')
#  Los largos son distintos, debido a que con set se eliminan valores repetidos

# 2.
'''
string: Caractereres de largo especifico
list: Elementos guardados en un array, pueden ser de cualquier tipo
tuple: Similar a la lista, pero no pueden mutar sus elementos
set: Similar a la lista, pero no permite datos repetidos
'''

# 3.
frase = 'I am a teacher and I love to inspire and teach people'
words = set(frase.replace(' ', ''))
print(words)
