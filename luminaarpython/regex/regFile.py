from re import *
f=open("regno.txt","r")
rule='[Kk][Ll][0-9]{2}[a-z]{2}\d{4}'
lst=[]
for data in f:
    lines=data.rstrip("\n")
    matcher=fullmatch(rule,lines)
    if matcher!=None:
        lst.append(lines)
print(lst)

