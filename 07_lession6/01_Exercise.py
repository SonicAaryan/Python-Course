# Q. Write a program to find the greatest of four numbers.

num1 = int(input("Enter the 1st Number"))
num2 = int(input("Enter the 2nd Number"))
num3 = int(input("Enter the 3rd Number"))
num4 = int(input("Enter the 4th Number"))

if num1 >= num2 and num1 >= num3 and num1 >= num4:
    print(f"Number {num1} is the greatest.")
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    print(f"Number {num2} is the greatest.")
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    print(f"Number {num3} is the greatest.")
else:
    print(f"Number {num4} is the greatest.")