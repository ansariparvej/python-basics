# Simple Inheritance:
class car:
    def __init__(self,body,engine,tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre
    def milege(self):
        print("Milege of my car: ")

c = car("solid", "v6", "radial")
print(c)

class tata(car):
    pass
t = tata("solid1", "v8", "radial1")
print(t)

print(t.milege())

