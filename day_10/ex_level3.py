from countries import countries
from countries_data import countries_data as cd

# 1.
the_lands = []

for country in countries:
    if 'land' in country:
        the_lands.append(country)

print(the_lands)


# 2.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_reverse = []

for i in range(len(fruits)):
    fruits_reverse.append(fruits[len(fruits) - 1 - i])

print(fruits_reverse)


# 3.
languages = []
for country in cd:
    for lang in country["languages"]:
        languages.append(lang)

print(f'Number of languages in the data: {len(set(languages))}')

langs = {}
for language in languages:
    if language in langs:
        langs[language] += 1
    else:
        langs[language] = 0

