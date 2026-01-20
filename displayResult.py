#3. Write a program to enter marks of 4 subjects and display result (result shall include total, percentage and grade) 


sub1 = float(input("enter social science marks : "))
sub2 = float(input("enter english marks : "))
sub3 = float(input("enter maths marks : "))
sub4 = float(input("enter science marks: "))

totalMarks = sub1+sub2+sub3+sub4

percentage = totalMarks/4

print("your total marks is ", totalMarks)
print("your percentage is ",percentage)

if percentage >= 90:
    print("excellent")
elif percentage >=80:
    print("very good")
elif percentage >= 70:
    print("good")
elif percentage >=60:
    print("average")
elif percentage >= 50:
    print(" poor ")
elif percentage >=40:
    print(" fail ")

