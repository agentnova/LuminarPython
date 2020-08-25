class Person:
    # method
    def __init__(self, name, age, gender):
        self.age = age
        self.name = name
        self.gender = gender

    def PrintValues(self):
        print(self.name)
        print(self.age)
        print(self.gender)

obj = Person("arjun",20,"male")
obj.PrintValues()