import heapq

que=[]
que.append((5,'Medium priority task'))
que.append((1,'High priority task'))
que.append((10,'Low priority task'))


que.sort(reverse=True)
print("Tasks with their priorities :")
#looping through sorted list
while que:
    queue_item=que.pop()
    print(queue_item)

# declaring empty list
que = [] # adding elements to the list
heapq.heappush(que, (5, 'Medium Priority task'))
heapq.heappush(que, (1, 'High priority task'))
heapq.heappush(que, (10, 'low priority task'))
# dequeuing elements
print("Elements will be dequeued according to their prorities")
while que:
    deque_item = heapq.heappop(que)
    print(deque_item)

import os
curworkdir =os. getcwd()
print ("The current working directory is", curworkdir)    