from threading import Thread
import threading
import time
import os
start =time.perf_counter()

def do_something(s):
    print("sleeping in {} second".format(s))
    time.sleep(s)
    print("Done something")

threads=[]
for i in range(10):
    t=threading.Thread(target=do_something,args=[i])
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()

finish =time.perf_counter()

print("finished in ",round(finish-start,2))
print(os.path.realpath(__file__))
print(os.path.abspath(__file__))
print(os.path.join(os.path.dirname(__file__),'configuration.conf'))
print(os.path.dirname(os.path.dirname(__file__)))
print(os.path.basename(__file__))

