# 1.
sum = 0
for x in range(101):
    sum += x
print(f'The sum of all numbers is {sum}')

# 2.
sum_evens = 0
sum_odds = 0
for x in range(101):
    if x % 2:
        sum_evens += x
    else:
        sum_odds += x
print(f'The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odds}.')
