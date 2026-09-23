# password generator project

import random
# create lists to store the combiations the password can be made from 
# all caps and small case letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# numbers from 0-9
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# all symbols 
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~']

print("HELLO! Welcome to your favourite  password generator\n")
# prompt the user for the number of letters, numbers and symbols they would like their password to have 
num_letters = int(input("Enter the number of letters you would like your password to have\n"))
num_numbers = int(input("How many numbers would like your password to have\n"))
num_symbols = int(input("Enter the number of symbols you would like your password to have\n"))

#contains the functionality of creating an empty list and then randomly picking the items from the list based by the number input from the user
# then appending the random items to the empty password list
password = []
['f','g','M','2','4','1','#','@']
for letter in range(0,num_letters):
    random_letter =random.choice(letters)
    password.append(random_letter)

for num in range(0, num_numbers):
    random_num = random.choice(numbers)
    password.append(random_num)

for sym in range(0, num_symbols): 
    random_symbol = random.choice(symbols)
    password.append(random_symbol)

# Now we have a list of our password but it is ordered so what we need to do is shuffle it using the shuffle function
random.shuffle(password)
#we now want to join the password and print it out as a string 
joined_password = "".join(password)

print("Here is your hard to hack password!")
print(joined_password)
