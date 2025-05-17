# Snake-Water-Gun game
# 1 = Snake, -1 = Water, 0 = Gun

import random
computer = random.choice([1, -1, 0])

# Mapping for user input and reverse lookup
userVariable = {"s": 1, "w": -1, "g": 0}
computerVariable = {1: "Snake", -1: "Water", 0: "Gun"}

userInput = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Validate input
if userInput not in userVariable:
    print("Invalid input! Please enter s, w, or g.")
else:
    yourSide = userVariable[userInput]
    print(f"You chose {computerVariable[yourSide]}\nComputer chose {computerVariable[computer]}")

    if computer == yourSide:
        print("It's a draw!")
    elif (yourSide == 1 and computer == -1) or (yourSide == -1 and computer == 0) or (yourSide == 0 and computer == 1):
        print("You Win!")
    else:
        print("You Lose!")
