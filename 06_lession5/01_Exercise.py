# Q. Write a program to create a dictionary of Hindi words with values as their english translation. Provide user with an option to look it up!.

meanings= {
    'kursi': 'Chair',
    'kutta': 'Dog',
    'undir': 'Mouse',
    'pani' : 'Water',
    'chaya': 'Shadow',
}

word = input("Enter the word in hindi to know the meaning in english :")

if word in meanings:
    print(f"The Meaning of '{word}' is : {meanings[word]}")
else:
    print(f"Apologize , the Meaning of '{word}' is not found ")