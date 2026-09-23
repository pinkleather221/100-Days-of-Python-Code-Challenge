# Hang man game
# import the random module 
import random
from hangman_art import hangman_stages, hangman_banner
from hangman_words import word_list
print(hangman_banner)
lives = 6
random_word = random.choice(word_list)
# print (random_word)

# printing out underscore in place of the word the computer randomly chose 
placeholder = ""
for l in random_word:
    placeholder += "_"
print(placeholder)

# creating an empty list to store the correctly guessed letters 
c_guessed = []


game_over = False

while not game_over: 
# replacing the underscore with the correct guessed letter 
    guess = input("Guess a letter ").lower()

    if guess in c_guessed:
       print(f"Already guessed {guess} guess a different letter ")
       
    display = ""
    for letter in random_word:
        if letter == guess:
            display += letter
            c_guessed.append(guess)
        elif letter in c_guessed:
            display+= letter
        else:
            display += "_"

        if lives == 0:
            print()
    
    print(display)    

    # checking to see if the underscore is no longer in the word then printing out "you win " and game_over resets to true 
    if "_" not in display:
        game_over = True
        print("You got it right, You win!")
        


    if guess not in c_guessed:
        lives -= 1
        print(f"You guessed letter {guess} its not in the word")
        print(f"You have lost one life,  {lives} remaining!")
       
                
        if lives == 0:
            game_over = True
            print("You Loose")
            print(f"The correct word was {random_word}")

            

    print(hangman_stages[lives])

