no_of_subject = int(input("Enter the total number of subjects: "))
max_marks = no_of_subject * 100
total_marks_obtained = 0
marks = 0

for marks in range(no_of_subject):
    while True:
    
        marks_obtained = int(input(f"Enter the marks obtained in subject {marks+1}: "))
    
        if marks_obtained<=100 and marks_obtained > 0:
            total_marks_obtained = marks_obtained + total_marks_obtained
            break
    
        else:
            print("Invalid marks. Please enter marks between 0 and 100.")
        

print("Total marks obtained = ", total_marks_obtained)

percentage= (total_marks_obtained / max_marks) * 100

print("Percentage Obtained = ", percentage)




if percentage >= 90:
    print("You've scored distinction")

elif percentage < 90 and percentage >= 80:
    print("You've scored First division")

elif percentage < 80 and percentage >= 60:
    print("You've scored Second division")

elif percentage < 60 and percentage >= 40:
    print("You've scored Third division")

else:
    print("You've failed")
    