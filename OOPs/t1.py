# Class (Classification of Entities) and Objects (real time objects):
class Person:
    def __init__(self,name,surname,emailid,dob):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.dob = dob

pmaa = Person("pma","ANS","pam@gmail.com",3025)
pmab = Person("pma1","ANS1","pam1@gmail.com",30251)
pmac = Person("pma2","ANS2","pam2@gmail.com",30252)

print(pmaa.name)
print(pmab.name)
print(pmac.name)
print(type(pmaa))





