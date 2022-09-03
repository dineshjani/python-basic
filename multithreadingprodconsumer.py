from threading import Thread
import threading
from queue import Queue

def producer(q):
    print(threading.get_ident())
    for i in range(5):
        q.put(i)
        print("published",i)
    

def consumer(q):
    print(threading.get_ident())
    
    while True:
        data=q.get()
        print("consumed",data)

q=Queue()

producer_thread=Thread(target=producer,args=(q,))

consumer_thread=Thread(target=consumer,args=(q,))
consumer_thread.start()
producer_thread.start()


#asyncio.run crates a event loop and push a coroutine to that loop.
# asyncio.run(coroutine)    only i user level thread
# now event loop work as a javascript
# multithreading handle by os but asyncio handle by us
#loop.createtask() register a coroutine on loop
https://medium.com/dev-bits/a-minimalistic-guide-for-understanding-asyncio-in-python-52c436c244ea
