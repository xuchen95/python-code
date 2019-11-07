def not_empty(s):
    return s and s.strip()

L = ['A', 'B', None, '  ', 'C']

l1 = list(filter(not_empty, L))

print(l1)



