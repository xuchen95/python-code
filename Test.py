"""说明这是一个测试python代码"""
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b, a+b
        n+=1
    return 'done'

f = fib(6)

print(f)

for e in f:
    print(e)




