# Write a program to find out whether a file is identical & matches the content of another file.

with open('info.txt','r')as f:
   content_file1 = f.read()
   
with open('info_copy.txt','r')as f:
   content_file2 = f.read()

if(content_file1==content_file2):
   print("Both File have same content")
else:
   print("Both File have doesn't same content")