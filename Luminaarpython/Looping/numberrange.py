# print numbers from lower limit to uper limit

low=int(input("enter lower limit :"))
upper=int(input("enter upper limit :"))
evensum=0
oddsum=0
for i in range(low,(upper+1)):
    if(i%2==0):
        evensum=evensum+i
    else:
        oddsum=oddsum+i
print("even sum :",evensum)
print("odd sum :",oddsum)
