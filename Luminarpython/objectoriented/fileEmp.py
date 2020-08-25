class Employee:
    def __init__(self,Eid,Ename,Designation,Salary):
        # this method initialises instance variables
        self.Eid=Eid # instance variable
        self.Ename=Ename
        self.Designation=Designation
        self.Salary=Salary
    def PrintValues(self):
        print(self.Eid)
        print(self.Ename)
        print(self.Designation)
        print(self.Salary)
f=open("a.txt","r")
for employee in f:
    data=employee.split(",")
    eid=data[0]
    ename=data[1]
    des=data[2]
    salar=data[3]

    obj=Employee(eid,ename,des,salar)
    obj.PrintValues()
