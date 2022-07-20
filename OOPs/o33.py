# Multiple Inheritance:

class bank:
    def txn(self):
        print("Total transaction value: ")
    def act_open(self):
        print("Your account open status: ")
    def deposite(self):
        print("your deposited account: ")
    def test(self):
        print("This is test method from bank class.")

class HDFC_bank:
    def hdfc_to_icici(self):
        print("This will show you the txn. happened to icici through hdfc")
    def test(self):
        print("This is test method from HDFC_bank class.")

class ineuron_bank:
    def account_status_icici(self):
        print("Print a account status in icici")

class icici(bank,HDFC_bank,ineuron_bank):
    pass

i = icici()

i.hdfc_to_icici()
i.txn()
i.deposite()
i.act_open()
i.test()
i.account_status_icici()
