# Q. Write a program to greet all the person names stored in a list 'l' and which starts with S.

list =["Ryan","Brown","Sky","Shifu","Panda"]

for i in range(len(list)):
    if(list[i].startswith("S")):
        print(f"Good morning '{list[i]}'")
    else:
        print(f"Hello Guys '{list[i]}'")