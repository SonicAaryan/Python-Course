# Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce

numbers = [231,2131,343,9945,4531,354235,5]

def findMax(a,b):
    if(a>b):
        return a
    return b

print(reduce(findMax,numbers))