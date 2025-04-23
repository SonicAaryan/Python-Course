# Q. Write a program to print multiplication table of n using for loops in reversed order.

num = int(input("Enter the input for star pattern :"))
for i in range(1,11):
    print(f"{num} x {11-i} = {num*(11-i)}") 
