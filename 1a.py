choice  = int(input("Enter the choice \n 1.addtion \n 2.subtraction \n 3.multiplication \n 4.division \n choice :"))
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
if choice ==1:
    print("Addtion of two numbers",a+b)
elif choice ==2:
    print("subtraction of two numbers is ",a-b)
elif choice ==3:
    print("multiplication of two numbers ",a*b)
elif choice ==4:
    print("division of two numbers ",a/b)
else :
    print("you entered wrong choice")

