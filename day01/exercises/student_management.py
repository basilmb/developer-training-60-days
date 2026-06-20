class Student:
    all_instances = []
    
    def __init__(self, name, course, mark):
        self.student_name = name
        self.course_name = course
        self.mark_list = dict(mark)
        
        Student.all_instances.append(self)

    def calculate_average(self):
        self.average_mark =  sum(self.mark_list.values()) / len(self.mark_list)

    def calculate_grade(self):
        if self.average_mark >= 80:
            self.grade =  "A"
        elif self.average_mark >= 60:
            self.grade = "B"
        elif self.average_mark >= 40:
            self.grade =  "C"
        elif self.average_mark >= 20:
            self.grade = "D"
        else:
            self.grade = "F"
    
    def display_student(self):
        print(f"\n Name: {self.student_name}\n Course: {self.course_name}")
        for key, value in self.mark_list.items():
            print(f" {key}: {value}")
        print(f" Average: {self.average_mark:.2f}\n Grade: {self.grade}")
        
subjects = ["Maths", "Python", "English"]    

while True:    
    print("Subjects in the Student Management are: ", subjects)
    choice = input("Do you Want to Add More Subjects (y/n)?: ")
    if choice not in ["y", "n"]:
        print("Invalid Entry")

    if choice == "y":
        subjects.append(input("Enter new Subject: "))
    else:
        print("Enter Students Details")
        break
        
status="true"
       
while status=="true":
    student_name = input("enter student name: ")
    course_name = input("enter course name: ")
    mark_list = {}

    print("enter marks out of 100")
    for subject in subjects:
        while True:
            mark = int(input(f"enter mark in {subject}: "))
            if 0 <= mark <= 100:
                mark_list[subject] = mark
                break
            print("Mark must be between 0-100")
            
    student = Student(student_name, course_name, mark_list)
    student.calculate_average()
    student.calculate_grade()
    student.display_student()

    while True:
        option = input("\nClick Corresponding Number\n1. Add More Subject\n2. Add More Students.\n3. Display All Students.\n4. Dasplay Top Student.\n5. Exit.\n")
        if option not in ["1", "2", "3", "4", "5"]:
            print("Invalid Selection")    
        match option:
            case "1":
                new_sub = input("Enter the Subject to Add: ")
                subjects.append(new_sub)
                for student_obj in Student.all_instances:
                    new_mark = input(f"mark in {new_sub} for {student_obj.student_name}: ")
                    student_obj.mark_list[new_sub] = new_mark
                status="fail"
                continue
            case "2":
                status="true"
                break
            case "3":
                for student_obj in Student.all_instances:
                    student_obj.display_student()
                status="fail"
                continue
            case "4":
                top_student = max(Student.all_instances, key = lambda student: student.average_mark)
                top_student.display_student()
                status="fail"
                continue
            case "5":
                print("Exiting from Student Mansagement")
                status="fail"
                break