#encoding:utf-8
#偏函数
print(int('12345'))
print(int('12345',base=8))
print(int('12345',16))
def int2(x,base=2):
    return int(x,base)
print(int2('1000000'))
print(int2('1010101'))
import functools
int2=functools.partial(int,base=2)
print(int2('1000000'))
print(int2('1010101'))
print(int2('1000000',base=10))

#使用模块
'a test module'
__author__='Micheal Lisa'
import sys
def test():
    args=sys.argv
    if len(args)==1:
        print('Hello,world!')
    elif len(args)==2:
        print('Hello,%s!'% args[1])
    else:
        print('Too many arguments!')
if __name__=='__main__':
    test()

#作用域
def _private_1(name):
    return 'Hello,%s'% name
def _private_2(name):
    return 'Hi,%s'% name
def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)


#安装第三方模块
import sys
print(sys.path)

#面向对象编程
std1={'name':'Micheeal','score':98}
std2={'name':'BOb','score':81}
def print_score(std):
    print('%s:%s'%(std['name'],std['score']))
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s:%s'%(self.name,self.score))

#类和实例
class Student(object):
    pass
bart = Student()
print(bart)
print(Student)
bart.name='Bart Simpson'
print(bart.name)
class Student1(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
bart=Student1('Bart Simpson',59)
print(bart.name)
print(bart.score)

#数据封装
def print_score(std):
    print('%s:%s'%(std.name,std.score))
print(print_score(bart))
class Student(object):
    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'



