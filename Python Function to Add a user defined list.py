## Function To Add a Use defined List ##
def listadd(a):
     sum=0
     for i in a:
          sum = sum + i
     print('Sum of list =', sum)
#__main__#
x=[]
n=int(input('Enter the no. of enteries to be listed: '))
for i in range(0,n):
     a=int(input('Enter value: '))
     x.append(a)
listadd(x)
