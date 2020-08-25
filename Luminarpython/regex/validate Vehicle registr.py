# validate all vehicle registration number
from re import *
rule='[Kk][Ll][0-9]{2}[a-z]{2}\d{4}'
regno=input("Enter the vehicle number :")
matcher=fullmatch(rule,regno)
if not matcher==None:
    print("Valid")
else:
    print("invalid")