# Other Method to Read file -> We can also use file.readline() function to read one full line at a time.
file=open('file.txt')

line1 = file.readline()
print(line1,type(line1))

line2 = file.readline()
print(line2,type(line2))

line3 = file.readline()
print(line3 == '')

file.close()