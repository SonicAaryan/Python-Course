'''
__init__() is a special method which is first run as soon as the object is created
__init__() method is also known as constructor.

It takes self-argument and can also take further arguments.
'''
class Employee:
      name = "Ferry"
      language = "Python" 
      salary = 1099000
      
      # In py __***__ methods are known as Dunder Method , Which is automatically called when < OBJECT IS CREATED >
      def __init__(self) -> None:
           print("I am creating an object")
      
      def getInfo(self):
         print(f"The Employee work on {self.language} language.")

objEmp = Employee()
# objEmp.name="Aaryan"
# print("Employee Name :",objEmp.name,"\nSalary :",objEmp.salary)
# objEmp.getInfo()