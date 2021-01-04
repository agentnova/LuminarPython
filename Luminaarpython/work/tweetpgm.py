from work.tweet import *

count=int(input("How many tweets : "))
for i in range(0,count):
    name=input("enter name ")
    tweet=input("Enter tweet ")
    writetweet(name,tweet)

tweets=readtweet()
dict={}
for item in tweets:
    name,tweet=item.split(" ")
    if name not in dict:
        dict[name]=1
    else:
        dict[name]+=1

for k,v in dict.items():
    print(k,v)
