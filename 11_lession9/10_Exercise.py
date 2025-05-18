# Write a program to rename a file to "renamed_by_python.txt".
# We can use os moudle to delete previous file.

with open('rename_me.txt')as f:
   content= f.read()
   
with open('renamed_by_python.txt','w')as f:
   f.write(content+"\ncreated with new file name")