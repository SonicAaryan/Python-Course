# Dictionary is a collection of keys-value pairs and it is mutable.
'''
Properties of Dictionaries
1) It is unordered
2) It is mutable
3) It is indexed
4) Cannot contain duplicate keys
'''

marks = {
    "Amit" : 78,
    "Rohan" : 69,
    "riya" : 81
}
print(marks["riya"]) # Here if the key is not present then it gives <Error>

print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.update({"riya":89}))
print(marks.get("riya")) # here if the key is not present then it give <None>


'''
Methods : marks.items() : Return a list of (key,value)tuples.
        : marks.keys()  : Return a list containing dictionary's keys. 
        : marks.update({"riya":89}) : Updates the dictionary with supplied key-value pairs.
        : marks.get("Amit") : Returns the value of the specified keys (and value is returned e.g "89" is returned here).

    explore more....
'''