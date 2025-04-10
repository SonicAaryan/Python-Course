# Q. Create an empty dictionary . Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

friendList = {}


length = int(input("Enter length of list :"))

for _ in range(length):
    name = input("Enter friends name :")
    lang = input("Enter language name :")
    friendList.update({name:lang})
    

print(friendList)