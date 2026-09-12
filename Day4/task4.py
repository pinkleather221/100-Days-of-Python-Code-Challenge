import random as r #importing the module called random ,, and giving it an alias name r
heads_or_tails = r.randint(0,1) #creating a variable to store the random integers being generated ,,, that is 1 or 2

#an if else statement to print heads or tails according to the random number generated 
if heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

#list is a way of storing ordered data ,,,(its a data structure)
names = ["nelly", "mogere", "gesare", "nelly"]
poped = names.pop() #removes the last item and returns the item removed
print(poped)
names.remove("nelly") # removes the first occurence of the item specified in the paranthesis 
print(names)
names.extend(["alan", "wayne"]) # this adds the names to the existing list
print(names)


# looping through a list to output a random item
names = ["nelly", "mogere", "gesare", "nelly"]
random_name = r.choice(names) #used the r alias i had assigned my random module earlier
print(random_name)

# alternative 
random_i =r.randint(0,len(names)-1)
print(names[random_i])



