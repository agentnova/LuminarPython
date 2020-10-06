f=open("file.csv","r")
dict={}
for lines in f:
    data = lines.rstrip("\n").split(",")
    confirm = data[4]
    state = data[1]
    recovered = data[6]
    death = data[5]
    if (state not in dict):
        dict[state] = {"confirmed": confirm, "recovered": recovered, "death": death}
    else:
        dict[state] = {"confirmed": confirm, "recovered": recovered, "death": death}

def Fetchdata(**kwargs):
    if(kwargs["state"] not in dict):
        print("No result found")
    else:
        for k,v in dict.items():
            if(k==kwargs["state"]):
                print("Total confirmed cases : ",v["confirmed"])
                if("param" in kwargs):
                    val=kwargs["param"]
                    if(val in v):
                        print(val,":",v[val])




Fetchdata(state="Kerala",param="recovered")