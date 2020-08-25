import datetime

class Person:
    def setValue(self,pname,age):
        self.age=age
        self.pname=pname


class Bank(Person):
    bank = "SBI"
    def __init__(self, accno):
        self.accno = accno
        self.balance = 3000
        self.bankname = Bank.bank

    def withdraw(self, amount):
        self.balance -= amount
        if (self.balance < amount):
            print("insufficient balance")
        else:
            print("Your account has been debited with Rs", amount, "on", datetime.date.today())
            print("Remaining balance is", self.balance)
    def deposit(self, amount):
        self.balance += amount
        print("Your",Bank.bank,"account has been credited with Rs", amount, "on", datetime.date.today())
        print("Remaining balance is ", self.balance)

    def balanceEnquiry(self):
        print("Account number", self.accno)
        print("Name", self.pname)
        print("Age",self.age)
        print("Bank name", Bank.bank)
        print("Balance is ", self.balance)


obj = Bank(1001)
obj.setValue("Arjun",21)




obj.balanceEnquiry()
