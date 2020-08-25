f=open("covid_19_india.csv","r")
dict={}
dict2={}
for lines in f:
    data = lines.rstrip("\n").split(",")
    state=data[3]
    death=data[7]
    confirmed=data[8]
    if state not in dict and state not in dict2:
        dict[state]=death
        dict2[state]=confirmed
    else:
        dict[state]=death
        dict2[state]=confirmed
dsum=0
csum=0
d_lst=[]
c_lst=[]
for k,v in dict.items():
    d_lst.append(int(v))
    dsum+=int(v)
    print(k,v)
for k,v in dict.items():
    if(max(d_lst)==int(v)):
        print("\nHighest death rate in :",k,v)

for k,v in dict2.items():
    c_lst.append(int(v))
    csum+=int(v)
for k,v in dict2.items():
    if(max(c_lst)==int(v)):
        print("Highest confirmed cases in :",k,v)

print("Total death :",dsum)
print("Total confirmed cases :",csum)



