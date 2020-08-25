import functools
class Emp:
    def __init__(self, id, name, desig, salary):
        self.id = id
        self.name = name
        self.desig = desig
        self.sal = salary

    def printValue(self):
        print("name", self.name)
        print("designation", self.desig)
        print("salary",self.sal)

    def __str__(self):
        return self.name




f = open("a.txt", "r")
lst = []
for data in f:
    values = data.rstrip("\n").split(",")
    id = values[0]
    name = values[1]
    desig = values[2]
    sal = values[3]
    obj = Emp(id, name, desig, sal)
    lst.append(obj)
upper = list(map(lambda emp: emp.name.upper(), lst))
print("Name in upper case ")
print(upper)


salry = list(map(lambda emps: int(emps.sal) + 5000, lst))
print("\nUpdated salary ")
print(salry)

salry_greaterthan=list(filter(lambda empo: int(empo.sal) > 25000, lst))
print("\nEmployee with salary>25000")
for emp in salry_greaterthan:
    print(emp)

    
max_sal=functools.reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,list(map(lambda emp:emp.sal,lst)))
print("\nMaximum salary ",max_sal)



equals=list(filter(lambda emp:emp.sal==max_sal,lst))
for equ in equals:
    print(equ)

