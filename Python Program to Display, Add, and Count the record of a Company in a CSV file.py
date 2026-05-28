## FUNCTIONS ##
import csv
def display():
     fin = open('record.csv','r',newline="\n")
     r=csv.reader(fin)
     for i in r:
          print(i)
     fin.close()
     
def ADD():
     fout=open("record.csv","a",newline="\n")
     wr=csv.writer(fout)
     empid=input("Enter Employee id :: ")
     name=input("Enter name :: ")
     mobile=int(input("Enter mobile number :: "))
     lst=[empid,name,mobile]
     wr.writerow(lst)
     fout.close()

def COUNTR():
     fin=open("record.csv","r",newline="\n")
     data=csv.reader(fin)
     d=list(data)
     print(len(d)-1
           )
     fin.close()

     
## MAIN ##
while True :
     print()
     print("Menu For Company Records")
     print("👉   1. Display")
     print("👉   2. Add")
     print("👉   3. Count")
     print("👉   4. Exit")
     choice=input("Enter your choice: ")
     print()
     if choice=='1':
          display()
     elif choice=='2':
          ADD()
     elif choice=='3':
          COUNTR()
     elif choice=='4':
          print("Exiting")
          break
     else:
          print("Exiting")
          print("Wrong Input")
          break

