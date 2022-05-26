#!usr/bin/python
#for loops
#26th May 2022
#Crunchy biscuit

for number in range (0,20):
    print(number)
 # even numbers
for number in range (0,20):
    if(number %2==0):
      print(number)
 # sum of all even numbers between 0 and 50
sum = 0
for number in range (0,20):
    if(number %2 == 0):
        sum = sum + number
        print(number)
print(sum)
# product of all odd numbers between 1 and 10
product = 1
for number in range(1,20):
    if(number %2==1):
        product = product * number
        print(number)
print(product)        
# while 0 to 9
number = 0
while number < 10:
    print(number)
    number = number + 1


num = 0
while num< 10:
    num = num + 1
    if(num % 2 == 0):
        print(num)
