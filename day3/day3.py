#encoding:utf-8
r1=12.34
r2=9.08
r3=73.1
s1=3.14*r1*r1
s2=3.14*r2*r2
s3=3.14*r3*r3

#调用函数
print(abs(100))
print(abs(-20))
print(abs(12.34))
print(max(1,2))
print(max(2,3,1,-5))
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))
a=abs
print(a(-1))

#定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
def nop():
    pass
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
import  math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)
r=move(100,100,60,math.pi/6)
print(r)
import math
print(math.sqrt(2))

#函数的参数
def power(x):
    return x*x
print(power(5))
print(power(15))
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(5))
print(power(5,2))
def enroll(name,gender):
    print('name:',name)
    print('gender:',gender)
print(enroll('Sarah','F'))
def enroll(name,gender,age=6,city='Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
print(enroll('Sarah','F'))
enroll('Bob','M',7)
enroll('Adam','M',city='Tianjin')
print(enroll('Bob','M'))
def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1,2,3]))
print(add_end(['x','y','z']))
print(add_end())
print(add_end())
print(add_end())
def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
print(add_end())
print(add_end())
def calc(numbers):
    sum=0
    for n in numbers:
        sum = sum+n*n
    return sum
print(calc([1,2,3]))
print(calc((1,3,5,7)))

print(calc((1,2,3)))
print(calc((1,3,5,7)))

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3))
print(calc())
nums=[1,2,3]
print(calc(nums[0],nums[1],nums[2]))
nums=[1,2,3]
calc(*nums)
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
print(person('Michael',30))
print(person('Bob',35,city='Beijing'))
print(person('Adam',45,gender='M',job='Engineer'))
extra={'city':'Beijing','job':'Engineer'}
print(person('Jack',24,**extra))
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
print(person('Jack',24,city='Beijing',addr='Chaoyang',zipcode=123456))
