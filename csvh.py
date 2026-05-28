'''import csv
def Add():
    a=open('student.csv','a')
    x=csv.writer(a)
    c=input('y/n')
    h=['Roll','Name','Marks']
    b=x.writerow(h)
    while c=='y':
        q=int(input('rollno'))
        w=input('name')
        e=int(input('enter marks'))
        z=[q,w,e]
        c=input('y/n')
        b=x.writerow(z)
Add()
def dis():
    a=open('student.csv','r')
    b=csv.reader(a)
    for i in b:
        print(i)
dis()        
'''
ph='1134567895'
i=0
while i<3:
    if len(ph)!=10:
        i+=1
        print('cannot be added')
    else:
        print('hola comostas')
