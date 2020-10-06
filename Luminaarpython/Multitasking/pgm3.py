from threading import *
class Mythread(Thread):
    def run(self):
        for i in range(1,10):

            print(i)
        print(current_thread().getName())

t=Mythread()

t.start()
for i in range(1,10):
    print(i)
print(current_thread().getName())


# after connecting print connect:[clnt name]
# then message send message:[msg] each of the client
# print disconnect:[clnt name]


# client
# input login name
# send connct msg to servr
# loop message input
# send msg to server

# send disconnect message through exit