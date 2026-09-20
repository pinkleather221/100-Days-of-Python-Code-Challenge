# Hang man game
# import the random module 
import random
word_list = ["serendipity", "ephemeral", "luminescence", "solitude", "resilience", "eloquence", "melancholy", "aurora", "petrichor", "alcyon"] 
random_word = random.choice(word_list)
print (random_word)

# printing out underscore in place of the word the computer randomly chose 
placeholder = ""
for l in random_word:
    placeholder += "_"
print(placeholder)

# replacing the underscore with the correct guessed letter 
guess = input("Guess a letter ").lower()
display = ""
for letter in random_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)      

