# Q. If the names of 2 friends are same ; what will happen to the program in problem 6 ? => Print's the latest value

friendList = {}


length = int(input("Enter length of list :"))

for _ in range(length):
    name = input("Enter friends name :")
    lang = input("Enter language name :")
    friendList.update({name:lang})
    

print(friendList)