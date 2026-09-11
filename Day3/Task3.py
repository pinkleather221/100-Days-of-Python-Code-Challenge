# If else statement 
print("Welcome to the voting station")
age = int(input("Enter your age: "))

# if statement to check if the user has the required age of 18 and above to vote 
if age > 18:
    print("You can vote")
else:
     print("Sorry you are not eligible to vote ")

#the modulo operator %,,,, divides a number and returns a remainder 
# alll even numbers do not have a remainder when divided by 2
number= int(input("What is the number you want to input"))
if number % 2 == 0:
     print("Its an even number")
else:
    print("This is an odd number")

# nested if else statement ,,, this is an if ststement inside another if statement
age = 24
if age > 18:
    print("you are almost there")
    citizen = input("enter your citizenship: ")
    if citizen == "kenyan":
         print("You can vote")
    else:
         print("You must be a kenyan citizen")
else:
     print("Sorry you are not eligible to vote ")



     