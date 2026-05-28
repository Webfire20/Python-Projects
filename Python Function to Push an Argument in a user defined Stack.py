## Function To Push Arrgument in a Use defined Stack ##
def PUSH(Arr):
    stack=[] 
    for i in range(0, len(Arr)): 
        if Arr[i]%5==0:  
            stack.append(Arr[i]) 
    if len(stack)==0: 
        print("Stack is Empty") 
    else: 
        print(stack)
##__main__##
Arr=[]
n=int(input('Enter the no. of enteries to be listed: '))
for i in range(0,n):
     a=int(input('Enter value: '))
     Arr.append(a)
PUSH(Arr)
