#file operation
# to store data
# read r
# write w
# append a
# -----create file reference--------
# f=open("filepath","mode of operation")
f=open("data.txt","r")
for lines in f:
    print(lines)
