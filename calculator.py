
print("+")
print("-")
print("*")
Print("/")
Print("selector")
choice=input("enter +/-/*//")
a=int(input("enter a num 1: "))
b=int(input("enter a num 2: "))
def add(a,b):
   return a+b
def sub(a,b):
   return a-b
def multiply(a,b):
   return a*b
def division(a,b):
  if b==0:
     print("invalid value")
  else:
     return a/b
if choice=="+":
   print(add(a,b))
elif choice =="-":
  print(sub(a,b))
elif choice =="*":
 print(multiply(a,b))
elif choice =="/":
 print(division(a,b))
else:
  print(" invalid")
