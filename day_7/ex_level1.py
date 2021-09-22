it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1.
print(len(it_companies))

# 2.
it_companies.add('Twitter')
print(it_companies)

# 3.
other_it_companies = {'Polywork', 'Azure', 'Globant', 'FrontendCafe'}
it_companies.update(other_it_companies)
print(it_companies)

# 4.
it_companies.remove('Amazon')
print(it_companies)

# 5.
'''
We can remove an item from a set using remove() method. If the item is 
not found remove() method will raise errors, so it is good to check if 
the item exist in the given set. However, discard() method doesn't raise any errors.
'''