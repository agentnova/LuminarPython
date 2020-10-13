# txt=input("Enter the string : ")
# rslt=""
# for i in range(1,len(txt)+1):
#     rslt+=i*txt[i-1]
# print(rslt)
#




















lst=[3,1,5,6,9,2]
lst2=[]
for j in range(0,len(lst)):
    if(lst[j]>5):
        lst2.append(lst[j]-1)
    elif(lst[j]<5):
        lst2.append(lst[j]+1)
    else:
        lst2.append(lst[j])

print("New List :",lst2)

