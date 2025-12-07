class GradeReport:

    @staticmethod
    def generate_report(students, courses, results):
        sid = input("Enter Student ID for GPA Report: ")

        if sid not in students:
            print("Student not found.")
            return

        print("\n==========================================")
        print(f"        GRADE REPORT FOR {students[sid]}")
        print("==========================================")
        print(f"{'Course Code':<12} {'Course Title':<20} {'Grade':<6} {'GP':<4}")
        print("------------------------------------------")

        total_gp = 0
        total_credits = 0
        found = False

        for r in results:
            if r["sid"] == sid:
                found = True
                cid = r["cid"]
                credit = courses[cid]["credit"]
                gp = r["gp"]

                print(f"{cid:<12} {courses[cid]['title']:<20} {r['grade']:<6} {gp:<4}")

                total_gp += gp * credit
                total_credits += credit

        if not found:
            print("No results found for this student.")
            return

        gpa = total_gp / total_credits

        print("\n------------------------------------------")
        print(f"Total Credits: {total_credits}")
        print(f"Final GPA: {gpa:.2f}")
        print("==========================================\n")
