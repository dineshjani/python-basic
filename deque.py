# importing the collections library  
# for deque operations  
import collections  
  
# declaring the deque  
my_deque = collections.deque([10, 20, 30, 40, 50])  
  
# using the append() function to add   
# data element at right end  
# inserting 60 at the end of the deque  
my_deque.append(60)  
  
# printing the resultant deque  
print( "The deque after appending at right: " )  
print( my_deque )  
  
# using the appendleft() function to add  
# data element at left end  
# inserting 70 at the starting of the deque  
my_deque.appendleft(70)  
  
# printing the resultant deque  
print( "The deque after appending at left: " )  
print( my_deque )  
  
# using the pop() function to remove  
# data element from the right end  
# removing 60 from the right end of deque  
my_deque.pop()  
  
# printing the resultant deque  
print( "The deque after removing from right: " )  
print( my_deque )  
  
# using the popleft() function to remove  
# data element from the left end  
# removing 70 from the left end of deque  
my_deque.popleft()  
  
# printing the resultant deque  
print("The deque after removing from left: " )  
print( my_deque )  
my_deque.rotate(-4)
print("After rotation operation the deque is : ")
print(my_deque)