#FUNCTION#
def nextNumber(Ist):
    new_list=[]
    for i in Ist:
        new_list.append(i+1)
    return new_list
##__main__##
#Creating a List
List = []
print("Initial List: ")
print(List)
a=int(input('Enter number of values to be inserted : '))
# Addition of Elements in the List
for i in range(0,a):
    x=int(input('Enter value: '))
    List.append(x)
print('List after addition of +1 successor of values',List)
#Calling Function
It=List
print("The new list is: ", nextNumber(It))
