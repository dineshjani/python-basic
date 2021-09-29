x=6     #first line of x
x=x+2    #second line of x
print(id(x))
def foo():
    y=20       # first line of y
    #x=20
    global x
    x=x+5      #THIRD line of x
    print(id(x))
    def bar():
        global x  
        print(id(x))  # look gor global x if x is not peresent in global then give error and same address as a global x address
        nonlocal y    
        print(id(y))  #serach y in outer scope of this function not global take a next line of y in outer function
        y=y+3         # second line of y
        x=x+3   # take as a next line of global x only change in global x      fourth line of x
        print(id(x))
    
     
    print("Before calling bar: ", x,id(x))
    print("Calling bar now")
    bar()
    print("value of y",id(y),y)
    print("After calling bar: ", x,id(x))

foo()
print("x in main: ", x,id(x))