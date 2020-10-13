#abnormal code or case

num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
try:
    res=num1/num2
    print(res)
except:
    print("exception occured")

finally:
    #mandatory code which will be executed if exception happens or not(both cases)
    print("Thank you")