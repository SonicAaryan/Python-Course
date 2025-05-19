# Write a class "calculator" capable of finding square,cube and square a root of a number.

class Calculator:
    def __init__(self,num):
        self.num = num
    
    def findSquare(self):
        print(f"The Square root of {self.num} is {self.num*self.num}")
    
    def findCube(self):
        print(f"The Cube root of {self.num} is {self.num*self.num*self.num}")
    
    def findSquareRoot(self):
        print(f"The Square root of {self.num} is {self.num**0.5}")
    
findSquare = Calculator(10)
findSquare.findSquare()

findCube = Calculator(5)
findCube.findCube()

findSquareRoot = Calculator(10)
findSquareRoot.findSquareRoot()
