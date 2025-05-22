'''
If you run this file then it will be -> main , and when u import in another file it will show <file name>
'''

def myFunc():
    print("Hey , Surprise!!")



if __name__ == "__main__":
    # If this code is executed by running the file its present in 
    print("We are directly this code")
else:
    myFunc()
    print(__name__)
    
'''
'__name__' evaluates to the name of the module in python from where the program is ran.
If the module is being run direclty from the command line , the '__name__' is set to string "__main__".Thus,this behaviour is used to check whether the module is run direclty or imported to another file. 
'''