# Hang man game
# import the random module 
import random
hangman_stages = [
    # Stage 6: Both legs added (Game Over)
    """
       --------

       |      |
       |      O

       |     /|\\
       |      |
       |     / \\
    --------
    """,
    # Stage 5: One leg added
    """
       --------

       |      |
       |      O

       |     /|\\
       |      |
       |     / 
    --------
    """,
    # Stage 4: Both arms added
    """
       --------

       |      |
       |      O

       |     /|\\
       |      |
       |     
    --------
    """,
    # Stage 3: One arm added
    """
       --------

       |      |
       |      O

       |     /|
       |      |
       |     
    --------
    """,
    # Stage 2: Torso added
    """
       --------

       |      |
       |      O

       |      |
       |      |
       |     
    --------
    """,
    # Stage 1: Head added
    """
       --------

       |      |
       |      O
       |     
       |      
       |     
    --------
    """,
    # Stage 0: Base and gallows only
    """
       --------

       |      |
       |      
       |     
       |      
       |     
    --------
    """
]
lives = 6
word_list = ["serendipity", "ephemeral", "luminescence", "solitude", "resilience", "eloquence", "melancholy", "aurora", "petrichor", "alcyon"] 
random_word = random.choice(word_list)
print (random_word)

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

    if guess not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Loose")

    print(hangman_stages[lives])

