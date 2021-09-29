def netfliex(c,*check):
    print(check)
    print(c)
    print(type(check))

#netfliex("ram","rahim","bhism")  

def netfliex1(c,*check,d,**e):
    print(check)
    print(d)
    print(c)
    print(type(check))
    print(e)

#netfliex1("ram","rahim","bhism",d="ravi",ram="sita",shiv="parwati") 

#sugar syntax

add=lambda a,b,c:a+b+c 
p=add(1,2,3)
print(p)

def listcheck(c,d,e):
    for i in range(len(c)):
        print(c[i])
    print(d)
    print(e)    

#listcheck([1,2,3],4,5)





#only on time default agument execute hote ha function declared ke time