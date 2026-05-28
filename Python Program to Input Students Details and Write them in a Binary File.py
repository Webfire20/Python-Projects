
import pickle
with open('stu.txt', "ab") as file:
    No_of_students=int(input("Enter the no of students who's data you want to enter: "))
    Dict=[]
    for i in range(No_of_students):
        Student_name=input("Enter Student's name: ")
        Student_rollno=input("Enter Student's rollno: ")
        Student_marks=input("Enter Student's marks: ")
        Student_grade=input("Enter Student's grade: ")
        Dict['Rollno']=Student_rollno
        Dict['Name']=Student_name
        Dict['Marks']=Student_marks
        Dict['Grade']=Student_grade
        pickle.dump(Dict,file)
        print()
    print('Successful!')

