# We are going to write a program that generates a random number and asks the user to guess it.
# If the player's guess is higher than the actual number,the program displays "Lower number please". Similarly ,if the user's guess is too low,the program prints "higher number please"
# When the user guesses the correct number ,the program displays the number of guesses the player used to arrive at the number.
  
import random
computerGuess = random.randint(1,100)
# print(computerGuess)
guesses = 0
userGuess = int(input("Guess the number :"))
userGuess = -1

while(userGuess!=computerGuess):
   
    userGuess = int(input("Guess the number again!:"))
    if(userGuess > computerGuess):
        guesses += 1
        print("Guess lower number")
    elif(userGuess<computerGuess):
        guesses += 1
        print("Guess a higher number")
    elif(userGuess == computerGuess):
        print(f"You have guessed the correct number in {guesses} guess")
    
