# Q. Write a program to accept marks of 6 student and display them in sorted manner .

studentMarks = []

marksLength = int(input("Enter length for student: "))

for _ in range(marksLength):
    marks= int(input("Enter studen mark :"))
    studentMarks.append(marks)
    studentMarks.sort()
    
print("ALl student marks :",studentMarks)