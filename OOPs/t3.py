# Class (Classification of Entities) and Objects (real time objects):
class Person:
    def __init__(a,name,surname,emailid,dob):
        a.name = name
        a.surname = surname
        a.emailid = emailid
        a.dob = dob

pmaa = Person("pma","ANS","pam@gmail.com",3025)
pmab = Person("pma1","ANS1","pam1@gmail.com",30251)
pmac = Person("pma2","ANS2","pam2@gmail.com",30252)

print(pmaa.name+ pmaa.surname)
print(pmab.name+pmab.surname+str(pmab.emailid)+str(pmab.dob))
print(pmac.name)
print(type(pmaa))





