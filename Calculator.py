print("--------------------------------------BASIC CALCULATOR------------------------------------------------")
print("Press '1' for ADDITION\nPress '2' for SUBTRACTION\nPress '3' for MULTIPLICATION")
print("Press '4' for DIVISION\nPress '5' for EXPONENTIAL OPERATION\n")
print("------------------------------------------------------------------------------------------------------")
num1 = float(input("Enter first operand: "))
num2 = float(input("Enter second operand: "))
choice = int(input("Enter your choice(1-5): "))
if (choice==1):
    add = num1 + num2
    print(num1,"+",num2,"=",add)
    print("***************************************************************************")
elif (choice==2):
    sub = num1 - num2
    print(num1,"-",num2,"=",sub)
    print("***************************************************************************")
elif (choice==3):
    mult = num1 * num2
    print(num1,"x",num2,"=",mult)
    print("***************************************************************************")
elif (choice==4):
    div = num1 / num2
    print(num1,"/",num2,"=",div)
    print("***************************************************************************")
else:
    exp = num1 ** num2
    print(num1,"raised to the power",num2,"=",exp)
    print("***************************************************************************")
