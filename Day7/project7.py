# Hang man game
# import the random module 
import random
word_list = ["serendipity", "ephemeral", "luminescence", "solitude", "resilience", "eloquence", "melancholy", "aurora", "petrichor", "alcyon"] 
random_word = random.choice(word_list)
print (random_word)
guess = input("Guess a letter ").lower()
for g in random_word:
    if g == guess:
        print("Right") 
    else:
        print("Wrong")
