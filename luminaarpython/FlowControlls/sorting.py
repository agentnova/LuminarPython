num1 = int(input("enter number 1 :"))
num2 = int(input("enter number 2 :"))
num3 = int(input("enter number 3 :"))

if(num1<num2)&(num1<num3):
    temp1=num1
    temp2 = num3
    temp3 = num2
    if(num2<num3):
        temp2=num2
        temp3=num3
elif(num2<num1)&(num2<num3):
    temp1=num2
    temp2 = num3
    temp3 = num1
    if(num1<num3):
        temp2=num1
        temp3=num3
else:
    temp1=num3
    temp2 = num1
    temp3 = num2
    if(num2<num1):
        temp2=num2
        temp3=num1
print("After sorting : ",temp1,temp2,temp3)