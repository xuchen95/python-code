from functools import reduce

digits = {'0':0, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def char2num(s):
    return digits[s]

def str2num(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))



print(str2num('583949'))