import json
import os

def save_student(filename = "student.json"):
    data_list = [student.to_dict() for student in Student.all_instances]
    
    try:
        with open(filename, "w") as file:
            json.dump(data_list, file, indent=4)
            print(f"successfully saved {len(data_list)} students to {filename}")
    except Exception as e:
        print(f"an error occurred while saving {e}")
        
def load_json(filename="student.json"):
    if not os.path.exists(filename):
        print("No previous student database found.")
        return
    try:
        with open(filename, "r") as file:
            data_list = json.load(file)
        for data in data_list:
            student = Student(name=data["student_name"], course=data["course_name"], mark=data["mark_list"])
            student.average_mark = data["average_mark"]
            student.grade = data["grade"]
        print(f"\nSuccessfully loaded {len(Student.all_instances)} students from {filename}")
    except Exception as e:
        print(f"[Warning] Error loading database: {e}.")
        
def find_student(name):
    for student in Student.all_instances:
        if name.strip().lower() == student.student_name.strip().lower():
            return student
    return None

def delete_student(name):
    student = find_student(name)
    if student:
        Student.all_instances.remove(student)
        return True
    return False

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
        
def add_student(subjects):
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
        
def main():
    load_json()
        
    subjects = ["Maths", "Python", "English"]

    while True:
        print("\nClick Corresponding Number")
        print("1. Add More Subject")
        print("2. Add More Students.")
        print("3. Display All Students.")
        print("4. Display Top Student.")
        print("5. Search Student.")
        print("6. Delete Student.")
        print("7. Exit.")
        choice = input("Enter choice: ").strip()        
        if choice not in ["1", "2", "3", "4", "5","6","7"]:
            print("Invalid choice!")
            continue    
        match choice:
            case "1":
                new_sub = input("Enter the Subject to Add: ")
                subjects.append(new_sub)
                for student in Student.all_instances:
                    new_mark = int(input(f"mark in {new_sub} for {student.student_name}: "))
                    student.mark_list[new_sub] = new_mark
                    student.calculate_average()
                    student.calculate_grade()
            case "2":
                add_student(subjects)
            case "3":
                for student_obj in Student.all_instances:
                    student_obj.display_student()
            case "4":
                top_student = max(Student.all_instances, key = lambda student: student.average_mark)
                top_student.display_student()
            case "5":
                search_name = input("Enter student name to search: ")
                target_student = find_student(search_name)
                if target_student:
                    print("\nStudent Found:")
                    target_student.display_student()
                else:
                    print(f"\nStudent '{search_name}' not found in the database.")
            case "6":
                delete_name = input("Enter student name to delete: ")
                confirm = input(f"Are you sure you want to permanently delete '{delete_name}'? (y/n): ")
                if confirm.lower() == "y":
                    deleted_student = delete_student(delete_name)
                    if deleted_student:
                        print(f"\nSuccessfully deleted '{delete_name}' from the database.")
                    else:
                        print(f"\nStudent '{delete_name}' not found.")
                else:
                    print("\nDeletion canceled.")
            case "7":
                save_student()
                print("Exiting from Student Management. Goodbye!")
                break
            
if __name__ == "__main__":
    main()