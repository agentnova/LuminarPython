class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def printValue(self):
        print(self.id)
        print(self.name)
        print(self.salary)

    def __str__(self):
        return self.name


obj = Employee(1001, "Arjun", 50000)
obj2 = Employee(1002, "Abhiram", 80000)
obj3 = Employee(1003, "Athul", 40000)
obj4 = Employee(1004, "Arun", 70000)

lst = []
lst2 = []
lst.append(obj)
lst.append(obj2)
lst.append(obj3)
lst.append(obj4)

for emp in lst:
    lst2.append(emp.salary)
for emp in lst:
    if (max(lst2) == emp.salary):
        print(emp)
