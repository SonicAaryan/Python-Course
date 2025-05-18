# The game() function in a program lets a user play a game and returns the score as an integer.You need to read a file 'Hi-Score.txt which is either blank or contains the previouse Hi-score .You need to write a program to update the Hi-Score whenever the game() function breaks the Hi-Score. 

import random

def game(): 
   print("You are playing the game.")
   score = random.randint(1,65)
   # Fetch the hiscore
   with open('Hi_score.txt') as f:
      hiscore = f.read()
      if(hiscore != ""):
         hiscore = int(hiscore)
      else:
         hiscore = 0
         
   print(f"Your score {score}")
   if(score > hiscore):
      with open('Hi_score.txt','w') as f:
         f.write(str(score)) # write() accept string so u have to pass value in file as String
 
   return score

game()