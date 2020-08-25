f=open("data2.txt","r")
dict={}


for word in f:
    words=word.rstrip(("\n")).split(" ")
    for w in words:
        if(w not in dict):
            dict[w]=1
        else:
            dict[w]+=1
for k,v in dict.items():
    print(k,",",v)