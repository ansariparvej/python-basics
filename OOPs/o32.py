# Multi-level Inheritance:

class bank:
    def txn(self):
        print("Total transaction value: ")
    def act_open(self):
        print("Your account open status: ")
    def deposite(self):
        print("your deposited account: ")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will show you the txn. happened to icici through hdfc")

class icici(HDFC_bank):
    pass

i = icici()
print(i.hdfc_to_icici())
print(i.deposite())
print(i.act_open())
print(i.txn())