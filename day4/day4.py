#encoding:utf-8
#递归函数
def fact(n):
    if n==1:
        return 1
    return  n*fact(n-1)
print(fact(1))
print(fact(5))
print(fact(100))
# print(fact(1000))
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num ==1:
        return product
    return fact_iter(num -1,num*product)
print(fact_iter(5,1))
print(fact_iter(4,5))
print(fact_iter(3,20))
print(fact_iter(2,60))
print(fact_iter(1,120))

def move(n,a,b,c):
    if n == 1:
        print(a,'-->',c)

#高级特性
#切片
L=['Michael','Sarah','Tracy','Bob','Jack']
print([L[0],L[1],L[2]])
r=[]
n=3
for i in range(n):
    r.append(L[i])

print(r)
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:])
print(L[-2:-1])
L=list(range(100))
print(L)
print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2])
print(L[::5])
print(L[:])
# print(0,1,2,3,4,5)[:3]
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

#迭代
d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
for ch in 'ABC':
    print(ch)
from collections import  Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))
for i,value in enumerate(['A','B','C']):
    print(i,value)
for x, y in [(1,1),(2,4),(3,9)]:
    print(x,y)

#列表生成式
print(list(range(1,11)))
L=[]
for x in range(1,11):
    L.append(x*x)
print(L)
print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x % 2 ==0])
print([m+n for m in 'ABC'for n in 'XYZ'])
import os
print([d for d in os.listdir('.')])
d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)
d={'x':'A','y':'B','z':'C'}
print([k+'='+ v for k,v in d.items()])
L=['Hello','World','IBM','Apple']
print([s.lower() for s in L])
x='abc'
y=123
print(isinstance(x,str))
print(isinstance(y,str))
