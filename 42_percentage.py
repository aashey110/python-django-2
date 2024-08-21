marks = {

}

subjects = ["Math", "Social", "Science", "Nepali", "English", "Computer"]
total_marks = 0

for subject in subjects:
    marks[subject] = int(input(f"Enter marks for {subject}: "))
    total_marks = total_marks + marks[subject]
    percentage = total_marks/len(subjects)



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