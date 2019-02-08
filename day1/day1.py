#encoding:utf-8
print(100+200)
print('hello, world')
print(100+200+300)
print('D://learngit//hello.py')
print('hello, world')
print('the quick brown fox', 'jumps over','the lazy dog')
print('I\'m\"ok\"!')
print('I\'m ok.')
print('I\'m learning\nPython.')
print('\\\n\\')
print('\\\t\\')
print(r'\\\t\\')
print('''line1
line2
line3''')
print(True)
print(False)
print(3>2)
print(3>5)
print(True or True)
print(True or True)
print(False or False)
print(5>3 or 1>3)
print(not True)
print(not False)
print(not 1>2)
age=3
if age >= 18:
    print('adult')
else:
    print('teenager')
a = 123
print(a)
a = 'ABC'
print(a)
a = 'ABC'
b = a
a = 'XYZ'
print(b)
PI = 3.14159265359
print(10/3)
print(9/3)
print(10//3)
print(10%3)



# _*_ coding: utf-8 _*_
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello. \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa'''
print(s2)
print('包含中文的str')
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')
x = b'ABC'
# print('ABC'.encode('ascii'))
# print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
print('中文'.encode('gb2312'))

#使用list和tuple
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
# print(classmates[0])
# print(classmates[1])
# print(classmates[1])
# print(classmates[2])
# print(classmates[3])
print(classmates[-1])
print(classmates[-2])
classmates.append('Adam')
print(classmates)
classmates.insert(1, 'Jack')
print(classmates)
print(classmates.pop())
print(classmates)
print(classmates.pop(1))
print(classmates)
classmates[1] = 'Sarah'
print(classmates)
L = ['Apple',123, True]
s = ['python', 'java',['asp', 'php'], 'scheme']
print(len(s))
L = []
print(len(L))
classmates = ('Michael', 'Bob', 'Tracy')
t = (1, 2)
print(t)
t = ()
print(t)
t = (1)
print(t)
t = (1,)
print(t)
t = ('a','b', ['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)


#条件判断
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


#循环
print(1 + 2+ 3)
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
print(list(range(5)))
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

