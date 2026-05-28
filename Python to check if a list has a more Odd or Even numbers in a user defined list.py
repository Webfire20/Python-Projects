#Creating a List
List = []
print("Initial List: ")
print(List)
a=int(input('Enter number of values to be inserted : '))
# Addition of Elements in the List
for i in range(0,a):
    x=int(input('Enter value: '))
    List.append(x)
print('List after addition of values',List)
##__main__##
len_Odd=0
len_Even=0
for i in List:
    if i % 2 == 0:
        len_Even += 1
    else:
        len_Odd += 1
if len_Even > len_Odd:
    print("The list has more Even numbers.")
    print('Even numbers--->',len_Even)
    print('Odd numbers--->', len_Odd)
elif len_Even == len_Odd:
    print("The list has Equal Even and Odd numbers.")
    print("Even numbers---> ",len_Even)
    print('Odd numbers--->',len_Odd)
else:
    print("The list has more Odd numbers.")
    print('Odd numbers--->',len_Odd)
    print('Even numbers--->',len_Even)
