from student_management import get_student

def calculate_percentage(subjects):
    if not subjects:
        return 0
    total = sum(subjects.values())
    return total / len(subjects)

def calculate_grade(pct):
    if pct >= 90: return "S"
    if pct >= 80: return "A"
    if pct >= 70: return "B"
    if pct >= 60: return "C"
    if pct >= 50: return "D"
    if pct >= 40: return "E"
    return "F"

def generate_report(sid):
    student = get_student(sid)
    if not student:
        return False, "Student not found."

    subjects = student["subjects"]
    pct = calculate_percentage(subjects)
    grade = calculate_grade(pct)
    report = {
        "id": student["id"],
        "name": student["name"],
        "class": student["class"],
        "subjects": subjects,
        "percentage": pct,
        "grade": grade
    }
    return True, report

def print_report(report):
    print("REPORT CARD")
    print("ID:", report["id"])
    print("name:", report["name"])
    print("class:", report["class"])
    if not report["subjects"]:
        print("No marks added yet")
        return
    for sub, m in report["subjects"].items():
        print(sub, ":", m)
    print("Percentage:", report["percentage"])
    print("Grade:", report["grade"])
