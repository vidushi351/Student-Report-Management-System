from student_management import student_exists, get_student

def add_mark(sid, subject, mark):
    
    if not student_exists(sid):
        return False, "Student not found."
    student = get_student(sid)
    student["subjects"][subject] = mark
    return True, "Mark added."

def add_marks_interactive(sid):
    
    if not student_exists(sid):
        print("Student not found.\n")
        return

    while True:
        sub = input("Enter Subject (press Enter to stop): ")
        if sub == "":
            break

        m = input("Enter Mark (numbers only): ")

        
        if m.isdigit():
            m = int(m)  
            success, msg = add_mark(sid, sub, m)
            if not success:
                print(msg)
        else:
            print("Invalid input! Enter numbers only.")

    print("Marks Updated")
