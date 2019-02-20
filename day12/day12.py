#encoding：utf-8
#使用元类
#type()
class Hello(object):
    def hello(self,name='world'):
        print('Hello,%s.'% name)
# from hello import Hello
h=Hello()
print(h.hello())
print(type(Hello))
print(type(h))
def fn(self,name='world'):
    print('Hello,%s.'% name)
Hello=type('Hello',(object,),dict(hello=fn))
h=Hello()
print(h.hello())
print(type(Hello))
print(type(h))

#metaclass
class ListMetaclass(type):
    def __new__(cls, name, bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
class MyList(list,metaclass=ListMetaclass):
    pass
L=MyList()
L.add(1)
print(L)
class Field(object):
    def __init__(self,name,column_type):
        self.name=name
        self.column_type=column_type
    def __str__(self):
        return '<%s:%s'%(self.__class__.__name__,self.name)
class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')
class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model:%s'% name)
        mappings=dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping:%s==>%s'%(k,v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__']=mappings
        attrs['__table__']=name
        return type.__new__(cls,name,bases,attrs)
class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model'object has no attribute'%s'"% key)
    def __setattr__(self, key, value):
        self[key]=value
    def save(self):
        fields=[]
        params=[]
        args=[]
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql='insert into %s(%s) value(%s)'%(self.__table__,','.join(fields),','.join(params))
        print('SQL:%s'% sql)
        print('ARGS:%s'% str(args))
class User(Model):
    id=IntegerField('id')
    name=StringField('username')
    email=StringField('email')
    password=StringField('password')
u=User(id=12345,name='Michael',email='test@orm.org',password='my-pwd')
print(u.save)

#错误 调试和测试
#错误处理

try:
    print('try...')
    r=10/2
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')
try:
    print('try...')
    r=10/int('a')
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
finally:
    print('finally...')
print('END')
try:
    print('try...')
    r=10/int('2')
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
def foo(s):
    return 10/int(s)
def bar(s):
    return foo()*2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:',e)
    finally:
        print('finally...')

#调用栈
#err.py:def foo(s):



#记录错误
#err_logging.py
import logging
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
print(main())
print('END')

#抛出错误
#err_raise.py
# class FooError(ValueError):
#     pass
# def foo(s):
#     n=int(s)
#     if n==0:
#         raise FooError('invalid value:%s'% s)
#     return 10/n
# print(foo('0'))

#练习
from functools import reduce
def str2num(s):
    return float(s)
def calc(exp):
    ss=exp.split('+')
    ns=map(str2num,ss)
    return reduce(lambda acc,x:acc+x,ns)
def main():
    r=calc('100+200+345')
    print('100+200+234=',r)
    r=calc('99+88+7.6')
    print('99+88+7.6=',r)
print(main())

#调试
# def foo(s):
#     n=int(s)
#     print('>>>n=%d'% n)
#     return 10/n
# def main():
#     foo('0')
# print(main())

#d断言
# def foo(s):
#     n=int(s)
#     assert n !=0,'n is zero!'
#     return 10/n
# def main():
#     foo('0')
# print(main())

#logging
import logging
# logging.basicConfig(level=logging.INFO)
# s='0'
# n=int(s)
# logging.info('n=%d'% n)
# print(10/n)


