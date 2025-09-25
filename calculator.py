def add(n1,n2):
 return n1+n2
def sub(n1,n2):
 return n1-n2
def multi(n1,n2):
 return n1*n2
def div(n1,n2):
    if n2 == 0:  # Check for division by zero
        return "Error! Division by zero."
    return n1 / n2

print("Please select operation \n"
      "1.Add\n"
      "2.Subtract\n"
      "3.Multiply\n"
      "4.divide\n")
sel = int(input("Select operation(1,2,3,4):"))      #sel=select
n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))

if sel == 1:
 print(n1,"+",n2,"=",add(n1,n2))
elif sel == 2:
  print(n1,"-",n2,"=",sub(n1,n2))
elif sel == 3:
  print(n1,"*",n2,"=",multi(n1,n2))
elif sel == 4:
  print(n1,"/",n2,"=",div(n1,n2))
else:
 print("Invalid input")


 
