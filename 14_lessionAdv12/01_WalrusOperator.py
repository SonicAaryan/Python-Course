'''
---- When to Use It ----
Use the walrus operator when:

You want to avoid repeating a function call.

You're doing a check and need the result later in the same expression.

You want to shorten your code, especially inside conditions and comprehensions.
'''

# Without the walrus operator:
value1 = input("Enter something :")
if value1 != "":
    print(f"Without the walrus operator -> You entered: {value1}\n")

# With the walrus operator:
if(value2 :=input("Enter something: ")) != "":
    print(f"With the walrus operator -> You entered: {value2}\n")
    

# Example with List Comprehension
result = []
for word in ['apple','banana','pear']:
    length = len(word)
    print(length>4)
    if(length>4):
        result.append((word,length))

print(result)

# With walrus 
results = [(word, length) for word in ['apple', 'banana', 'pear'] if (length := len(word)) > 4]
print("using walrus :",results)