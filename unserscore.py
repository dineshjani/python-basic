#The python interpreter stores the last expression value to the special variable called ‘_’
a=10
print(a)

x, _, y = (1, 2, 3)
print(_)

x, *_, y = (1, 2, 3, 4, 5) # x = 1, y = 5  
print(_)
for _ in range(10):
    print(_)   
    