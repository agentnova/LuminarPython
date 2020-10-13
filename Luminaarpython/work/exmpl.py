x=int(input("enter num : "))
for i in range(x,0,-1):
    for j in range(0, x-1-i):
        print(end=" ")
    for j in range(0, i):
        print("* ", end="")
    print()

