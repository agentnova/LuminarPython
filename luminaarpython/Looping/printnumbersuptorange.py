#print numbers upto a range
low=int(input("enter lower limit :"))
limit=int(input("enter higher limit :"))

while(low<=limit):
    if(low%2==0):
        print(low)
    low+=1