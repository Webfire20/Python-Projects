
num=float(input("Enter a number: "))
a=input("Enter the unit in which you want to convert the number(m or km): ")
x=a.lower()
if x=="m":
    print("The given kilometers in miles is: ", num*0.62)
elif x=="km":
    print("The given kilometers in miles is: ", num*1.6)
else:
    print("Wrong Unit")
