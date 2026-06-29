import json
import os
from student import Student

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
        print("\nNo previous student database found.")
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