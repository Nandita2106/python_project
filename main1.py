a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
print("choose an operation: +, -, *, /")
operation=input("enter an airthmetic operation:")

if (operation== '+'):
    result=(a+b)
    print("Result:", result)
elif (operation== '-'):
    result=(a-b)
    print("Result:", result)
elif (operation== '*'):
    result=(a*b)
    print("Result:", result)
elif (operation== '/'):
    if(b!=0):
     result=(a/b)
     print("Result:", result)
    else:
       print("Error! Division by zero is not allowed")

else:
   print("Invalid operation selected")       
 
   