import random
print('Welcome to our password generator')
character = 'Shonarwa@345'
no_of_password = input('How many passwords do you want?')
no_of_password = int(no_of_password)
len_of_password = int(input('length of password'))
# print(character)
for password in range (no_of_password):
    password = ''
    for c in range(len_of_password):
     password += random.choice(character)
    print(password)