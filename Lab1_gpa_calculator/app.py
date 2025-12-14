from students.StudentService import manage_students
from courses.CourseService import manage_courses
from results.ResultService import manage_results
from gradereports.GradeReport import generate_report

students = {}
courses = {}
results = []

def menu():
    print("\n===== GPA CALCULATOR =====")
    print("1. Students")
    print("2. Courses")
    print("3. Results")
    print("4. Grade Reports")
    print("5. Exit")
    return input("Enter choice: ")

while True:
    choice = menu()

    if choice == "1":
        manage_students(students)

    elif choice == "2":
        manage_courses(courses)

    elif choice == "3":
        manage_results(students, courses, results)

    elif choice == "4":
        generate_report(students, courses, results)

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
