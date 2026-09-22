# Made by Reshma - PGDCA - Student Marksheet System

print("===== STUDENT MARKSHEET =====")
name = input("Enter Student Name: ")

# Take 5 subject marks
sub1 = float(input("Enter marks for Subject 1 (out of 100): "))
sub2 = float(input("Enter marks for Subject 2 (out of 100): "))
sub3 = float(input("Enter marks for Subject 3 (out of 100): "))
sub4 = float(input("Enter marks for Subject 4 (out of 100): "))
sub5 = float(input("Enter marks for Subject 5 (out of 100): "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

# Find Grade
if percentage >= 90:
    grade = "A+ - Outstanding!"
elif percentage >= 75:
    grade = "A - Excellent"
elif percentage >= 60:
    grade = "B - Very Good"
elif percentage >= 45:
    grade = "C - Good"
else:
    grade = "D - Need Improvement"

print("\n------ RESULT ------")
print(f"Name: {name}")
print(f"Total Marks: {total}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")

# Check pass/fail
if sub1>=33 and sub2>=33 and sub3>=33 and sub4>=33 and sub5>=33:
    print("Status: PASS :)")
else:
    print("Status: FAIL - Work harder next time!")
    
print("\nMade by Reshma - PGDCA")
