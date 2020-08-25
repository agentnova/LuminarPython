from re import *
# pattern="a+" #occurance of ,does not count other place
# pattern="a*" #occurance of a,check for other places too
# pattern="a?" #occurance of single a look for all places
# pattern="a{2}" #check 2 number of a
pattern="a{2,3}" #minimum2 a and max 3a
matcher=finditer(pattern,"abaabaaaacaadaaaaaaa")
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print(count)