f=open("movies.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    movies=data[1]
    rating=data[3]
    if(rating not in dict):
        dict[rating]=1
    else:
        dict[rating]+=1
for k,v in dict.items():
    print("rating",k,"-",v,"Movies")