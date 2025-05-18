class Employee:
      name = "ZBC"
      salary = 6000
      
      # In py __***__ methods are known as Dunder Method , Which is automatically called when < OBJECT IS CREATED >
      def __init__(self,name,language,salary) -> None:
         self.name=name # Here when this Function will get call it will replace the value of class property.
         self.language=language
         self.salary=salary
         print("CALLS WHEN OBJECT IS CREATED -> I am creating an object")
      
      def getInfo(self):
         print(f"The Employee work on {self.language} language.")

objEmp = Employee("Ferry","Python",1099000)

print("Employee Name :",objEmp.name,"\nSalary :",objEmp.salary)
objEmp.getInfo()