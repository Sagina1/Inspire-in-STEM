# paragraphs
Billionaire = {"Name":"Bill","ID no":"294715","Residence":"Richville"}
print(Billionaire["Name"])
print(Billionaire["ID no"])
print(Billionaire["Residence"])

#adding to a paragraph
Billionaire["Heirs"] = ("2")
Billionaire["Cars"] = ("20")
print(Billionaire)
 
# replacing sth in a paragraph
Billionaire["Name"] = ("Sagina")
Billionaire["Residence"] = ("Not constant")
print(Billionaire)

# deleting sth in a paragraph
del Billionaire["Heirs"]
print(Billionaire)

# squares
print("number\tsquare")
print("==============")
for number in range(0,2700):
    print(number**2,number)

#squareroots
print("number\tsquareroot")
print("==================")
for number in range(0,2700):
    print(number, number//2)


