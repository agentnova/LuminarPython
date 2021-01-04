
f = open("tweets.txt","a")

def writetweet(name,tweet):
   f.write(name+" "+tweet+"\n")
   f.flush()

f1=open("tweets.txt","r")
def readtweet():
    lst=[]
    for tweets in f1:
        tweet=tweets.rstrip("\n")
        lst.append(tweet)
    return lst





