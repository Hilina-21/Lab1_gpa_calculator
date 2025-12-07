class CourseService:

    @staticmethod
    def manage_courses(courses):
        print("\n--- COURSE MANAGEMENT ---")
        print("1. Register Course")
        print("2. List Courses")
        option = input("Enter choice: ")

        if option == "1":
            CourseService.register_course(courses)
        elif option == "2":
            CourseService.list_courses(courses)
        else:
            print("Invalid choice.")

    @staticmethod
    def register_course(courses):
        cid = input("Enter Course Code: ")
        title = input("Enter Course Title: ")
        credit = int(input("Enter Course Credit: "))
        courses[cid] = {"title": title, "credit": credit}
        print("Course registered successfully.")

    @staticmethod
    def list_courses(courses):
        if not courses:
            print("No courses registered.")
        else:
            print("\nRegistered Courses:")
            for cid, info in courses.items():
                print(f"  course-id={cid} -  title={info['title']} (  credit={info['credit']} hr)")
