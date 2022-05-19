motorcycle = ['honda','yamaha','suzuki']
print(motorcycle)
#accessing list items using index
#print(motorcycle)
print(motorcycle[1])
motorcycle[0]='bugatti'# replacing an item in a list
print ("i love " +str(motorcycle[2]))
# adding elements in a list
motorcycle.append('bugatti yohana')
print(motorcycle)
# puting each motorcycle and plate number
plate_number = ["KCD,KBP,KDD"]
motorcycle_owner = ('mojo jojo')
print("KCD" +str(motorcycle[0]))
print("KBP"+str (motorcycle[1]))
print("KDD" +str (motorcycle[2]))
#deleting an itm from a list---del
del motorcycle[3]
print (motorcycle)
# deleting item from a list use --del 
# to delete last item from a list use popped ie popped_motorcycle = motorcycle.pop
popped_motorcycle = motorcycle.pop()
print(motorcycle)
print(popped_motorcycle)
#task
print("My name is {} and i own a motorcycle plate number {} ".format(motorcycle_owner,plate_number[0]) )
print(f"my name is {motorcycle_owner}and i won a motorcycle{plate_number[0]}") 
#task remove statement---removing an item from a list
motorcycle.remove('suzuki')
print(motorcycle)
motorcycle.remove('bugatti')
print(motorcycle)