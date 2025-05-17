# Q. Write a python function to remove a given word form a list & strip it at the same time.

def remove(list,word):
    n = []
    for item in list:
        if not(item == word):
            n.append(item.strip(word))
    return n
            
list = ["anHarry","Rohan","Joy","ryan"] 
print(remove(list,"an"))

# strip(word) removes an from <front and the end> of the word