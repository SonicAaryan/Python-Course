# Q. Write a program to find whether a given number is prime or not.

checkPrime = int(input("Enter the number to check prime :"))

if(checkPrime%2==0):
    print(f"{checkPrime} is a Prime Number")
else:
    print("Is not a Prime Number")