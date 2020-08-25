f=open("covid_19_india.csv","r")
dict={}
d_lst=[]
for lines in f:
    data = lines.rstrip("\n").split(",")
    state=data[3]
    death=data[7]
    if state not in dict:
        dict[state]=death
    else:
        dict[state]=death

for k,v in dict.items():
    d_lst.append(int(v))
for k,v in dict.items():
    if(max(d_lst)==int(v)):
        print("\nHighest death rate in :",k,v)
