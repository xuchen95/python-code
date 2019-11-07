#无限序列 
def _odd_iter():
    n=1
    while True:
        n+=2
        yield n

#筛选函数 
def _not_divisible(n):
    return lambda x:x%n > 0

#生成器,不断生成下一个素数 
def primes():
    yield 2
    #it指向列表生成器... 
    it = _odd_iter() 
    while True: 
        #获取下一个元素
        n=next(it)  
        yield n 
        #更新列表
        it = filter(_not_divisible(n), it) 

#生成1000以内的素数 
for n in primes():
    if n<1000:
        print(n)
    else:
        break

