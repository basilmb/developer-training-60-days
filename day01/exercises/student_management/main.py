from student import Student
from database import (
    load_json,
    save_student,
    find_student,
    delete_student
)

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

subjects = []

def main():
    load_json()
        
    global subjects
    for student in Student.all_instances:
        for sub in student.mark_list.keys():
            if sub not in subjects:
                subjects.append(sub)

    while True:
        print("\nClick Corresponding Number")
        print("1. Add Subject")
        print("2. Add Students.")
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
                if subjects:
                    add_student(subjects)
                else:
                    print("\nPlease add at least one subject before registering a student!")
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