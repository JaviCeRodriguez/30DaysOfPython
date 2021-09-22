person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1.
if 'skills' in person:
    middle = len(person) // 2
    print(f'Middle skill: {person["skills"]}')

# 2.
if 'skills' in person:
    print(f'Python is{"" if "Python" in person["skills"] else " not"} in skills')

# 3.
if len(person['skills']) == 2 and 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('He is a front end developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a backend developer')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a fullstack developer')
else:
    print('unknown title')

# 4.
if person['is_marred'] and person['country'] == 'Finland':
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is {person["is married"]}')
