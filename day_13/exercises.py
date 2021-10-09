# 1.
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers_filter = [n for n in numbers if n > 0]
print(numbers_filter)

# 2.
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_list = [c for a in list_of_lists for b in a for c in b]
print(one_list)


# 3.
def make_tuple(n):
    return tuple([n, n ** 0, n ** 1, n ** 2, n ** 3, n ** 4, n ** 5])


list_of_tuples = [make_tuple(n) for n in range(11)]

print(list_of_tuples)

# 4.
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_flatten = [[c[0].upper(), c[0].upper()[:3], c[1].upper()] for aux in countries for c in aux]
print(countries_flatten)

# 5.
countries_dict = [{"country": c[0].upper(), "city": c[1].upper()} for aux in countries for c in aux]
print(countries_dict)

# 6.
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [' '.join(person[0]) for person in names]
print(full_names)

# 7.
slope = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)
print(slope(x1=2, x2=5, y1=-2, y2=4))
