#encoding:utf-8
#高阶函数sorted
print(sorted([36,5,-12,9,-21]))
print(sorted([36,5,-12,9,-21],key=abs))
print(sorted(['bob','about','Zoo','Credit']))
print(sorted(['bob','about','Zoo','Credit'],key=str.lower))
print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))

#练习一
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(t):
    if len(t)>0:
        return t[0]
def by_score(t):
    if len(t)>1:
        return t[1]
L1=sorted(L,key=by_name)
print(L1)
L2=sorted(L,key=by_score,reverse=True)
print(L2)

#返回函数
def calc_sum(*args):
    ax=0
    for n in args:
        ax=ax+n
    return ax
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
f=lazy_sum(1,3,5,7,9)
print(f)
print(f())
f1=lazy_sum(1,3,5,7,9)
f2=lazy_sum(1,3,5,7,9)
print(f1==f2)

#闭包
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())

#练习
def counter():
    print('闭包中--')
    f[0]=f[0]+1
    return f
print(2,3)

def createCounter():
    f=[0]
    print('闭包外--')
    def counter():
        print('闭包内--')
        f[0]=f[0]+1
        return f[0]
    return counter
counterA=createCounter()
print(counterA(),counterA(),counterA(),counterA(),counterA())
counterB=createCounter()
print(counterB(),counterB,counterB,counterB)


#匿名函数
print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))
f=lambda x:x*x
print(f)
print(f(5))
def build(x,y):
    return lambda:x*x+y*y
print(build(1,2))

#练习
L=list(filter(lambda x:x%2==1,range(1,20)))
print(L)

#装饰器
def now ():
    print('2015-3-25')
f=now
print(f())
print(now.__name__)
print(f.__name__)
def log(func):
    def wrapper(*args,**kw):
        print('call %s():'% func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print('2015-3-25')
print(now())
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')
print(now())
print(now.__name__)
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():'% func.__name__)
        return func(*args,**kw)
    return wrapper
