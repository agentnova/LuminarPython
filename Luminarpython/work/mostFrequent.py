words="ABABABCAAA"
dict={}
lst=[]
for i in words:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
for k,v in dict.items():
    lst.append(v)
for j in dict:
    if(int(max(lst))==dict[j]):
        print("most fequent letter is ",j)

