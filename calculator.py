stack=[]
p=input()
n=len(p)
cur=""
e=False
for j in range(n):
    
    if (p[j]=='+' or p[j]=='-' or p[j]=='*' or p[j]=='/'):
       
       
        if(e==True):
            if(sign=='*'):
                cur=float(cur)
                prev=float(prev)
                
                x=cur*prev
                stack.append(x)
            if(sign=='/'):
               
                cur=float(cur)
               
                prev=float(prev)
                x=prev/cur
                stack.append(x)    
        
            e=False
            if(p[j]=='*' or p[j]=='/'):
                prev=stack.pop()
                e=True
                sign=p[j]
            if(p[j]=='+' or p[j]=='-'):
                stack.append(p[j])
        else:
            if(p[j]=='*' or p[j]=='/'):
                prev=cur
                e=True
                sign=p[j]
            if(p[j]=='+' or p[j]=='-'):
                stack.append(cur)
                stack.append(p[j])

        cur=""
    else:
        
        cur=cur+p[j]
    

if(e==True):
            if(sign=='*'):
                x=float(cur)*float(prev)
                stack.append(x)
            if(sign=='/'):
                x=float(prev)/float(cur)
                stack.append(x)
else:
    stack.append(cur)                
                
sum=0;
print(type(stack))
si=1;
while(len(stack)):
    d=stack.pop()
    
    if(d=='+'):
        si=1
    
    elif(d=='-'):
        si=-1
    
    else:
        sum=sum+si*float(d)


print(sum)    