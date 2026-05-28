import pickle
def Add():
    z=open('student.dat','ab')
    roll=int(input('enter roll number'))
    name=input('enter name')
    marks=int(input('enter marks'))
    l=(roll,name,marks)
    pickle.dump(l,z)
    z.close()
    
def Display():
    z= open('student.dat','rb')
    x=pickle.load(z)
    for i in x:
        print(i)
    
a=open ('student.dat','ab')
while True:
    ch=int(input('1 for adding record \n 2 for display \n 3 for exiting'))
    if ch==1:
        Add()
        print('adding')
    elif ch==2:
        Display()
        print('done')
    elif ch==3:
        print('exiting')
        break
        
