# PPP variable Concept:
class Person :
    def __init__(self , name ,surname , yob):
        self._name1 = name # Protected Variable
        self.__surname1 = surname # Private Variable
        self.yob1 = yob # Public variable

pma = Person("Anonymous", "gender", 1990)
print(pma._name1)
print(pma._Person__surname1)
print(pma.yob1)