# Add a static method in problem 2, to greet the user with hello
'''
You used the @staticmethod decorator → ✅ Correct.

You didn't use self inside greet() → ✅ Correct for a static method.

You printed a greeting → ✅ Matches: "Hello User , A Very Good Morning to you!!"

You called the method using the object msg → ✅ Works fine.
'''

class Message:
    
    @staticmethod
    def greet():
        print("Hello User , A Very Good Morning to you!!")

msg = Message()
msg.greet()
# You can also call static methods using the class name directly (no object needed):
Message.greet()