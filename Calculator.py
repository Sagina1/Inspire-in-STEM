#!usr/bin/python
################
# Making a calculator
#Name: Yvonne Sagina
###################
# make a simple calculator 
#define the functions
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b 

def multiply(a,b):
    return a * b

def divide(a,b):
    return a/b

print(""" To add enter 1,
       to subtract enter 2,
       to multiply enter 3,
       to divide enter 4.""")

user_input = int(input("Enter the operator you want"))
if user_input == 1:
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    answer = add(a,b)
    print("The sum of the numbers is" +str(answer))

elif user_input == 2:
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    answer = subtract(a,b)
    print("The difference of the numbers is" +str(answer))

elif user_input == 3:
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    answer = multiply(a,b)
    print("The product of the numbers is" +str(answer))

elif user_input == 4:
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    answer = divide(a,b)
    print("The quotient of the number is" +str(answer))
else:
    print("Not in range")