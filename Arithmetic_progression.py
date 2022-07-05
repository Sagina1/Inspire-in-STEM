#usr/bin/python
####################
#Arithmetic progressions
#Yvonne Sagina
#26/5/22


# n = a + (n-1)d
a = int(input("enter first number"))
d = int(input("common difference"))
n = int(input("nth term"))
for i in range (1,n+1):
    n_term = a + (i-1)*d
    print (n_term)

for i in range (1,n+1):
    sum_n = n_term/2(a+(i-1)*d)
    print(sum_n)  



