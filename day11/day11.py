#encoding:utf-8
#定制类
class Student(object):
    def __init__(self,name):
        self.name=name
print(Student('Michael'))
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Studenr object (name:%s)'% self.name
print((Student('Michael')))
s=Student('Michael')
print(s)
class Student(object):
    def __init__(self,name):
        slef.name=name
    def __str__(self):
        return 'Student object(name=%s)'%self.name
    __repr__=__str__

#__iter__
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>100000:
            raise StopIteration()
        return self.a
for n in Fib():
    print(n)

#__getitem__
class Fib(object):
    def __getitem__(self, n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
f=Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[10])
print(f[100])
#Fib切片
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n,int):
            a,b=1,1,
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b=b,a+b
            return L
f=Fib()
print(f[0:5])
print(f[:10])
print(f[:10:2])

#__getattr__
class Student(object):
    def __init__(self):
        self.name='Michael'
s=Student()
print(s.name)
class Student(object):
    def __init__(self):
        self.name='Michael'
    def __getattr__(self, attr):
        if attr=='score':
            return 99
s=Student()
print(s.name)
print(s.score)
class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda :25
s=Student()
print(s.age())
class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self, path):
        return Chain('%s/%s'%(self._path,path))
    def __str__(self):
        return self._path
    __repr__=__str__
print(Chain().status.user.timeline.list)

#__call__
class Student(object):
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('My name is %s.'% self.name)
s=Student('Michael')
print(s())
print(callable(Student('Michael')))
print(callable(max))
print(callable([1,2,3]))
print(callable(None))
print(callable('str'))

#使用枚举类
from enum import Enum
Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','JUl','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
from enum import  Enum,unique
@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6
day1=Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1==Weekday.Mon)
print(day1==Weekday.Tue)
print(Weekday(1))
print(day1==Weekday(1))
for name,member in Weekday.__members__.items():
    print(name,'=>',member)




