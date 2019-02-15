#encoding：utf-8
#高阶函数
print(abs(-10))
print(abs)
x=abs(-10)
print(x)
f=abs
print(f)
f=abs
print(f(-10))
# abs=10
# print(abs(-10))
def add(x,y,f):
    return f(x)+f(y)
print(add(-5,6,abs))

#高阶函数map/reduce
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
L=[]
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print(L)
print(list(map(str,[1,2,3,4,5,6,7,8,9])))
from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,3,5,7,9]))
from functools import reduce
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))
from functools import reduce
def fn(x,y):
    return x*10+y
def char2num(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]
print(reduce(fn,map(char2num,'13579')))
from functools import reduce
DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))
from functools import reduce
DIHITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))

def normalize(name):
    pass
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)
#练习一
def normalize(s):
    return (s.lower().title())
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)

#练习2
def prod(L):
    def  multi(x,y):
        return x*y
    return (reduce(multi,L))
print('3*5*7*9=',prod([3,5,7,9]))

#练习3
def str2float(s):
    def char2num(s):
        DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':'.'}
        return DIGITS[s]
    def fn(x,y):
        return x*10+y
    def fm(x,y):
        return x*0.1+y
    r1=[]
    r2=[]
    n=0
    m=-1
    r=list(map(char2num,s))
    while n <3:
        r1.append(r[n])
        n=n+1
    while m>-4:
        r2.append(r[m])
        m=m-1
    return reduce(fn,r1)+reduce(fm,r2)/10
print('str2float(\'123.456\')=',str2float('123.456'))

#高阶函数filter
def is_odd(n):
    return n % 2==1
list(filter(is_odd,[1,2,4,5,6,9,10,15]))

def not_empty(s):
    return s and s.strip()
list(filter(not_empty,['A','','B',None,'C',' ']))
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
def _not_divisible(n):
    return lambda x:x % n>0
def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)
for n in primes():
    if n <1000:
        print(n)
    else:
        break
