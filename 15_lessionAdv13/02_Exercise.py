# Write a program to input name , marks and phone number of a student and format it using the format function like below. "The name of the student is Harry, his marks are 72 and phone number is 99999888"

name = input("Enter your name :")
marks = int(input("Enter your Percentage :"))
phoneNum = int(input("Enter your Phone Number :"))

sentence = "The name of the student is {0}, his Percentage are {1} and phone number is {2}".format(name,marks,phoneNum)
print(sentence)