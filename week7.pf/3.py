obt_marks = int(input("Enter your marks:"))

total_marks = int(input("Enter total marks:"))

percentage = (obt_marks / total_marks) * 100

if obt_marks > total_marks:
    print("Obtained marks should not be greater than total marks.")
else:
    print(input("Enter your marks again:"))

if total_marks > 300:
    print("Total marks should not be greater than 300.")
else:
    print(input("Enter total marks again:"))

if percentage >= 90:
    print("A + grade.")
elif percentage >= 80:
    print("A grade.")
elif percentage >= 70:
    print("B grade.")
elif percentage >= 60:
    print("C grade.")
elif percentage >= 50:
    print("D grade.")
else:
    print("Fail.")

print ("Your percentage is ", percentage)
print ("Your marks are ", str(int(obt_marks)))


