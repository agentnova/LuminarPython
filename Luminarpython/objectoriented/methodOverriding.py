# 1.method overriding
# class parent:
#     def phone(self):
#         print("samsung")
#
# class child(parent):
#     def phone(self):
#         print("iphone")
#
# c=child()
# c.phone()

# overrides parent method with childs on property

class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):#overrides built in method
        return self.name


E = Employee("arjun")
print(E)
