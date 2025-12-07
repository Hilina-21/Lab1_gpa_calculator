class ResultService:

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

    @staticmethod
    def manage_results(students, courses, results):
        print("\n--- RESULT MANAGEMENT ---")
        print("1. Add Result")
        print("2. List Results")
        option = input("Enter choice: ")

        if option == "1":
            ResultService.add_result(students, courses, results)
        elif option == "2":
            ResultService.list_results(results)
        else:
            print("Invalid choice.")

    @staticmethod
    def add_result(students, courses, results):
        sid = input("Enter Student ID: ")
        if sid not in students:
            print("Student not found.")
            return

        cid = input("Enter Course Code: ")
        if cid not in courses:
            print("Course not found.")
            return

        grade = input("Enter Letter Grade (A, B+, C…): ")
        gp = ResultService.DBU_GRADE.get(grade, None)

        if gp is None:
            print("Invalid grade.")
            return

        results.append({"sid": sid, "cid": cid, "grade": grade, "gp": gp})
        print("Result recorded.")

    @staticmethod
   
    def list_results(results):
     if not results:
        print("No results recorded.")
     else:
        print("\n--- RECORDED RESULTS ---")
        for r in results:
            print(f"Student ID: {r['sid']} | Course_id: {r['cid']} | Grade: {r['grade']} | GPA: {r['gp']}")
