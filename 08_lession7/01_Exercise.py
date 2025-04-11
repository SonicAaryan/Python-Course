# Q. Write a pg to print multiplication table of given number using for loop.

number = int(input("Enter the Number :"))

for i in range(1,11):
    print(f"{number} x {i} = {number*i}")