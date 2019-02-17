#encoding:utf-8
#访问限制
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s:%s'% (self.__name,self.__score))
# bart=Student('Bart Simpson',59)
# print(bart.__name)
class Student1(object):
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
class Student2(object):
    def set_score(self,score):
        self.__score=score


#继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass
class Cat(Animal):
    pass
dog=Dog()
print(dog.run())
cat=Cat()
print(cat.run())
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')
dog=Dog()
print(dog.run())
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
dog=Dog()
print(dog.run())
cat=Cat()
print(cat.run())
a=list()
b=Animal()
c=Dog()
print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Dog))
print(isinstance(c,Animal))
b=Animal()
print(isinstance(b,Dog))
def run_twice(animal):
    animal.run()
    animal.run()
print(run_twice(Animal()))
print(run_twice(Dog()))
print(run_twice(Cat()))
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
print(run_twice(Tortoise()))
class Timer(object):
    def run(self):
        print('Start...')
timer=Timer()
print(timer.run())


#获取对象信息
#使用type()
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type(a))
print(type(123)==type(456))
print(type(123)==int)
print(type('abc')==type('123'))
print(type('abc')==str)
print(type('abc')==type(123))
import types
def fn():
    pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

#使用isinstance()
a=Animal()
d=Dog()
print(isinstance(d,Dog))
print(isinstance(d,Animal))
print(isinstance('a',str))
print(isinstance(123,int))
print(isinstance(b'a',bytes))
print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))


#使用dir()
print(dir('ABC'))
print(len('ABC'))
print('ABC'.__len__())
class MyDog(object):
    def __len__(self):
        return 100
dog=MyDog()
print(len(dog))
print('ABC'.lower())
class Myobject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x
obj=Myobject()
print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',19)
print(hasattr(obj,'y'))
print(getattr(obj,'y'))
print(obj.y)
print(getattr(obj,'z',404))
print(hasattr(obj,'power'))
print(getattr(obj,'power'))
fn=getattr(obj,'power')
print(fn)
print(fn())

#实例属性和类属性
class Student(object):
    def __init__(self,name):
        self.name=name
s=Student('Bob')
s.score=90
class Student(object):
    name='Student'
s=Student()
print(s.name)
print(Student.name)
s.name='Michael'
print(s.name)
print(Student.name)
del s.name
print(s.name)



