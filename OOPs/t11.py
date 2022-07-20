# Importing the package with whole module => file t7:

from Import_example.import_example import Person
print(Person) # Prints results of t7 module.
obj = Person("Anonymous4", "gender4", 1993)
print(obj.yob1)
print(obj._name1)
print(obj._Person__surname1)

class person2:
    def ask_name(self):
        name = input("Tell me your last name: ")
        return name
NAME = person2()
print(NAME.ask_name())

