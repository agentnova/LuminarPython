# armstrong numbers

num=int(input("enter the number :"))
temp=num
sum=0
while(num>0):   #457>0
    # reminder=num%10
    rem=num%10   #457%10
    sum=(rem*rem*rem)+sum
    num=num//10
print("sum=",sum)
if(sum==temp):
    print("Its an armstrong number.")
    