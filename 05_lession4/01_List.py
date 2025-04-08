
list =["Orange", 5 , 1 , 7 , 98.9 , None , bool] # Lists are mutable , a list can be indexed just like a string.
print("Before :",list)

list.append("Mangos") # add in the end of the list.

print("After :",list)
print(list[2:])
# print(list[5]) Error : IndexError: list index out of range

# List Method 
'''
1) list.sort() : updates the list to [1,2,7,8,12,21]
2) list.reverse() : updates the list to [12,5,6,8,9]
3) list.append("Mangos") # add in the end of the list.
4) list.insert(3,8) : This will add 8 at index 3.
5) list.pop(2) : Will delete element at index 2 and return its value.
6) list.remove(None) : Will remove 21 from the list.
'''