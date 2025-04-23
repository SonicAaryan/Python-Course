# Q. Perform star pattern 
'''
 * * *
 *   *
 * * *
'''
row = int(input("Enter the input for star pattern :"))
for i in range(1,row+1):
    for j in range(1,row+1):
        if(i%2==0):
            if(j==1 or j==row):
                print("*",end=" ")
            else:
                print(end="  ")
        else:        
            print("*",end=" ")
    
    print("\n")