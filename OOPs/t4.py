# Class (Classification of Entities) and Objects (real time objects):
class Person:
    def __init__(self,name,surname,emailid,dob):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.dob = dob

    def age(self,current_year):
        return current_year - self.dob

pmaa = Person("pma","ANS","pam@gmail.com",3025)
agediff = pmaa.age(4025)

print(agediff)