x = "global"   #string
print("before update call id of x",id(x),x)
list=[2]       #list
x=x*2
print("before fun call id of list",id(list),list)

print("before fun call id of x",id(x),x)

def foo():
 #   print(x)  # we can read but cannot modify
  #  p =x*2            # here also not giving error
    global x
    print(id(x))
    x=x*2
    
    list.append(2)
    
    print("fun id of list",id(list),list)
    print("fun id of x",id(x),x)
    

foo()
print("outside id of x",id(x),x)        #both x pointing to different id/address  call by value 
print("outside id of list",id(list),list)   #both list pointing to same id/address call by reference

