total_student_list = []

total_student = int(input("\nEnter total number of student: "))

for student in range(total_student):

    student_name = input("\nEnter student name: ")

    subject_mark = {}

    obtained_mark = 0


    total_subject = int(input("\nEnter total number of subjects: "))


    total_mark = total_subject * 100


    for i in range(total_subject):

        subject = input("\nEnter the name of subject: ")
        mark = input(f"\nEnter marks obtained in {subject}: ")
        subject_mark[subject] = mark

        obtained_mark = obtained_mark + int(mark)

    percentage = (obtained_mark/total_mark) * 100

    if percentage >= 90:
        division = 'Distinction'

    elif percentage < 90 and percentage >= 80:
        division = 'First Division'

    elif percentage < 80 and percentage >= 60:
        division = 'Second Division'

    elif percentage < 60 and percentage >= 40:
        division = 'Third Division'

    else:
        division = 'Fail'



    subject_mark['percentage'] = percentage

    subject_mark['division'] = division

    subject_mark['student_name'] = student_name

    total_student_list.append(subject_mark)

print(total_student_list)


#give example  of each

#create list
#append data to list and print
#access list item using for loop

#create dictionary
#append data to dictionary and print
#how to access and change value of dictionary
#access dictionary item using for loop

#add dictionary to list
#print mark and student name using loop from data = [{'name':'salman', 'percentage' : 45},{'name':'mithun', 'percentage' : 56},{'name':'katrina', 'percentage' : 75}]
