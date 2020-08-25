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

obj=Employee(1001,"Arjun","Developer",30000)
obj.PrintValues()