even=[]
odd=[]
sum=0
f=open("numbers.txt","r")
for num in f:
    if(int(num)%2==0):
        even.append(num.rstrip("\n"))
    else:
        odd.append(num.rstrip("\n"))
print("even list :",even)
print("odd list :",odd)




# num.rstrip("\n")==trailing/ending char removal
# num.lstrip("h")==leading/first char removal
#


# odd numbers into one list even into another

