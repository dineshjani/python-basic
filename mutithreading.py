from threading import Thread
import threading
import time

start =time.perf_counter()
def square(n):
    time.sleep(1)
    print(threading.get_ident())
    print("square is",n**2)

def cube(n):

    time.sleep(1)
    print("cube thraed")
  
    print(threading.get_ident())
    print("cube is",n**3) 

t1=Thread(target=square,args=(2,))
t2=Thread(target=cube,args=(4,))  

t1.start()
t2.start()
t1.join() 
t2.join()

#print("hello is bettwen so it is asynchronous")
finish =time.perf_counter()
print("finished in ",round(finish-start,2))


