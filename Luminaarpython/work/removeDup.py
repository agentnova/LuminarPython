lst=[10,10,20,63,20,23,5,63,5,23,45,36,26,16,78]
lst2=[]
lst.sort()
last=len(lst)
print(lst)

for i in range(0,last-1):
    temp=lst[i]
    if(temp!=lst[i+1]):
        lst2.append(temp)

if(lst[last-2]==lst[last-1]):
    lst2.append(lst[last-1])
else:
    lst2.append((lst[last-1]))
print(lst2)



