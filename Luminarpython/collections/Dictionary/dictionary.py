# key value pair
dict={}
student={"rollno":1001,"name":"Arjun","Age":20,"cpp":25}
# duplicate keys are not allowed
# values may be duplicate
# print(student["name"])
# dict iteration

for keys in student:
    print(keys,",",student[keys])

# update value
student["cpp"]+=25
student["name"]="arun"
print(student)
print("total" in student)
student["total"]=150
print(student)