'''
The 'enumerate' function adds counter to an iterable and return it
'''
# Without Enumerate
print("\nWithout Enumerate")
index = 0
list1 = [1,23,5,45,76]
for item in list1:
    print(f"The item number {index} is {item}") # Prints the items of list 1 with index
    index += 1

print("\nWith Enumerate")
# With Enumerate
for index , item in enumerate(list1):
    print(f"The item number {index} is {item}") # Prints the items of list 1 with index