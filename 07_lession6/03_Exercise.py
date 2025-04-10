# Q. A Spam comment is defined as a text containing following keywords: "Make a lot of money" , "Buy now" , "subscribe this" , "click this". Write a program to detect these spams.

p1 = "make a lot of money"  
p2 = "click this"
p3 =  "buy now"
p4 =  "subscribe this" 

message = input("Enter your comment :")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")
else:
    print("This comment is not a spam")