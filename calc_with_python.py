class Calculator:
    def __init__(self,input_string): 
        self.input_string=input_string


    def operationOnStack(self,cur_element,prev_element,cur_stack,signOfOperation):
        
        cur_stack.append(float(cur_element)*prev_element) if signOfOperation=='*' else cur_stack.append(prev_element/float(cur_element))
        
    def evaluateStack(self,stack):                        
        result_sum=0;
        addorminus_sign=1;
        for index,get_element in  enumerate(stack):
            if(get_element=='+' or get_element=='-'):
                addorminus_sign=int(get_element+"1")
            else:
                result_sum=result_sum+addorminus_sign*float(get_element)    
        return result_sum


    def calculateMethod(self):
        input_string=self.input_string
        cur_stack=[]
        cur_element=""
        sol_muldiv_first=False
        for j,jthChar in enumerate(input_string):
            if (jthChar=='+' or jthChar=='-' or jthChar=='*' or jthChar=='/'):
                if(sol_muldiv_first==True):    
                    self.operationOnStack(cur_element,prev_element,cur_stack,signOfOperation)
                    if(jthChar=='*' or jthChar=='/'):
                        prev_element,sol_muldiv_first,signOfOperation=cur_stack.pop(),True,jthChar
                    else:
                        cur_stack.append(jthChar)
                        sol_muldiv_first=False
                else:
                    if(jthChar=='*' or jthChar=='/'):
                        prev_element,sol_muldiv_first,signOfOperation=float(cur_element),True,jthChar
                    else:
                        cur_stack.append(cur_element)
                        cur_stack.append(jthChar)

                cur_element=""
            else:
                
                cur_element=cur_element+jthChar

        if(sol_muldiv_first==True):
            self.operationOnStack(cur_element,prev_element,cur_stack,signOfOperation)            
        else:
            cur_stack.append(cur_element)                
        
        return self.evaluateStack(cur_stack)



calc_instace=Calculator(input())
print(calc_instace.calculateMethod())