obt_marks = int(input("Enter your marks:"))
total_marks = int(input("Enter total marks:"))
percentage = (obt_marks / total_marks) * 100

marks = int(obt_marks)
if percentage >= 90:
    print("A + grade.")
elif percentage >= 80:
    print("A grade.")
elif percentage >= 70:
    print("B grade.")
elif percentage >= 60:
    print("C grade .")
elif percentage >= 50:
    print("D grade.")
else:
    print("Fail.")
print("Your percentage is", percentage)
print("Your marks are", marks)
