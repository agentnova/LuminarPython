from re import *
f=open("mail.txt","r")
rule="\w*[@]gmail.com"
lst=[]
for data in f:
    lines=data.rstrip("\n")
    matcher=fullmatch(rule,lines)
    if matcher!=None:
        lst.append(lines)
print(lst)