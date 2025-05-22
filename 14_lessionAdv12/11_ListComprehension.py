# List Comprehension is an elegant way to create lists based on existing lists.

myList = [123,435,324,32,231]
squardList = []
for item in myList:
    squardList.append(item*item)
    
print("Without using List Comprehension :",squardList)

# Using List Comprehension
myList = [i for i in myList]
print(f"Using List Comprehension :{myList}")