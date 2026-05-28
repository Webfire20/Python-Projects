## FUNCTIONS ##
import csv
def display():
     fin = open('furdata.csv','r')
     r=csv.reader(fin)
     for i in r:
          print(i)
     fin.close()

def ADD():
     fout = open('furdata.csv','a')
     w=csv.writer(fout)
     fid=input('Enter Item Code: ')
     fname=input('Enter Product Name: ')
     fprice=int(input('Enter Product Price: '))
     lst=[fid,fname,fprice]
     w.writerow(lst)
     fout.close()

def COUNTR():
     fin = open('furdata.csv','r')
     r=csv.reader(fin)
     n=input('Enter the Item Code: ')
     for i in r :
          if i[0]==n:
               print(i)
          else:
               print(end='')
     fin.close()

## MAIN ##
def menu():
     while True :
          print()
          print("Menu For CSV")
          print("👉   1. Display")
          print("👉   2. Add")
          print("👉   3. Search")
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
menu()