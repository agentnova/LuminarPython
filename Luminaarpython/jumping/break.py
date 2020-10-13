for i in range(0,50):
    if(i==25):
        continue
    print(i)
print("outside loop")
for i in range(0,50):
    if(i==25):
        break
    print(i)
print("outside loop")