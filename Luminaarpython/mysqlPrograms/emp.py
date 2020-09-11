f=open("employees","r")
emp={}
for lines in f:
    id,name,des,sal=lines.rstrip("\n").split(",")
    if(id not in emp):
        emp[id]={"id":id,"name":name,"designation":des,"salary":sal}

def fetchdata(**kwargs):
    id=str(kwargs["id"])
    if(id not in emp):
        print("employee not exist")
    else:
        print(emp[id]["name"])
        if "prop" in kwargs:
            val=kwargs["prop"]
            print(emp[id][val])

fetchdata(id=10001,prop="salary")















# def fetchdata(**kwargs):
#     try:
#         id=str(kwargs["id"])
#         prop=kwargs["prop"]
#         if(id not in emp):
#             print("employee not exist")
#         else:
#             print(emp[id]["name"],emp[id][prop])
#     except:
#         print(emp[id]["name"])