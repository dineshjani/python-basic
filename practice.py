# print("hello world");
# a = 1 + 2 + 3 + \
#     4 + 5 + 6 + \
#     7 + 8 + 9
# print(a)
# sum=0;
# for i in range(1,11):
#     print(i)
#     if i%2==0:
#         sum=sum+i
#         if i>6:
            #print("try")
            
#print(sum)
"""perfect example of
   ghghg"""


# p=2
# print(p=="2")
# 
# if p>0:
#     print("pos")
# elif p<0 :
#     print("neg")
# else :
#     print(0)
# 
# def greet(a):
#     print("hello paxcom",a)
#     return a;
#   
# p=greet(2)
# print(p)
# marks =[1,2,3,4]
# print(len(marks))

# languages=["hindi","japani","chaines"]
# print(languages[0:])
# languages[4:]=["ravI"]
# print(languages[2])
from typing import List


languages=["hindi","japani","chaines"]
print(languages)
con=(set(languages))

# languages.insert(0,"ah")

print(con)
list1=[1,2,3,4]
print(list(map(lambda x:x*2,list1)));
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
my_tuple[1][0]=4
a=1;
b=2;
b,a=(a,b)  #swap number using touple
print(a,b)
print(my_tuple)

old_square={x:x**2 for x in range(11) if x%2==0}
list_square=(x**2 for x in range(11) if (x%2==0 and x>3))

print(type(list_square))
#print(next(list_square))
#print(next(list_square))
#print(old_square)
#print(list_square)
print(sum(x**2 for x in list_square))
#print([float(input("Enter side "+str(i+1)+" : ")) for i in range(3)])


#my_list = [[1], [2, 3], [4, 5, 6, 7]]

#flat_list = [num for sublist in my_list for num in sublist]
#print(flat_list)

'''
class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result

#p=iter(PowTwo())      
#print(next(p))

def fib():
   prev,cur=0,1
   while True:
      yield cur
      prev=cur
      cur=cur+prev

p=fib()   
print("generator function1",next(p))
print("generator function2",next(p))

'''

x = "global"   #string
print("before update call id of x",id(x),x)
list=[2]       #list
x=x*2
print("before fun call id of x",id(x),x)

def foo(x):
    x=x*2
    list.append(2)
    print(id(x))
    print("fun id of list",id(list),list)
    print("fun id of x",id(x),x)
    

foo(x)
print("outside id of x",id(x),x)        #both x pointing to different id/address  call by value 
print("outside id of list",id(list),list)   #both list pointing to same id/address call by reference

list=[]
