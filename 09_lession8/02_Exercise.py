# Q. Write a recursive function to calculate the sum of first n natural numbers.
def sumOfNum(num):
    if(num==1):
        return 1
    return sumOfNum(num-1)+num

print("Sum of Natural No are :",sumOfNum(5))