def armstrong_number(x):
 s=0
 z=x
 while x>0:
  y=x%10
  s=y**3+s
  x=x//10
 if s==z:
  print("is armstrong no.")
 else:
  print("is not")
x=int(input())
number=armstrong_number(x)
print(number)

