# variables
a = 2
b = 3
f = 123.45
s = "hello"
print('* a, b, s')
print(a, b, s)
print('* a + b')
print(a + b)
print('* %')
print('a + b = %d' % (a + b))
print('a=%d, f=%f, s=%s' % (a, f, s))
print('a=%4d' % a)
print('a=%04d' % a)
print('f=%.1f' % f)
print('f=%.2f' % f)
print('f=%8.2f' % f)
print('f=%08.2f' % f)

print('* type')
print(type(a))
print(type(f))
print(type(s))

# if
print('* if')
if a == 1:
    print('a == 1')
else:
    print('a != 1')

if type(a) is int:
    print('a is int')
else:
    print('a is not int')
print('-----')

# for
print('* range(3)')
for i in range(3):
    print(i)
print('-----')

print('* range(10, 15)')
for i in range(10, 15):
    print(i)
print('-----')

# list
l = ['apple', 'orange']
print('* print l')
print(l)
print(l[0])
print(l[1])

print('* print l using for')
for item in l:
    print(item)
l[1] = 'lemon'
l.append('banana')

print('* print l again')
for item in l:
    print(item)
print('-----')

# 2次元list
print('* print l2')
l2 = [
    [1,2,3],
    [4,5,6],
]
print(l2)
l2[0][1] = 100
l2[1][1] = 200
print(l2)

# dictionary
d = {1: 'foo', 2: 'bar', 'hello': 'world'}
print('* print dictionary')
print(d[1])
print(d['hello'])

d['hello'] = 'Japan'
print('* print all dictionary items')
for k, v in d.items():
    print(k, v)
