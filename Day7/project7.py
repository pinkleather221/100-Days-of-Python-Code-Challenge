# Hang man game
# import the random module 
import random
word_list = ["serendipity", "ephemeral", "luminescence", "solitude", "resilience", "eloquence", "melancholy", "aurora", "petrichor", "alcyon"] 
random_word = random.choice(word_list)
print (random_word)

placeholder = ""
for l in random_word:
    placeholder += "_"
print(placeholder)

display = list(placeholder)

guess = input("Guess a letter ").lower()

for g, letter in enumerate(random_word):
    if letter == guess:
        display[g] = guess
        final_display = "".join(display)
print(final_display)        

