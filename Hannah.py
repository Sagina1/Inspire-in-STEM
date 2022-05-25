alcohol = {"Serial no": "2","Type":"Guarana","Amount": "750ml"}
print(alcohol["Serial no"])
print(alcohol["Type"])
print(alcohol["Amount"])

#adding a value
alcohol["place"] = "roasters"
alcohol["person"] = "kabiru"
print(alcohol)

#delete that bitch
del alcohol["person"]
print(alcohol)

print("number\tsquare")
print("==============")
for number in range (0,1000):
    print(number,"\t",number**2)
