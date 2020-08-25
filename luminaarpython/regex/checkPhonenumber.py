# validate phone number
from re import *
rule='\d{10}'
num=input("enter the number :")
matcher=fullmatch(rule,num)
if matcher!=None:
    print("Valid phone number")
else:
    print("invalid phone number")