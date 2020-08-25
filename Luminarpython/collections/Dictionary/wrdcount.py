line="hai hello hi hello"
words=line.split(" ")
dict={}


for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)


# for i in range(0,len(words)-1):
#     if words[i] not in dict:
#         dict[words[i]]=i+1
# print(dict)

