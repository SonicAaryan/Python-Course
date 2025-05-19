# Write a class "Programmer" for storing info of few programmers working at microsoft

class Programmer:
    company = "Microsoft"
    
    def __init__(self,name):
        self.name=name
        
    def getInfo(self):
        print(f"{self.name} works at {self.company}")

p1 = Programmer( "Jue")
p2 = Programmer( "Sailesh")
p3 = Programmer( "Spider")
p4 = Programmer( "Spizz") 

p1.getInfo()
p2.getInfo()
p3.getInfo()
p4.getInfo()