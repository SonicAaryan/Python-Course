# Write a program to filter a list of numbers which are divisible by 5
def divisible(num):
    if(num % 5 == 0):
        return True
    else:
        return False

numbers = [231,2131,343,9945,4531,354235,5]

filterForNum = list(filter(divisible,numbers))
print(f"divisible by 5 are :{filterForNum}")
