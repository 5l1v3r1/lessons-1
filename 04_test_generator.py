def gen():
    for i in range(2):
        yield i


g = gen()
print(next(g))
print(next(g))

c = gen()
for i in c:
    print(i)