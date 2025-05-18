# SELF refers to the instance of the class .It is automatically possed with a function call from an object 
class Employee:
      name = "Ferry"
      language = "Python" 
      salary = 1099000
      
      def getInfo(self):
         print(f"The Employee work on {self.language} language.")

      @staticmethod # Sometimes we need a function that does not use the self-parameter. We can define a static method like this: If you dont want anything from Object Property then use @staticmethod
      def greet():
         print("Good Morning sir")

      def greet2():
         print("Good Morning sir")
   
objEmp = Employee()

print("Employee Name :",objEmp.name,"\nSalary :",objEmp.salary)
objEmp.getInfo()

objEmp.greet()
'''
If u dont give 'self' parameter then the above line is converted into Employee.getInfo(objEmp) <- here it accept parameter so we write SELF
'''

objEmp.greet2()