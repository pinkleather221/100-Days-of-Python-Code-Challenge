# functions and while loops(used when you want to loop through
#  a program when the condition is true , 
# only making an exi when its false this can be dangerous as the loop will run infinitely if the condition will never be false)
while 5 > 2:
    print("I will run forever")

#because 5 will forever be greater than 2 we will get an output of 
# I will run forever
# I will run forever
# I will run forever
# I will run forever
# I will run forever
# I will run forever
# I will run forever
# I will run forever

# functions are used to avoid repetition and also make the code more readable 

def print_name(): #defining the function
    print("My name is nelly ")

print_name() #calling the function