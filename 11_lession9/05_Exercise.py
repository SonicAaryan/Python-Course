# Repeat program 4 for a list of such words to be censored.

words = ["shit","ass","holy"]

with open('word.txt','r')as f:
   content  = f.read()

for word in words:
   content = content.replace(word,"#"*len(word))

with open('word.txt','w')as f:
   f.write(content)