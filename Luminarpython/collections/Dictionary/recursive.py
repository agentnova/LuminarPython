pattern="BABABAC"
a={}
for char in pattern:
    if char not in a:
        a[char]=1
    else:
        print("first recursive character is ",char)
        break
