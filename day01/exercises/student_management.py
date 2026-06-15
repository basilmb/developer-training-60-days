all_students = []

def calculate_average(mark_list):
    return sum(mark_list) / len(mark_list)

def calculate_grade(average_mark):
    if average_mark >= 80:
        return "A"
    elif average_mark >= 60:
        return "B"
    elif average_mark >= 40:
        return "c"
    elif average_mark >= 20:
        return "D"
    else:
        return "F"
    
def display_student(name, course, average, grade):
    print(f" \n Student Report \n name: {name} \n course: {course} \n average: {average:.2f} \n grade: {grade} ")
        
while True:
    student_name = input("enter student name: ")
    course_name = input("enter course name: ")
    subjects = ["Maths", "Python", "English"]
    mark_list = []

    print("enter marks out of 100")
    for subject in subjects:
        while True:
            mark = int(input(f"enter mark in {subject}: "))
            if 0 <= mark <= 100:
                mark_list.append(mark)
                break
            print("Mark must be between 0-100")

    average_mark = calculate_average(mark_list)
    grade = calculate_grade(average_mark)
    display_student(student_name, course_name, average_mark, grade)

    student = {"name": student_name, "course": course_name, "average": average_mark, "grade": grade}
    all_students.append(student)
    print(" \n", all_students)
    
    if all_students:
        topper = max(
            all_students,
            key=lambda x:x["average"]
        )
        print(topper["name"])

    choice = input(" \n add more students? y/n: ")
    if choice != "y":
        print(" \n exiting from student management system \n ")
        break