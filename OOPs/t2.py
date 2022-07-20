# Class (Classification of Entities) and Objects (real time objects):
class Person:
    def __init__(self,name,surname,emailid,dob):
        self.v1 = name
        self.v2 = surname
        self.v3 = emailid
        self.v4 = dob

pmaa = Person("pma","ANS","pam@gmail.com",3025)
pmab = Person("pma1","ANS1","pam1@gmail.com",30251)
pmac = Person("pma2","ANS2","pam2@gmail.com",30252)

print(pmaa.v1)
print(pmab.v1)
print(pmac.v1)
print(type(pmaa))





