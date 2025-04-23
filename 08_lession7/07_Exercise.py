# Q. Perform star pattern 
'''
*
* *
* * *
'''
row = int(input("Enter the length for star pattern"))
for i in range(1,row+1):
    
    for j in range(i):
        print("*",end=" ")
    
    print("\n")