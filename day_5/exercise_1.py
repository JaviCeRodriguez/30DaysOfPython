# 1.
list_1 = []

# 2.
list_2 = ['Naruto', 'Sasuke', 'Sakura', 'Sai', 'Kakashi']

# 3.
print(f'Length of list: {len(list_2)}')

# 4.
print(f'First item: {list_2[0]}')
print(f'Middle item: {list_2[len(list_2) // 2]}')
print(f'Last item: {list_2[-1]}')

# 5.
mixed_data_types = ['Javier', 25, 170, 'Pelado', 'San Fernando']

# 6.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7.
print(f'{it_companies}')

# 8.
print(f'{len(it_companies)}')

# 9.
print(f'First item: {it_companies[0]}')
print(f'Middle item: {it_companies[len(it_companies) // 2]}')
print(f'Last item: {it_companies[-1]}')

# 10.
it_companies[4] = 'FrontendCafe'
print(f'{it_companies}')

# 11.
it_companies.append('InvGate')

# 12.
it_companies.insert(len(it_companies) // 2, 'FluxIt')

# 13.
it_companies[-1] = it_companies[-1].upper()

# 14.
print('#; '.join(it_companies))

# 15.
print(f'MySpace in "it_companies"? {"MySpace" in it_companies}')

# 16.
it_companies.sort()
print(it_companies)

# 17.
it_companies.sort(reverse=True)
print(it_companies)

# 18.
print(it_companies[3:])

# 19.
print(it_companies[:-3])

# 20.
idx = len(it_companies) // 2
print(it_companies[:idx] + it_companies[idx + 1:])

# 21.
it_comp = it_companies.copy()
del it_comp[0]
print(it_comp)

# 22.
idx = len(it_comp) // 2
del it_comp[idx]
print(it_comp)

# 23.
del it_comp[-1]
print(it_comp)

# 24.
it_comp.clear()
print(it_comp)

# 25.
del it_companies

# 26.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

# 27.
idx = full_stack.index('Redux')
full_stack.insert(idx + 1, 'Python')
full_stack.insert(idx + 2, 'SQL')
print(full_stack)
