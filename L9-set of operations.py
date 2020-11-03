# set of operators allowed in expression
Operators=set(['','-','+','%','/','*'])
def evaluate_postfix(expression):
# empty stack for storing numbers    
    stack=[] 
    for i in expression:
        if i not in Operators:
            stack.append(i) #This will contain numbers
        else:
            a=stack.pop() 
            b=stack.pop()
            if i=='+':
                res=int(b)+int(a) 
            elif i=='-':
                res=int(b)-int(a)    
            elif i=='*':
                res=int(b)*int(a)
            elif i=='%':
                res=int(b)%int(a) 
            elif i=='/':
                res=int(b)/int(a)
            elif i=='**':
                res=int(b)**int(a)
 # final result                
            stack.append(res) 
    return(''.join(map(str,stack)))
expression = input('Enter the postfix expression ')
print()
print('postfix expression entered: ',expression)
print('Evaluation result: ',evaluate_postfix(expression))
