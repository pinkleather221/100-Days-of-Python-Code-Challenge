import random as r #importing the module called random ,, and giving it an alias name r
heads_or_tails = r.randint(0,1) #creating a variable to store the random integers being generated ,,, that is 1 or 2

#an if else statement to print heads or tails according to the random number generated 
if heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
