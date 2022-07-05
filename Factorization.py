number = int(input("Enter the number"))
print(number)
factorial = 1
if number < 0:
    print("factorial of negative number doesnt exist")
elif number == 0:
    print("factorial of 0 = 1")
else:
    for i in range (1,number +1):
        factorial = factorial *i
print("factorial of",number,"is",factorial)