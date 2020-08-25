#polymorphism

# 1.method overloading
# 2.method overriding
# 3.operator overloading

# 1.method overloading
# same method name but different number of argument
class Math:
    def add(self):
        num=10
        num2=20
        print(num+num2)
    def add(self,num1):
        num=20
        print(num+num1)
    def add(self,num1,num2):
        print(num1+num2)
m=Math()
m.add(10,10)
# python doesnt support method overloading directly only works last defined method