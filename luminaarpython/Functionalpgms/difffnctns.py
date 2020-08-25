# def add(num1,num2):
#     return num1+num2
#
# add(10,20)

# var length argument
# def printVal(name,location):
#     print(name)
#     print(location)
# printVal("hi","hello")

def add(**args):
    print(args)
    sum = 0
    for k, v in args.items():
        sum += v
    print("sum ", sum)



add(num1=10, num2=67, num3=45)
