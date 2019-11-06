#求list里数的乘积
from functools import reduce

def prod(L):
    return reduce(lambda x,y:x*y, L)

value = prod([3,4,5,7,8])

print(value)


