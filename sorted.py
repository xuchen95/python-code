
from operator import itemgetter
#operator.itemgetter函数
#operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为序号

print(sorted([36,5,-12,9,-21], key=abs))

print(sorted(['bob', 'zoo', 'about','Credit'], key=str.lower))


#practice sorted()函数

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


#将列表按名字排序
def by_name(t):
    print(sorted(t, key=itemgetter(0)))



#将列表按成绩排序
def by_score(t):
    print(sorted(t, key=lambda t: t[1]))

print(sorted(L, key=itemgetter(1), reverse=True))

by_score(L)
by_name(L)

