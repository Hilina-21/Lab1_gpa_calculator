FILE_NAME = "courses.txt"

def load_courses():
    courses = {}
    file = open(FILE_NAME, "r")

    for line in file:
        cid, title, credit = line.strip().split(",")
        courses[cid] = {"title": title, "credit": credit}

    file.close()
    return courses

def save_courses(courses):
    file = open(FILE_NAME, "w")

    for cid, info in courses.items():
        file.write(f"{cid},{info['title']},{info['credit']}\n")

    file.close()
    print("✔ Courses saved to file.")

def manage_courses(courses):
    print("\n--- COURSE MANAGEMENT ---")
    print("1. Register Course")
    print("2. List Courses")
    print("3. Exit")
    option = input("Enter choice: ")

    if option == "1":
        register_course(courses)
        save_courses(courses)
    elif option == "2":
        list_courses(courses)
    elif option == "3":
        save_courses(courses)
        print("Exiting course menu...")
        exit()
    else:
        print("Invalid choice.")


def register_course(courses):
    cid = input("Enter Course Code: ")

    if cid in courses:
        print("Error: Course already exists!")
        return

    title = input("Enter Course Title: ")
    credit = input("Enter Course Credit: ")

    if not credit.isdigit():
        print("Error: Credit must be a number!")
        return

    courses[cid] = {
        "title": title,
        "credit": credit
    }

    print("✔ Course registered successfully.")

def list_courses(courses):
    if len(courses) == 0:
        print("No courses registered.")
    else:
        print("\nRegistered Courses:")
        for cid, info in courses.items():
            print(
                f"  course-id={cid} - title={info['title']} (credit={info['credit']} hr)"
            )
