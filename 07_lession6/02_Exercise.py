# Q. Write a program to find out whether a student has passwed or failed if it requires a total of 40% and at least 30% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

sub1 = int(input("Enter chemistry marks :"))  
sub2 = int(input("Enter math marks :"))  
sub3 = int(input("Enter physics marks :")) 

total_percentage = (100*(sub1+sub2+sub3))/300
if(total_percentage>=40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print("You are pass")
else:
    print(f"You have failed {total_percentage},try again next sem! ")