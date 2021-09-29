y="ght"
def outer():
    x = "local"

    def inner():
        global x
        global y
        y="global"
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)
    print("outerg:", y)


outer()
print(y)


def func_outer():
    
    a = "local"
    def func_inner():
        
        #nonlocal a
        a = "nonlocal"
        print("inner:", a)
    func_inner()
    print("outer:", a)
    
func_outer()
