class StudentService:

    @staticmethod
    def manage_students(students):
        print("\n--- STUDENT MANAGEMENT ---")
        print("1. Register Student")
        print("2. List Students")
        option = input("Enter choice: ")

        if option == "1":
            StudentService.register_student(students)
        elif option == "2":
            StudentService.list_students(students)
        else:
            print("Invalid choice.")

    @staticmethod
    def register_student(students):
        sid = input("Enter Student ID: ")

        # Check if ID already exists
        if sid in students:
            print(" Error: This Student ID is already registered!")
            return  # stop registration

        name = input("Enter Student Name: ")
        students[sid] = name
        print("✔ Student registered successfully.")

    @staticmethod
    def list_students(students):
        if not students:
            print("No students registered.")
        else:
            print("\nRegistered Students:")
            for sid, name in students.items():
                print(f"  id={sid} - name={name}")
