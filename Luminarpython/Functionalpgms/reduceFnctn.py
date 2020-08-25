import functools
lst=[30,20,10,31,32]
# 10,20-----10+20
# 30,30----30+30
# 60,31----60+31
# 91,32----91+32
total=functools.reduce(lambda num1,num2:num1+num2,lst)
print("Total ",total)
max=functools.reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print("Maximum ",max)
min=functools.reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print("Minimum ",min)