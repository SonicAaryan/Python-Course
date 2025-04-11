# Q. Write a program to find the sum of first n natural numbers using while loop

num = int(input("Enter the length to calculate sum of natural number :"))
sum=0
for i in range(1,num+1):
    sum +=i

print(f"The sum of n natural number are {sum}")