it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1.
print(A.union(B))

# 2.
print(A.intersection(B))

# 3.
print(A.issubset(B))

# 4.
print(A.isdisjoint(B))

# 5.
print(A.union(B), B.union(A)) # ?

# 6.
print(A.symmetric_difference(B))

# 7.
del A
del B
