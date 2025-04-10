# Q. Can you change the values inside a list which is contained in set S?
# Set has no indexing...
'''
But in Python, sets can only contain immutable (hashable) objects. Lists are mutable (i.e., their contents can be changed), so they are unhashable, and therefore cannot be added to a set.
'''
s = {8 , 7 , 12 , "AAA" , [1 , 2]}  
print(s)

