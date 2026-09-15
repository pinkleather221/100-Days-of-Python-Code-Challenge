#Generating a rock, paper, scissors game
import random
print("--" * 25)
print("Welcome to the: -->  |ROCK --> PAPER --> SCISSORS| GAME") 
print("Logic of the game , rock - paper(win), paper - scissors(loose), scissors - rock(loose)")
print("--" * 25)

user_choice = input("What do you choose: input=>   0: for (rock), 1: for (paper), 2: for (scissors)")
computer_choice = random.randint(0,2)

if user_choice.isdigit() and int(user_choice) < 3:  

    user_choice = int(user_choice)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("Its a draw, no winner yet")
    elif (user_choice == 0 and computer_choice == 2 or
        user_choice == 1 and computer_choice == 0 or
        user_choice == 2 and computer_choice == 1):
        print("You Win!")
    else:
        print("    You Loose! ")
else:
    print("Invalid Input: choose  between (0, 1, 2)")




