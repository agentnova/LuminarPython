

class Bank {
    static bname;
    static setBank(){
        this.bname="Sbi"
    }
    constructor(accno,pname) {
        this.accno=accno;
        this.pname=pname;
        this.balance=3000;
    }
    deposit(amount){
        this.balance+=amount;
        console.log("Account has been credited with "+amount)
    }
    withdraw(amount){
        if(amount>this.balance){
            console.log("Insufficient balance")
        }
        else {
            console.log("Your account has been debited with Rs"+amount)
        }
    }
    checkBalance(){
        console.log("Current balance is "+this.balance)
    }
}
obj=new Bank(1001,"Arjun")
obj.deposit(2000)
obj.checkBalance()






//     bank = "SBI"
//     def
//     __init__(self, accno)
// :
//     self.accno = accno
//     self.balance = 3000
//     self.bankname = Bank.bank
//
//     def
//     withdraw(self, amount)
// :
//     self.balance -= amount
//     if (self.balance < amount):
//     print("insufficient balance")
// else:
//     print("Your account has been debited with Rs", amount, "on", datetime.date.today())
//     print("Remaining balance is", self.balance)
//     def
//     deposit(self, amount)
// :
//     self.balance += amount
//     print("Your", Bank.bank, "account has been credited with Rs", amount, "on", datetime.date.today())
//     print("Remaining balance is ", self.balance)
//
//     balanceEnquiry(){
//         print("Account number", self.accno)
//         print("Name", self.pname)
//         print("Age", self.age)
//         print("Bank name", Bank.bank)
//         print("Balance is ", self.balance)
//     }
// }
//
// class Person {
//     setValue(pname, age) {
//         this.age = age
//         this.pname = pname
//     }
// }
// obj = Bank(1001)
// obj.setValue("Arjun",21)