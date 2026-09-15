# password generator project

# create lists to store the combiations the password can be made from 
# all caps and small case letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# numbers from 0-9
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# all symbols 
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~']

print("HELLO! Welcome to your favourite  password generator\n")
# prompt the user for the number of letters, numbers and symbols they would like their password to have 
num_letters = int(input("Enter the number of letters you would like your password to have"))
num_numbers = int(input("How many numbers would like your password to have"))
num_symbols = int(input("Enter the number of symbols you would like your password to have"))

password = ""
for letter in letters:
    pass