# Class (Classification of Entities) and Objects (real time objects):
class Person:
    def __init__(self, name, surname, emailid, dob):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.dob = dob
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def age(self, current_year):
        return current_year


pmaa = Person("pma", "ANS")
agediff = pmaa.age(4025)

print(agediff)