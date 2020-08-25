lst = [7, 4, 1, 2, 3]
num = int(input("enter the number to search :"))
s_lst = sorted(lst)
lower = 0
upper = len(lst) - 1
middle = (lower + upper) // 2
flag = 0
while (lower <= upper):
    middle = (lower + upper) // 2
    if (num > s_lst[middle]):
        lower = middle + 1
    elif (num < s_lst[middle]):
        upper = middle - 1
    else:
        flag += 1
        break
if (flag > 0):
    print("number found")
else:
    print("not found")
