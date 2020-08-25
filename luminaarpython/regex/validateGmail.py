from re import *
rule="\w*[@]gmail.com"
mail=input("enter the mail id :")
matcher=fullmatch(rule,mail)
if(matcher!=None):
    print("valid mail id")
else:
    print("invalid mail id")