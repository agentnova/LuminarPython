a=(10,"hello",True)
print(a)

# duplicate allowed
# insertion order presered
# immutable
# can store multiple types of values

from functools import *
y=list(filter(lambda x:x<4,[1,2,3,4,5]))
print(y)
print(tuple(y))
