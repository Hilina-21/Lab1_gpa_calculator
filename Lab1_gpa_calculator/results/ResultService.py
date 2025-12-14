FILE_NAME = "results.txt"
DBU_GRADE = {
    "A": 4.0,
    "A-": 3.75,
    "B+": 3.5,
    "B": 3.0,
    "B-": 2.75,
    "C+": 2.5,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
}

def load_results():
    results = []
    file = open(FILE_NAME, "r")

    for line in file:
        sid, cid, grade, gp = line.strip().split(",")
        results.append({
            "sid": sid,
            "cid": cid,
            "grade": grade,
            "gp": gp
        })

    file.close()
    return results

def save_results(results):
    file = open(FILE_NAME, "w")

    for r in results:
        file.write(f"{r['sid']},{r['cid']},{r['grade']},{r['gp']}\n")

    file.close()
    print("✔ Results saved to file.")


def manage_results(students, courses, results):
    print("\n--- RESULT MANAGEMENT ---")
    print("1. Add Result")
    print("2. List Results")
    print("3. Exit")
    option = input("Enter choice: ")

    if option == "1":
        add_result(students, courses, results)
        save_results(results)
    elif option == "2":
        list_results(results)
    elif option == "3":
        save_results(results)
        print("Exiting result menu...")
        exit()
    else:
        print("Invalid choice.")


def add_result(students, courses, results):
    sid = input("Enter Student ID: ")
    if sid not in students:
        print("Student not found.")
        return

    cid = input("Enter Course Code: ")
    if cid not in courses:
        print("Course not found.")
        return

    grade = input("Enter Letter Grade (A, A-, B+, ...): ")

    if grade not in DBU_GRADE:
        print("Invalid grade.")
        return

    gp = DBU_GRADE[grade]

    results.append({
        "sid": sid,
        "cid": cid,
        "grade": grade,
        "gp": gp
    })

    print("✔ Result recorded.")


def list_results(results):
    if len(results) == 0:
        print("No results recorded.")
    else:
        print("\n--- RECORDED RESULTS ---")
        for r in results:
            print(
                f"Student ID: {r['sid']} | "
                f"Course ID: {r['cid']} | "
                f"Grade: {r['grade']} | "
                f"GPA: {r['gp']}"
            )
