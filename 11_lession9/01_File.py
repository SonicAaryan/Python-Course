# The random-access memory is volatile and all its contents are lost once a program terminates in order to persist the data forever , we use files.

# A File is data stored in storage device. A python program can talk to the file by reading content from it and writing content to it

file = open('file.txt','r') #open() help to open file and accept two parameter (ByDefault is r)
data = file.read()
print(data)
file.close()