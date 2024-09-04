#print mark and student name using loop from data = [{'name':'salman', 'percentage' : 45},{'name':'mithun', 'percentage' : 56},{'name':'katrina', 'percentage' : 75}]

student_info = {}
student_list = []
for i in range(3):
    student_name = input("\nEnter the name of the student:")
    student_percentage = int(input("Enter the percentage of the student:"))
    student_info[student_name] = student_percentage

student_list.append(student_info)
print(student_list)