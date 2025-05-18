str = "You are amazing!!"
file = open('WriteFile.txt','w')

file.write(str)
file.close()

'''
Modes of Opening a File
r -> open for reading.
w -> open for writing.
a -> open for appending.
+ -> open for updating.
rb -> will open for read in binary mode.
rt -> will open for read in text mode.
'''