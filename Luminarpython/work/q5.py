lst=[1,2,3,4,5,6,2,7]
num=int(input("enter element :"))
for i in range(0,len(lst)-1):
    for j in range(0,len(lst)-1):
        if(lst[i]+lst[j]==num):
            print(lst[i],lst[j])