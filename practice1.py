#利用map()函数,将输入的名字首字母变为大写其余字母小写

from functools import reduce

names = ['jims','john','tom','LISA']
change_name=[]

for name in names:
    change_name.append(name.title())

print(change_name)

#用map()函数来写这个小程序
def useTitle(str):
    return str.title()

change_names = list(map(useTitle, names))

print(change_names)


