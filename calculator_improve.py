def operationonStack(cur,prev,stack,sign):
    
    if(sign=='*'):
        stack.append(float(cur)*prev)
    else:
        stack.append(prev/float(cur))

def calculator_logic(input_string):
    str_length=len(input_string)
    stack=[]
    cur=""
    sol_muldiv_first=False
    for j in range(str_length):
        
        if (input_string[j]=='+' or input_string[j]=='-' or input_string[j]=='*' or input_string[j]=='/'):
            if(sol_muldiv_first==True):    
                operationonStack(cur,prev,stack,sign)
                if(input_string[j]=='*' or input_string[j]=='/'):
                    prev,sol_muldiv_first,sign=stack.pop(),True,input_string[j]
                if(input_string[j]=='+' or input_string[j]=='-'):
                    stack.append(input_string[j])
                    sol_muldiv_first=False
            else:
                if(input_string[j]=='*' or input_string[j]=='/'):
                    prev,sol_muldiv_first,sign=float(cur),True,input_string[j]
                if(input_string[j]=='+' or input_string[j]=='-'):
                    stack.append(cur)
                    stack.append(input_string[j])

            cur=""
        else:
            
            cur=cur+input_string[j]
    if(sol_muldiv_first==True):
        operationonStack(cur,prev,stack,sign)            
    else:
        stack.append(cur)                
                    
    sum=0;
    addorminus_sign=1;
    for i in range(len(stack)):
        element=stack[i]
        if(element=='+'):
            addorminus_sign=1
        elif(element=='-'):
            addorminus_sign=-1
        else:
            sum=sum+addorminus_sign*float(element)    
    return sum
  

print("Enter String For Calculation")
input_string=input()
result=calculator_logic(input_string)
print("Result",result)    