from datetime import datetime


def timeIt(func):
    def wrapped(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapped


#@timeIt
def One(rng):
    l = []
    for i in range(rng):
        if i % 2 == 0:
            l.append(i)
    return l


#@timeIt
def Two(rng):
    l = [i for i in range(rng) if i % 2 == 0]
    return l


l1 = One(100000)
la = Two(100000)

fwrap = timeIt(One)
print(type(fwrap), fwrap.__name__)

l1 = timeIt(One)(20000)

print('*'*30)

def timeItArg(arg):
    print(arg)
    def outer(func):
        def wrapped(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wrapped
    return outer


@timeItArg('name')
def OneArg(rng):
    l = []
    for i in range(rng):
        if i % 2 == 0:
            l.append(i)
    return l

l3 = OneArg(10000)
l4 = timeItArg('name')(OneArg)(10000) #без декоратора
