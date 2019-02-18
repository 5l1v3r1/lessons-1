class A1():
    def __init__(self, *args, **kwargs):

        self.fieldA = 'A'
        self.fieldB = 'B'
        self.__fieldC = 'C'

        return super().__init__(*args, **kwargs)


a = A1()
print(a.__dict__)  # _A__fieldC - private

# descriptors Get Set Delete

print('*'*20)


class Robot:

    def __init__(self, name, build_year, lk=0.5, lp=0.5):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable!"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse!"
        elif s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"


x = Robot("Marvin", 1979, 0.2, 0.4)
y = Robot("Caliban", 1993, -0.4, 0.3)
print(x.condition)
print(y.condition)

print('*'*20)


class P:

    def __init__(self, x):
        self.set_x(x)

    def get_x(self):
        print('call get')
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(get_x, set_x)


p = P(1)
p.x = 3000
print(p.x)
