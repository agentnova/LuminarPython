#print maximum amng3
num1=int(input("enter number 1 :"))
num2=int(input("enter number 1 :"))
num3=int(input("enter number 1 :"))

if(num1>num2)&(num1>num3):
    print(num1," is maximum")
elif(num2>num1)&(num2>num3):
    print(num2," is maximum")
elif(num1==num2)&(num2==num3)&(num1==num3):
    print("all are equal numbers")
else:
    print(num3," is maximum")