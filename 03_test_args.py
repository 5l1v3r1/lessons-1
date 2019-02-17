def add(*args):
    print(args)
    print(sum(args))


add(1, 2)
add()

add(*[1, 2, 4])


def add1(a, *args):  # не желательно
    print(a)
    print(args)
    print(sum(args))


add1(1, 2, 3)


def gen():
    for i in range(10):
        yield i


add(*gen())  # плохо, потому что генератор открутился полностью


def add2(*args, **kwargs):
    print(args)
    print(sum(args))
    print(kwargs)


print('-'*20)
add2(*[1, 2, 3], age=20, len=40)
