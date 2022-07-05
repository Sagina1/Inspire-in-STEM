#!usr/bin/python
#################
#Geometric Progression
#Yvonne Sagina
##################
from ast import Str


a = int(input("Enter the first term"))
r = int(input("Enter the common ratio"))
n = int(input("Enter the number of terms"))
for i in range(1,n):
    nth_term = a*(r**(i-1))
    print("The nth_term is" +str(nth_term))

if r>1:
    sum_of_numbers_in_a_GP = (a*((r**n)-1))/(r-1)
else:
    sum_of_numbers_in_a_GP = (a*(1-(r**n)))/(1-r)
print(sum_of_numbers_in_a_GP)