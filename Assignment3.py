Gender = input("input whether male or female")
print("i_am_a" +Gender)
Age = input("What is your age")
print("i_am" +str(Age) + "years old")
acc_bal = 100
if (int(Age) >25) and (int(Age) <30):
    acc_bal = acc_bal+ 10000
    print("Confirm you have received ksh 10000")
else:
    print("sorry no money for you")



