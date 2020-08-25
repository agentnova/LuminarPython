import re
matcher=re.finditer("ab","ababababababababababab")
print(matcher)
count=0
for match in matcher:
    print(match.start())    #position
    print(match.group())    #searching pattern/word
    count+=1
print("total number of pattern",count)