# 1.
for n in range(11):
    print(n, end=" ")

print("")

x = 0
while x != 11:
    print(x, end=" ")
    x += 1

print("\n")

# 2.
for n in range(11):
    print(10 - n, end=" ")

print("")

x = 10
while x >= 0:
    print(x, end=" ")
    x -= 1

print("\n")

# 3.
for n in range(1, 8):
    print('#' * n)

print("")

# 4.
for _ in range(8):
    for _ in range(8):
        print('#', end=" ")
    print("")

# 5.
print("")
for x in range(11):
    print(f'{x} x {x} = {x ** 2}')

print("")

# 6.
for i in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
    print(i)

print("")

# 7.
for n in range(101):
    if n % 2:
        print(n, end=" ")

print("\n")

# 8.
for n in range(101):
    if not n % 2:
        print(n, end=" ")
