# Q. Perform star pattern 
'''
    *
   * *
  * * *
'''
row = int(input("Enter the input for star pattern :"))
for i in range(1,row+1):
    print(" " * (row - i), end="")
    
    for j in range(i):
        print("* ",end="")
        
    print("\n")