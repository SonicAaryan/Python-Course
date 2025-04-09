# Q. Enter the list of fruit from users side.

fruits = []

data = int(input("Enter length for fruit bucket: "))

# Loop for the number of fruits
for _ in range(data): 
    fruit = input("Enter fruit name: ")
    fruits.append(fruit)

print("Fruits in the bucket:", fruits)
