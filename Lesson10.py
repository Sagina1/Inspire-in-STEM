#!usr/bin/python
#dictionaries
#CrunchyBiscuit
#25th May 2022
##################

#key value pair are written inside curly brackets and enclosed in quotations and separated by a full colon
color = {'color': 'red'}
vehicle = {'type':'toyota','plate number':'kyz'}
print(type(color))# this is to find out the data type
#key value pair for a person
person = {'name':'Susan',
'age':'19',
'ID no':'27300512',
'location':'Kisumu',
'number':'0709374654'}
print(vehicle['type'],vehicle['plate number'])
print(type(person))
print(person)
#deleting key value pair
del(person['number'])
print(type(person))
print(person)


