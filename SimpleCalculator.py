#simple Calculator
#init
#functions
#This function adds two numbers together and prints them both
def add(num1,num2):
    result = num1+num2
    print(result)
def subtract(num1,num2):
    result = num1-num2
    print(result)
def multiply(num1,num2):
    result = num1*num2
    print(result)
def divide(num1,num2):
    result = num1/num2
    print(result)

#main
while True:
    print("Welcome to simple calculator")
    print("Please select an operation:")
    print("""1.Add
2.Subtract
3.Multiply
4.Divide
5.Quit""")
    operation = int(input("(1-5) Option:"))
    if operation == 1:
        int1 = int(input("Enter the first number you would like to add"))
        int2 = int(input("Enter the second number you would like to add"))
        add(int1,int2)
    if operation == 2:
        int1 = int(input("Enter the first number you would like to subtract"))
        int2 = int(input("Enter the second number you would like to subtract"))
        subtract(int1,int2)
    if operation == 3:
        int1 = int(input("Enter the first number you would like to multiply"))
        int2 = int(input("Enter the second number you would like to multiply"))
        multiply(int1,int2)
    if operation == 4:
        int1 = int(input("Enter the first number you would like to divide"))
        int2 = int(input("Enter the second number you would like to divide"))
        divide(int1,int2)
    if operation == 5:
        break
