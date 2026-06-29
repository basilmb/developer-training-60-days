class Student:
    all_instances = []
    
    def __init__(self, name, course, mark):
        self.student_name = name
        self.course_name = course            
        self.mark_list = dict(mark)
        self.average_mark = 0.0
        self.grade = "F"
        
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
        
    def to_dict(self):
        return{
            "student_name": self.student_name,
            "course_name": self.course_name,
            "mark_list": self.mark_list,
            "average_mark" : self.average_mark,
            "grade" : self.grade
        }