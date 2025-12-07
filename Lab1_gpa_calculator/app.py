from students.StudentService import StudentService
from courses.CourseService import CourseService
from results.ResultService import ResultService
from gradereports.GradeReport import GradeReport

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
        StudentService.manage_students(students)

    elif choice == "2":
        CourseService.manage_courses(courses)

    elif choice == "3":
        ResultService.manage_results(students, courses, results)

    elif choice == "4":
        GradeReport.generate_report(students, courses, results)

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
