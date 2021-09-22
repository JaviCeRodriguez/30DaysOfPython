from ex_level1 import family_members

# 1.
siblings = family_members[2:]
parents = family_members[:2]
print(siblings, '\n', parents)

# 2.
fruits = ('orange', 'banana', 'watermelon')
vegetables = ('tomato', 'onion', 'carrot')
animal = ('fish', 'cat', 'cow') # Rosario mode ON
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

# 3.
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4.
idx_mid = len(food_stuff_lt) // 2
print(food_stuff_tp[:idx_mid])

# 5.
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

# 6.
del food_stuff_tp

# 7.
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f'"Estonia" in nordic_countries? {"Estonia" in nordic_countries}')
print(f'"Iceland" in nordic_countries? {"Iceland" in nordic_countries}')
