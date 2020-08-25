limit=int(input("enter the limit :"))
count=0
num1=0
num2=1
while(count<limit):
    print(num1)
    num3=num1+num2
    num1=num2
    num2=num3
    count+=1
