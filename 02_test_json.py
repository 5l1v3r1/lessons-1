import json

class Player:
    def __init__(self,name,age):
        self.name = name
        self.age  = age

    def forPrint(self):
        return self.name + ': ' + str(self.age)

class ComplexPlayerEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, Player):
            d ={
                "__Player__": True,
                "name": z.name,
                "age": z.age
            }
            return (d)
        else:
            super().default(self, z)

class ComplexPlayerDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.default)

    def default(self, z):
        if "__Player__" in z:
            player = Player(z["name"],z["age"])
            return player
        else:
            super().default(self, z)

player1 = Player('Vasya',30)
player2 = Player('Petya',40)
print(player1.__dict__)
players = []
players.append(player1)
players.append(player2)
del player1
del player2
print(players)

jsstr = json.dumps(players, cls=ComplexPlayerEncoder)

print(jsstr)

del players



players = json.loads(jsstr, cls=ComplexPlayerDecoder)

print(players)

print(players[0].forPrint())
print(players[1].forPrint())

# def props(x):
#     return dict((key, getattr(x, key)) for key in dir(x) if key not in dir(x.__class__))




