#second largest number
num1=int(input("enter number 1 :"))
num2=int(input("enter number 1 :"))
num3=int(input("enter number 1 :"))

if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("number 2 is 2nd largest")
    else:
        print("number 3 is second largest")
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print("number1 is 2nd largest")
    else:
        print("number3 is 2nd largest")
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("number1 is 2nd largest")
    else:
        print("number2 is 2nd largest")
