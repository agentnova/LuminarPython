from threading import *
import time

def squares(num):
    for n in num:
        time.sleep(1)
        print(n**2)


def double(num):
    for n in num:
        time.sleep(1)
        print(2*n)

num=[1,2,3,4,5,6]
begintime=time.time()
print("bdegin",begintime)

t1=Thread(target=squares,args=(num,))
t1.start()
t2=Thread(target=double,args=(num,))
t2.start()

t1.join()
t2.join()

endtime=time.time()
print("end",endtime)
total=endtime-begintime
print("total time ",total)
