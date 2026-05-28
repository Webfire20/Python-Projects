file=open("Marks.txt",'r')
c=file.read()
print(c)
for i in file:
    print(i)
file.close()
file=open("Marks.txt", "a")
no_of_std=int(input("Enter The No Of Students: "))
print()
for i in range(no_of_std):
    STD= str(i+1)
    Rollno=int(input("Enter roll no of student "+ STD +": "))
    name=input("Enter name of student "+ STD + ":")
    Marks=int(input("Enter Marks of student "+ STD + ": "))
    data=str(Rollno)+' '+name+', '+str(Marks)+','+ '\n'
    file.write(data)
    print()
print("Successfully Appended data!")
file.close()

