byear = int(input("enter the year of birth :"))
bmonth = int(input("enter the birth month :"))
bday = int(input("enter the birth day :"))

cyear = int(input("enter the current year :"))
cmonth = int(input("enter the current month :"))
cday = int(input("enter the current day :"))

age = cyear - byear

if(bmonth>cmonth):
    age-=1
elif(bmonth==cmonth)&(bday>cday):
    age-=1
print("you are", age, "years old")
