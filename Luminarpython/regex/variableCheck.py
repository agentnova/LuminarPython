#first char is an alphabet it should be a-k
# second should be a digit and it must be divisible by 3
# then any number of char
from re import *
rule='[a-k][369][a-zA-Z0-9]*'
varname=input("enter var name :")
matcher=fullmatch(rule,varname)
if(matcher!=None):
    print("valid")
else:
    print("invalid")