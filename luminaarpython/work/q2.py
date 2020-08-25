# [X,Y,Z]=[(X,Y),(X,Z),(Y,Z)]
lst=[2,3,4,3,5]
lst2=[]
for i in range(0,len(lst)-1):
    ls=lst[i],lst[i+1]
    if(ls not in lst2):
        lst2.append(ls)
    last=lst[0],lst[len(lst)-1]
    if(last not in lst2):
        lst2.append(last)
print(lst2)



