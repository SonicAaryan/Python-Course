# Q. Write a program to input eight numbers from the user and display all the uniqye numbers(once).

s = set()

length = int(input("Enter length of the number to add input :"))

for _ in range(length):
    num= input("Enter your number :")
    s.add(num)
    
print("All unique numbers :",s)