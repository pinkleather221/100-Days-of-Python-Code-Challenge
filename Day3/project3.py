print("welcome to Treasure Island. Your mission is to find the treasure")

# Prompt the user to input a direction either left or right
direction = input("Which direction do you want to go:(left / right)").lower().strip()
if direction == "right":
        print("Game Over")
# the rest of the choices fall under this nested if else loop
else:
        activity= input("what activity would you like to do: (swim / wait) ").lower().strip()
        if activity == "swim":
                print("Game Over!")
        elif activity == "wait":
                door = input("Which door would you like to open: (blue / red/ yellow)").strip().lower()
                if door in ("blue", "red"):
                        print("Game Over")
                elif door == "yellow":
                        print("You Win")


                        
 