# Map applies a function to all the items in an input_list
'''
syntax : map(function, input_list)
# the function can ne lambda function
'''
l = [1,2,3,5,6]
square = lambda x :x*x
sqlist = map(square,l)
print(list(sqlist)) # output converted into list


# Filter creates a list of items for which the function returns true.
'''
syntax : list(filter(function))
# The function can be lambda function
'''
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even,l)
print("Evens :",list(onlyEven))

# Reduce Applies a rolling computation to sequential pair of elements.
'''
syntax : from functools import reduce
         val = reduce (function, list1)
         # The function can be lambda function
'''

from functools import reduce

def sum(a,b):
    return a+b

print("Sum :",reduce(sum,l))