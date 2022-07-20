# module(s) = file(s), package = (folder + __init__.py file) which contains module(s)

# Importing the required function from file t9:
from t9 import employee
print(employee) # Prints results of t9 module.

obj = employee()
print(obj.yob)
print(obj._name)
print(obj._employee__surname)

print(obj)
print(obj._age(2022))
print(obj._person__age1(2023))
