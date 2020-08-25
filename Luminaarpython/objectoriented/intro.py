# class
# blueprint,plan,design,design pattern

# object
# real world entity,constructed using design pattern

# reference
# if we want to perform an operation on object then we need to create reference

# class classname

# static variable/class variable used to save memory loss

class Person:
    # method
    def setValues(self, name, age, gender):
        self.age = age
        self.name = name
        self.gender = gender

    def PrintValues(self):
        print(self.name)
        print(self.age)
        print(self.gender)


# create reference

obj = Person()
obj.setValues("arjun",20,"male")
obj.PrintValues()
