#encoding:utf-8
#生成器
L=[x*x for x in range(10)]
print(L)
g=(x*x for x  in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
g=(x*x for x in range(10))
for n in g:
    print(n)
def fib(max):
    n,a,b=0,0,1
    while n < max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
print(fib(6))
def fib(max):
    n,a,b=0,0,1
    while n < max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
f=fib(6)
print(f)
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)
o=odd()
print(next(o))
print(next(o))
print(next(o))
for n in fib(6):
    print(n)
g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

#迭代器
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))

