from queue import Queue,LifoQueue,PriorityQueue
s=Queue()
for j in range(5):

    s.put(j)
while not s.empty():
    print(s.get())

print("ENDs")


q=LifoQueue()
q.put(10)
q.put(5)
q.put(20)
q.put(15)
while not q.empty():
     print(q.get(),end=' ')

   
t=PriorityQueue()
t.put((1,"AAA"))
t.put((3,"CCC"))
t.put((2,"BBB"))
t.put((4,"DDD"))
while not t.empty():
    print(t.get()[1],end=' ')