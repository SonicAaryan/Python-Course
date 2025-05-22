# Type hints are added using the colon(:) syntax for variables and the -> syntax for function return types.

# Variable type hint
age: int = 25

# Function type hints
def greet(name:str)-> str:
    return f"Hello ,{name}!"

# Usage
print(greet("Aryan"))
 
n : int = 5
name : str = "ABC"

def sum(a:int,b:int)-> int:
    return a+b

print("Addition of two variable is :",sum(50,76))