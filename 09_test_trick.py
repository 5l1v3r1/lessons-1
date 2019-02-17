# _ - последний вывод

print(2+3)
print(globals())


print('*'*20)

x = 100
x = 10 if x == 10 else 5
print(x)

print('Ok' if x == 10 else 'No ok')

print('*'*20)

def pr(x,y,z):
    print(x,y,z)

l1 = [1,2,3]
l2 = {'x':1 , 'y':2 , 'z':3}

pr(*l1)
pr(**l2)

print('*'*20)

fn = {'sum': lambda x,y: x + y,
      'sub': lambda x,y: x - y}

print(fn['sum'](1,2))
print(fn['sub'](1,2))

