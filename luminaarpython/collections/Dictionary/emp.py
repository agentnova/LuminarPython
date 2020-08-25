employee={
    "eid":1001,
    "ename":"Arjun",
    "designation":"manager",
    "salary":15000

}

print(employee["ename"])
print("comp" in employee)
employee["company"]="luminar"
employee["salary"]+=5000
for keys in employee:
    print(keys,":",employee[keys])


# print emp name
# add a new record company name luminar
# check for company is there
# update employee salary=current salary+5000
# print all key values