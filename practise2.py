acc_bal = input("What is your account balance")
print(acc_bal)
if (int(acc_bal>100000 and int(acc_bal<200000))):
    acc_bal= int(acc_bal) - 25000
    print("We have deducted 25000")
elif (int(acc_bal>200000 and int(acc_bal<500000))):
    acc_bal= int(acc_bal) - 30000
    print("We have deducted 30000")
elif (int(acc_bal>500000 and int(acc_bal<1000000))):
    acc_bal= int(acc_bal) - float(0.3)
    print("We have deducted 0.3 from your account")  
elif (int(acc_bal>1000000)):
    acc_bal= int(acc_bal) - 15000
    print("We have deducted 15000 from your account")          
else:
    print("You a not a viable candidate for deduction")