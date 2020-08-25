#bubble sorting

lst=[4,6,2,5,9]
print("Before sorting :",lst)
for i in range(0,len(lst)):
    for j in range(0,len(lst)-i-1):
        if(lst[j]>lst[j+1]):
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp
print("After sorting :",lst)
