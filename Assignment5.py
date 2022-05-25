#!/usr/bin/python
#a list of vehicles
Cars = ["bmw","audi","toyota","mercedes","jeep"]
#print(Cars[4].upper())
#using a for loop to print all vehicles
#for Cars in Cars:
  #  if Cars == "bmw":
   #  print(Cars.upper())
#else:
 #   print(Cars.title())     

    #boyfriend for crunchybiscuit edition
gender = input("Are you male or female")
print("i am a"+ gender)
age = input("What is your age") 
print("i am" + str(age) + "years old")   
if ("gender == male") and ("age < 18"):
    print("sorry maybe next time")
elif("gender == male") and ("age > 18"):
    print("You are a qualified candidate")
elif("gender == female") and ("age is > 18"):
    print("we can consider you")
elif("gender == female") and ("age is < 18"):
    print("sorry maybe next time")
else:
    print("sorry better luck next time")    