# 1.
dog = {}

# 2.
dog['name'] = 'Clifford'
dog['color'] = 'Rojo'
dog['breed'] = 'Sabueso'
dog['legs'] = 4
print(dog)

# 3.
student = {
    'first_name': 'Javier',
    'last_name': 'Rodriguez',
    'gender': 'Male',
    'age': 25,
    'marital status': 'single',
    'skills': ['React', 'Styled Components', 'Python', 'FastAPI', 'PostgreSQL'],
    'country': 'Argentina',
    'city': 'Buenos Aires',
    'address': 'Calle Falsa 123'
}
print(student)

# 4.
print(len(student))

# 5.
print(student.get('skills'))
print(type(student.get('skills')))

# 6.
student['skills'].append('JavaScript')
student['skills'].append('TailwindCSS')
print(student['skills'])

# 7.
print(student.keys())

# 8.
print(student.values())

# 9.
print(student.items())

# 10.
del student['address']

# 11.
del dog
