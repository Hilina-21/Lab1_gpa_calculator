FILE_NAME = "students.txt"
def load_students():
    students = {}
    file = open(FILE_NAME, "r")

    for line in file:
        if line.strip() != "":
            sid, name = line.strip().split(",")
            students[sid] = name

    file.close()
    return students

def save_students(students):
    file = open(FILE_NAME, "w")

    for sid, name in students.items():
        file.write(sid + "," + name + "\n")

    file.close()
    print("✔ Students saved to file.")

def manage_students(students):
    print("\n--- STUDENT MANAGEMENT ---")
    print("1. Register Student")
    print("2. List Students")
    print("3. Exit")
    option = input("Enter choice: ")

    if option == "1":
        register_student(students)
        save_students(students)
    elif option == "2":
        list_students(students)
    elif option == "3":
        save_students(students)
        print("Exiting program...")
        exit()
    else:
        print("Invalid choice.")


def register_student(students):
    sid = input("Enter Student ID (integer only): ")

    if not sid.isdigit():
        print("Error: Student ID must be an integer!")
        return

    if sid in students:
        print("Error: This Student ID is already registered!")
        return

    name = input("Enter Student Name: ")
    students[sid] = name
    print("✔ Student registered successfully with ID " + sid + ".")


def list_students(students):
    if len(students) == 0:
        print("No students registered.")
    else:
        print("\nRegistered Students:")
        for sid in students:
            print("  id=" + sid + " - name=" + students[sid])
