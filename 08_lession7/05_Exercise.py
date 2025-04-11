# Q. Write a program to calculate the factorial of given number using for loop

num = int(input("Enter the number to calculate factorial :"))
sum=1
for i in range(1,num+1):
    sum *= i 
    
print(f"The sum of factorial of {num} is {sum}")
