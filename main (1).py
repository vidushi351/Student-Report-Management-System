from student_management import add_student, list_students
from marks_management import add_marks_interactive
from report_generation import generate_report, print_report

def menu():
    print("1. Add Student")
    print("2. Add Marks")
    print("3. Show Report")
    print("4. List Students")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Enter Choice: ")
        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            cls = input("Enter Class: ")
            add_student(sid, name, cls)
            print("Student Added.\n")
        elif choice == "2":
            sid = input("Enter Student ID: ")
            add_marks_interactive(sid)
        elif choice == "3":
            sid = input("Enter Student ID: ")
            ok, result = generate_report(sid)
            if not ok:
                print(result + "\n")
            else:
                print_report(result)
        elif choice == "4":
            students = list_students()
            if not students:
                print("No students.\n")
            else:
                print("\n--- Student List ---")
                for sid, name, cls in students:
                    print(sid, "-", name, "(", cls, ")")
                print()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

main()
