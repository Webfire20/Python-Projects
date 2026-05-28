def menu():
     while True :
          print()
          print("Menu For CSV")
          print("👉   1. Display")
          print("👉   2. Replace")
          print("👉   3. Exit")
          choice=input("Enter your choice: ")
          print()
          if choice=='1':
               display()
          elif choice=='2':
               replace()
          elif choice=='3':
               print("Exiting")
               break
          else:
               print("Exiting")
               print("Wrong Input")
               break
def display():   
     with open('poem.txt','r')as file:
          c=file.read()
          print(c)
          print()
def replace():
     with open('poem.txt','r')as file:
          c=file.read()
          a=input('Enter value to be replaced: ')
          b=input('Enter value to replce: ')
     c=c.replace(a,b)
     with open('poem.txt','w')as file:
          file.write(c)
          print('Text has been replaced')     
menu()
