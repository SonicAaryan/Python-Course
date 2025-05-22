# Write a program to open three files 1.txt , 2.txt , 3.txt if any these are not present , a message without exiting the program must beprinted prompting the same.
try:

    with open('1.txt','r')as f:
        print(f.read())
except Exception as e:
    print(e)

try:

    with open('2.txt','r')as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open('3.txt','r')as f:
        print(f.read())
except Exception as e:
    print(e)
