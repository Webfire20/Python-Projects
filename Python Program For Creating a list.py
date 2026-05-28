#__main__
#Creating a List
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements in the List
n=int(input('Enter number of enteries to be listed : '))
for i in range(0,n):
     a=int(input('Enter value: '))
     List.append(a)
print("\nList after Addition of ",n,"elements: ")
print(List)
import random
print(" Adding elements to the List using Iterator ")
x=int(input('Enter value: '))
for i in range(0, x):
     o=random.randint(i,x)
     List.append(o)
print("\nList after Addition of elements from 0",n)
print(List)

print("Adding Tuples to the List")
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)
