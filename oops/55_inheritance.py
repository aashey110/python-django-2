class University:
    def __init__(self):
        self.university_name = "Tribhuvan University"

class College(University):
    def __init__(self, college_name):
        self.college_name = college_name
        self.teachers = []
        University.__init__(self)

    def add_teachers(self, name, department):
        teacher_name = name
        department = department
        self.teachers.append({"teacher_name": teacher_name, "department": department, "college": self.college_name, "university": self.university_name})
        print("teacher is added")
        self.display_teachers()
        
    def display_teachers(self):
        print(self.teachers)
    
college_obj = College("NCC")
college_obj.add_teachers("manoj", "IT department")