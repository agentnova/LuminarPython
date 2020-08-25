
# print(lst[3:7])
# print(lst[1:])
# print(lst[:6])
# print(lst[-1])

#
# num=int(input("enter the number to search :"))
# flag=0
# for i in lst:
#     if(i==num):
#         flag=1
# if(flag==1):
#     print("found")
# else:
#     print("not found")

lst=[1,2,3,4,5,6,7,8,9,10,11,12]
#if 6 print 3,4
num=int(input("enter the number"))
for i in lst:
    for j in lst:
        if(i+j==num):
            print(i,j)

