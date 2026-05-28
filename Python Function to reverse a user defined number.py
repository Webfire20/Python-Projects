## Function To Reverse a Use defined Number ##
def reverse(i):
     rev=0
     while i>0:
          rev=(rev*10)+i%10
          i=i//10
     print('reverse = ',rev)
#__main__
i=int(input('Enter no = '))
reverse(i)
