'''
An Object is an instantiation of a class.when class is defined, a template(info) is defined. Memory is allocated only after object instantiation.

Objects of a given class can be invoke the methods available to it without revealing the implementatuon detailed to the user - Abstractions & Encapsulation.
'''
# instance-vs-classAttribute -> Instance attributes take preference over class attributes during assignment & retrieval
class Employe:
      name = "Ferry"
      language = "Python" # This is a class attributes.
      salary = 1099000
   
objEmp = Employe()
print("Object Address :",objEmp)
objEmp.name="Joy" # This is an instance attribute
print("Employee Name :",objEmp.name,"\nSalary :",objEmp.salary)

# Class Attributes - An Attribute that belongs to the class rather than a particular object.