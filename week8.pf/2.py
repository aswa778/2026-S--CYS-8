c = int(input("Enter total students :"))
i = 1
while i < c:
     name = str(input("Enter your name :"))
     roll_number = int(input("Enter your roll number :"))
     obt_marks = int(input("Enter your marks :"))
     total_marks = int(input("Enter total marks :"))
     percentage = (obt_marks / total_marks) * 100
     marks = int(obt_marks)
     if percentage >= 90:
        print("A + grade.")
     elif percentage >= 80:
        print("A grade.")
     elif percentage >= 70:
        print("B grade.")
     elif percentage >= 60:
        print("C grade.")
     elif percentage >= 50:
        print("D garde.")
     else:
        print("Fail.")
     print("Name :", name)
     print("Roll_number:", roll_number)
     print("Your percentage is", percentage)
     print("Your marks are", marks)

i = i+1

     