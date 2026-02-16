print("calculator")
num1=float(input("enter a number"))
num2=float(input("enter a number"))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice=int(input("enter your choice(1/2/3/4)"))
if choice==1:
    print(num1+num2)

elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    if num2!=0:
        print(num1/num2)
    else:
        print("Error! division by zero")

else:
    print("Invalid number")