# Exception Handling
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter valid numbers!")
else:
    print("When try block executes then else block executes")
finally:
    print("Hey i am inside of finally")
