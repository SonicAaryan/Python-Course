# Create a class with class attribute a: create an object from it and set 'a' directly using object.a = o ,Does this change the class attribute?  

class CarShowroom:
    def __init__(self):
        self.car1 = "Rolls-Royce Cullinan"
        self.car2 = "Range Rover"
        self.car3 = "Bentley Continental GT"
        self.car4 = "Mercedes-Benz S-Class"
        self.car5 = "Porsche Cayenne"
    
    def getCars(self):
        print("The available cars are:")
        try:
            print(f"{self.car1}, {self.car2}, {self.car3}, {self.car4}, {self.car5}")
        except AttributeError as e:
            print("Error:", e)

# Create object
cars = CarShowroom()

# Modify car1
cars.car1 = "Ferrari"
cars.getCars()  # Shows "Ferrari" as car1

# Delete car1
del cars.car1
cars.getCars()  # Raises AttributeError because car1 no longer exists

'''
. When you use obj.a = value:
You’re creating or overriding an instance attribute (obj.a)

If you then do del obj.a, Python deletes the instance-level version

BUT: If the class also has a class attribute a, then obj.a will fall back to the class attribute

✅ That’s why it doesn't raise an error — it finds a on the class.
'''

# Case 1: Class Attribute Fallback
class MyClass:
    a = "Class value"

obj = MyClass()
obj.a = "Instance value"
print(obj.a)  # Output: Instance value

del obj.a
print(obj.a)  # ✅ Output: Class value (fallback!)


# Case 2: No Fallback (Only Instance Attribute)
class MyOtherClass:
    def __init__(self):
        self.b = "Only instance value"

obj2 = MyOtherClass()
print(obj2.b)  # Output: Only instance value

del obj2.b
print(obj2.b)  # ❌ AttributeError — no class-level b