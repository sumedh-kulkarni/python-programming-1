#factorial of a number
#NIMISH GEDAM
#M46
def factorial(n): #function_defination
 f=1
 if n<0:
  print('enter valid no.')
 elif n==0 or n==1:
  print(1)
 else:
  while n>1:
   f=f*n
   n=(n-1)
  print(f)
n=int(input())
factorial(n)
