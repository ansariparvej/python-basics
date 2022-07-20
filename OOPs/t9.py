# Inheritance:

class person:
    _name = "Anonymous"
    __surname = "gender"
    yob = 1990

    def _age(self, current_year):
        return current_year - self.yob

    def __age1(self, current_year):
        return current_year - self.yob

obj1 = person()
print(obj1)
print(obj1._age(2020))
print(obj1._person__age1(2021))

class employee(person):
    _name = "Anonymous1"
    __surname = "gender1"
    yob = 1991

obj2 = employee()
print(obj2)
print(obj2._age(2022))
print(obj2._person__age1(2023))

print(obj2.yob)
print(obj2._name)
print(obj2._employee__surname)
