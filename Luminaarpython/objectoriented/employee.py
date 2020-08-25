class Employee:
    def SetEmployee(self,Eid,Ename,Designation,Salary):
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

obj=Employee()
obj.SetEmployee(1001,"Arjun","Developer",30000)
obj.PrintValues()
# self is a keyword used to point current class instance

# constructor
# initialise instance variables,
# constructor automatically invoked during time of object creation
# the name of constructor is always __init__(self)

