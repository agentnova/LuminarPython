
# num=int(input("enter element :"))
# for i in range(0,len(lst)-1):
#     for j in range(0,len(lst)-1):
#         if(lst[i]+lst[j]==num):
#             print(lst[i],lst[j])
#

lst=[1,2,3,4,5,6,2,7]
num=int(input("enter element :"))
lst.sort()
low=0
upp=len(lst)-1
while(0<=3):
    data=lst[low]+lst[upp]
    if(data==num):
        print("pairs",lst[low],",",lst[upp])
        break
    elif(data>num):
        upp=upp-1
    else:
        low=low+1