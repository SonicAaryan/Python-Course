file = open('file.txt')
print(file.read())
file.close()

# The Same can be written using with statement like this
with open("file.txt") as f:
   print(file.read())

# You Dont have to explicitly close the file