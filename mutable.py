x = "global"   #string
print("before update call id of x",id(x),x)
list=[2]       #list
x=x*2
print("before fun call id of x",id(x),x)

def foo(x,list):
    
    x=x*2
    list.append(2)
    
    print("fun id of list",id(list),list)
    print("fun id of x",id(x),x)
    

foo(x,list)          #?? mutable passed as a pass by reference but immutable not why??
print("outside id of x",id(x),x)        #both x pointing to different id/address  call by value 
print("outside id of list",id(list),list)   #both list pointing to same id/address call by reference
