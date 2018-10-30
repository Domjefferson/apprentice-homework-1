def add (x, y):
    return x + y
def sub (x , y):
    return x - y
def mult(x , y):
    return x * y
def divflt (x ,y):
    return x / y
def divwhlint (x , y):
    return x // y
def expnt (x ,y):
    return x ** y
def modls(x ,y):
    return x % y

print("selected desired operation")
print ("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide and return decimal point")
print ("5.divide and return whole number")
print ("6.divde and return remainder")
print("7.exponent")

choice = input("Enter operation(1/2/3/4/5/6/7):")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    print(num1,"+",num2,"=", add (num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=", sub (num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=", mult (num1,num2))
elif choice =='4':
    print(num1,"/",num2,"=", divflt (num1,num2))
elif choice =='5':
    print(num1,"//",num2,"=", divwhlint (num1,num2))
elif choice =='6':
    print(num1,"%",num2,"=", modls (num1,num2))
elif choice =='7':
    print(num1,"to the power of",num2,"=", expnt (num1,num2))
else:
    print("please select an option from the menu")
###### let me know if theres a more effcient way to do it :)
