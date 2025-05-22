# Store the multiplication tables generated in a file named Tables.txt

num = int(input("Enter no.for multiplication of table :"))
table = [num*i for i in range(1,11)]
print(table)
with open('Tables.txt','a')as f:
    f.write(f"Table of {num} : {str(table)} \n")
