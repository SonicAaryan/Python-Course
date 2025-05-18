# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.
file = open('file.txt')
content = file.read()
if ('twinkle' in content):
   print('Twinkle word is present in the file')
else:
   print("The word is not present in the file!")

file.close()