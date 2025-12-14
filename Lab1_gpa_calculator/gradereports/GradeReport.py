def generate_report(students, courses, results):
    sid = input("Enter Student ID for GPA Report: ")

    if sid not in students:
        print("Student not found.")
        return

    file_name = "grade_report_" + sid + ".txt"
    file = open(file_name, "w")

    print("\n==========================================")
    print(f"        GRADE REPORT FOR {students[sid]}")
    print("==========================================")
    print(f"{'Course Code':<12} {'Course Title':<20} {'Grade':<6} {'GP':<4}")
    print("------------------------------------------")

    file.write("==========================================\n")
    file.write(f"        GRADE REPORT FOR {students[sid]}\n")
    file.write("==========================================\n")
    file.write(f"{'Course Code':<12} {'Course Title':<20} {'Grade':<6} {'GP':<4}\n")
    file.write("------------------------------------------\n")

    total_gp = 0
    total_credits = 0
    found = False

    for r in results:
        if r["sid"] == sid:
            found = True
            cid = r["cid"]
            credit = int(courses[cid]["credit"])
            gp = float(r["gp"])

            line = (
                f"{cid:<12} "
                f"{courses[cid]['title']:<20} "
                f"{r['grade']:<6} "
                f"{gp:<4}\n"
            )

            print(
                f"{cid:<12} "
                f"{courses[cid]['title']:<20} "
                f"{r['grade']:<6} "
                f"{gp:<4}"
            )

            file.write(line)

            total_gp += gp * credit
            total_credits += credit

    if not found:
        print("No results found for this student.")
        file.write("No results found for this student.\n")
        file.close()
        return

    gpa = total_gp / total_credits

    print("\n------------------------------------------")
    print(f"Total Credits: {total_credits}")
    print(f"Final GPA: {gpa:.2f}")
    print("==========================================\n")

    file.write("------------------------------------------\n")
    file.write(f"Total Credits: {total_credits}\n")
    file.write(f"Final GPA: {gpa:.2f}\n")
    file.write("==========================================\n")

    file.close()

    print(f" Grade report saved to file: {file_name}")
