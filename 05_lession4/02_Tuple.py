# A Tuple is an immutable data type in python.

tuple = (1,2,3,4)
a,b,c,d = tuple # Unpacking
print(a,b,c,d)
print(4 in tuple) # return boolean value
# tuple[0] = 100 # Error : cannot change value
print("Tuple :",tuple)
print("length of tuple :",len(tuple))

empty = ()
print(type(empty))

data=(1) # here tuple is not created so to do that we add <,> after value
print(type(data))

number=(1,)
print(type(number))

# Method
'''
    tuple.index(1) -> return value at index 1
    tuple.count(1) -> return number of times the 1 has in the tuple.
    explore more method.
''' 