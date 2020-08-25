#print employee name who have salary > 17000
employees=[[100,"Arjun",20000],
           [101,"vinu",15000],
           [102,"binu",18000],
           [103,"aarun",10000]]

# for emp in employees:
#     if(emp[2]>17000):
#         print(emp[1])
sum=0
for emp in employees:
    sum+=emp[2]

print(sum)