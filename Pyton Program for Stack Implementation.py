#####FUNCTIONS#####
def isempty(stack): 
    if stack==[]:
        return True 
    else:
        return False
def Push(stack,item):
    global top
    stack.append(item) 
    top=len(stack)-1
def Pop(stack):
    global top 
    if isempty(stack): 
        return "Underflow"
    else:
        popped_item= stack.pop()
        if len(stack)==0:
            top=None
        else:
            top=len(stack)-1 
            return popped_item
def Peek(stack): 
    global top 
    if isempty(stack): 
        return "Underflow" 
    else:
        top=len(stack)-1 
        return stack[top]
def Display(stack): 
    global top 
    if isempty(stack):
        return "Underflow"
    else:
        top= len(stack)-1
        print('Top',stack) 
        for i in range(top,1,1):
            print(stack[i])
##__________________main___________________________##

stack=[]
top=None
while True :
    print()
    print("Stack project")
    print("1. Push")
    print("2. Pop")
    print("3 Peek")
    print("4 Display")
    print("5 Exit")
    choice=input("Enter your choice: ")
    print()
    if choice=='1':
        n=int(input('Enter no. of entries to insert: '))
        for i in range(0,n):            
            item=int(input("Enter your Item :"))
            Push(stack,item)
    elif choice=='2':
        item_popped=Pop(stack) 
        if item_popped=="Underflow":
            print("Underflow error!")
            print() 
        else:
            print("Just popped ",item_popped)
            print()
    elif choice=='3':
         item=Peek(stack)
         if item=="Underflow":
            print("Underflow error!")
            print()
         else:
            print("The Top item is: ", item) 
            print()
    elif choice=='4':
        Display(stack)
    elif choice=='5':
        print("Exiting")
        print("Done")
        print()
        break
    else:
        print("Exiting")
        print("Wrong Input")
        break
