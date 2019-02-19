#encoding:utf-8
#面向对象高级编程
#使用__slots__
class Student(object):
    pass
s=Student()
s.name='Michael'
print(s.name)
def set_age(self,age):
    self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)
s2=Student()
def set_score(self,score):
    self.score=score
Student.set_score=set_score
s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)
class Student(object):
    __slots__ = ('name','age')
s=Student()
s.name='Michael'
s.age=25
print(s.name)
print(s.age)
class GraduateStudent(Student):
    pass
g=GraduateStudent()
g.score=9999
print(g.score)

#使用@property
class Student1(object):
    def get_score(self):
        return self.get_score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value <0 or value>100:
            raise ValueError('score must between 0~100!')
        self._score=value
s=Student1()
s.set_score(60)
print(s.get_score())

class Student2(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must ba an integer!')
        if value<0 or value >100:
            raise ValueError('score must between 0~100!')
        self._score=value
s=Student2()
s.score=60
print(s.score)
class Student3(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth=value
    @property
    def age(self):
        return 2015-self._birth
s=Student3()
s.birth=1990
print(s.age)

#练习
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value
    @property
    def heigth(self):
        return self._heigth
    @heigth.setter
    def heigth(self,value):
        self._heigth=value
    @property
    def resolution(self):
        return self._width*self._heigth
s=Screen()
s.width=1024
s.heigth=768
print('resolution=',s.resolution)

#多重继承
class Animal(object):
    pass
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass
class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying...')
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass
class Parrot(Bird,Flyable):
    pass
class Ostrich(Mammal,Runnable):
    pass
dog=Dog()
print(dog.run())
bat=Bat()
print(bat.fly())
parrot=Parrot()
print(parrot.fly())
ostrich=Ostrich()
print(ostrich.run())

#Mixln









