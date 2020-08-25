#reduce code


# lambda
# map
# filter
# listcomprehen
#reduce

# lambda functions also called anonymous function
# f=lambda num1,num2 :num1*num2
# print(f(9,67))

# map-used in where all objects need an alteration
#filter-used in where only some objects have to be altered
def square(num):
    return num*num
lst=[1,2,3,4]
sq=list(map(square,lst))
print(sq)

lst2=[1,2,3,4,5,6,7]
def even(num):
    return num%2==0

evens=list(filter(even,lst))
print(evens)



