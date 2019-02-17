a  = 1
b = a
print (b)
print(id(a)) #id возвращает идентификатор объекта 
print(id(b))

print ('*'*20)

a = 2 #создали новый объект
print (b)
print(id(a)) #id возвращает идентификатор объекта 
print(id(b))

print ('*'*20)

del(a,b)
a = []
b = a
a.append('ffff')
print (b)
print(id(a)) #id возвращает идентификатор объекта 
print(id(b))

print ('*'*20)

def f():
    x = 1

#x - не определена

print ('*'*20)

def one():
    l = [1,2]
    def prr():
        print(l)
        print(id(l))
    return prr

o = one()

o()

print ('*'*20)
print(dir(o))
print ('*'*20)
print(dir(o.__closure__))
print ('*'*20)
print(dir(o.__closure__[0]))
print(o.__closure__[0])
print ('*'*20)
print(o.__closure__[0].cell_contents)
a = o.__closure__[0].cell_contents
print(id(a))

a.append(555)
o() #мы изменили локальную переменную функции one из глобального поля, потому что в функции prr сохранена ссылка на переменную которую она видит, тоисть в o -> prr -> l



